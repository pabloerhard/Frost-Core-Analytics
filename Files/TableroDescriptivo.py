import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from streamlit_toggle import st_toggle_switch
from datetime import date
# from Statics.Data import df_final  as df_final

def main():
    st.markdown(
        """
        <style>
        .st-emotion-cache-1wivap2 {
            font-size: 23px !important; /* Ajusta el tamaño de la fuente según tus necesidades */
        }
        .st-emotion-cache-10trblm.e1nzilvr1 {
            font-size: 24px; /* Ajusta el tamaño del título aquí */
            text-align: center; /* Centra el texto */
        }
        .centered-title {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100px; /* Ajusta la altura del contenedor según sea necesario */
        }
        .st-bl.st-ak.st-bm.st-bn.st-bo.st-ar.st-bp.st-bq.st-br {
            font-size: 15px;  /* Ajusta el tamaño de la fuente aquí */
        }
        
        </style>
        """,
        unsafe_allow_html=True
    )



    # Título del tablero
    st.title("FrostCore Analytics")


    #Crear tres columnas 
    col1,col2,col3=st.columns(3)




    toggle = st_toggle_switch(label="Base de datos limpia",
                            key="toggle",
                            default_value=False,
                            label_after=False,
                            inactive_color="#D3D3D3", 
                            active_color="#11567f", 
                            track_color="#29B5E8")



    # Añadir el CSS y el JavaScript para mover el toggle switch al lado del título
    st.markdown("""
        <style>
            .title-container {
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .title-container h1 {
                margin: 0;
            }
        </style>
        <script>
            document.addEventListener("DOMContentLoaded", function() {
                const titleElement = document.querySelector('h1');
                const toggleElement = document.querySelector('div[data-testid="stToggleSwitch"]');

                if (titleElement && toggleElement) {
                    const container = document.createElement('div');
                    container.className = 'title-container';
                    titleElement.parentNode.insertBefore(container, titleElement);
                    container.appendChild(titleElement);
                    container.appendChild(toggleElement);
                }
            });
        </script>
    """, unsafe_allow_html=True)

    if toggle:
        csv_file = 'Statics/Data/df_final.csv'
    else:
        csv_file = 'Statics/Data/df_final1.csv'
        

    # Cargar los datos
    df = pd.read_csv(csv_file)





    # Convertir las fechas a formato datetime
    df['Fecha'] = pd.to_datetime(df['Fecha'])
    # Seleccionar solo las columnas especificadas
    df_filtered = df[['Pintura', 'Litros Totales', 'Valor USD', 'Area', 'Espesor', 'Rendimiento Diario', 'Rendimiento Std', 'Diferencia de Rendimientos']]
    df_filtered = df_filtered.groupby('Pintura').sum().reset_index()
    # Obtener el filtro anterior y los valores anteriores de litros totales y dinero total
    prev_linea = st.session_state.get('linea', 'All')
    prev_total_litros = st.session_state.get('total_litros', 0)
    prev_total_valor = st.session_state.get('total_valor', 0)
    default_start_date = date(2021,8,8)
    default_end_date = date(2021,12,12)

    # Definiendo los límites para los date inputs
    min_date = date(2021, 1, 1)  # Ejemplo de fecha mínima
    max_date = date.today()  # La fecha de hoy como máximo


    #--------------------------------- COLUMNA 1 -----------------------------------------

    # Filtros de línea y rango de fechas en el col1
    with col1:
        linea = st.selectbox('Linea', options=['All', 'Pintado 1', 'Pintado 2'])
        st.markdown("<br>", unsafe_allow_html=True)
        with st.container():
            subcol2,subcol3 = st.columns(2)
            with subcol2:
                fecha_inicial = st.date_input('Fecha Inicial', value=default_start_date, min_value=min_date, max_value=max_date)
            with subcol3:
                fecha_final = st.date_input('Fecha Final', value=default_end_date, min_value=min_date, max_value=max_date)
        top_pinturas_litros = df.groupby('Pintura')['Litros Totales'].sum().nlargest(5)
        df_top_70 = df[df['Pintura'].isin(top_pinturas_litros.index)]
        #Aplicar filtros
        if linea != 'All':
            df = df[df['Linea'] == linea]
        df = df[(df['Fecha'] >= pd.to_datetime(fecha_inicial)) & (df['Fecha'] <= pd.to_datetime(fecha_final))]
        #Sacar top pinturas para box plot
        df_top_70 = df[df['Pintura'].isin(top_pinturas_litros.index)]


        # Filtrar los datos para el rango intercuartil (entre los percentiles 5 y 95)
        lower_quantile = df_top_70['Diferencia de Rendimientos'].quantile(0.05)
        upper_quantile = df_top_70['Diferencia de Rendimientos'].quantile(0.95)
        filtered_df = df_top_70[(df_top_70['Diferencia de Rendimientos'] >= lower_quantile) & 
                                (df_top_70['Diferencia de Rendimientos'] <= upper_quantile)]

        # Crear el boxplot con Plotly Express
        fig = px.box(filtered_df, x='Pintura', y='Diferencia de Rendimientos', color='Pintura',title='Diferencia de Rendimientos')
        fig.update_traces(marker_color='#FFA500')  # Establece el color naranja
        # Personalizar el diseño del gráfico
        fig.update_layout(
            plot_bgcolor='lightgrey',  # Color de fondo del gráfico
            paper_bgcolor='lightgrey',
            xaxis_title="Pintura",
            yaxis_title="Diferencia de Rendimientos",
            margin=dict(l=0, r=0, t=40, b=0),
            xaxis_tickangle=-90,  # Etiquetas del eje x en orientación vertical
            showlegend=False,
            height=400,
            width=300,
            font=dict(size=10)  # Ajusta el tamaño de la fuente
        )

        st.plotly_chart(fig)
        
        

    # Filtrar los datos según los filtros seleccionados
    if linea != 'All':
        df = df[df['Linea'] == linea]
    df = df[(df['Fecha'] >= pd.to_datetime(fecha_inicial)) & (df['Fecha'] <= pd.to_datetime(fecha_final))]

    # Cálculos de kpis
    total_litros = df['Litros Totales'].sum()
    total_valor = df['Valor USD'].sum()

    # Comparar con los valores anteriores para calcular el delta
    litros_delta = (total_litros - prev_total_litros) / prev_total_litros * 100 if prev_total_litros != 0 else 0
    valor_delta = (total_valor - prev_total_valor) / prev_total_valor * 100 if prev_total_valor != 0 else 0

    # Guardar los valores actuales para la próxima iteración
    st.session_state.linea = linea
    st.session_state.total_litros = total_litros
    st.session_state.total_valor = total_valor

    #--------------------------------- COLUMNA 2 -----------------------------------------

    # Gráficas de pie en col2
    # Gráfica de boxplot para diferencia de rendimientos en col2





    with col2:
        top_pinturas_litros = df.groupby('Pintura')['Litros Totales'].sum().nlargest(5)
        top_pinturas_area = df.groupby('Pintura')['Area'].sum().nlargest(5)

    # Gráfico de barras horizontal para Top Pinturas Por Litros
        fig1 = px.bar(x=top_pinturas_litros.values, y=top_pinturas_litros.index, orientation='h', title='Top Pinturas Por Litros')
        fig1.update_traces(marker_color='#FFA500', text=top_pinturas_litros.values, textposition='inside')  # Coloca las etiquetas dentro de las barras
        fig1.update_layout(
            plot_bgcolor='lightgrey',  # Color de fondo del gráfico
            paper_bgcolor='lightgrey',
            xaxis_title="Litros",
            yaxis_title="Pintura",
            yaxis=dict(showticklabels=True),  # Muestra las etiquetas del eje y
            height=235,
            width=400,
            margin=dict(l=0, r=0, t=30, b=0),
            clickmode='event+select',
            showlegend=False,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            font=dict(size=17)  # Ajusta el tamaño de la fuente
        )
        st.plotly_chart(fig1)

        # Gráfico de barras horizontal para Top Pinturas Por Área
        fig2 = px.bar(x=top_pinturas_area.values, y=top_pinturas_area.index, orientation='h', title='Top Pinturas Por Area')
        fig2.update_traces(marker_color='#FFA500', text=top_pinturas_area.values, textposition='inside')  # Coloca las etiquetas dentro de las barras
        fig2.update_layout(
            plot_bgcolor='lightgrey',  # Color de fondo del gráfico
            paper_bgcolor='lightgrey',
            xaxis_title="Área",
            yaxis_title="Pintura",
            yaxis=dict(showticklabels=True),  # Muestra las etiquetas del eje y
            height=235,
            width=400,
            margin=dict(l=0, r=0, t=30, b=0),
            clickmode='event+select',
            showlegend=False,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            font=dict(size=17)  # Ajusta el tamaño de la fuente
        )
        st.plotly_chart(fig2)




    #--------------------------------- COLUMNA 3 -----------------------------------------

    # Cajas comparativas de litros y dinero en col3
    # Gráficas de líneas en col3
    area_por_fecha = df.groupby('Fecha')['Area'].sum().reset_index()
    dinero_por_fecha = df.groupby('Fecha')['Valor USD'].sum().reset_index()
    with col3:
        with st.container():
            subcol11, subcol22 = st.columns(2)
            with subcol11:
                if total_litros > 1000000:
                    st.metric(label="Litros Totales", value=f"{total_litros/1000000:.1f}M", delta=f"{litros_delta:.1f}%")
                else:
                    st.metric(label="Litros Totales", value=f"{total_litros/1000:.1f}K", delta=f"{litros_delta:.1f}%")
            with subcol22:
                if total_valor > 1000000:
                    st.metric(label="Dinero", value=f"{total_valor/1000000:.1f}M", delta=f"{valor_delta:.1f}%")
                else:
                    st.metric(label="Dinero", value=f"{total_valor/1000:.1f}K", delta=f"{valor_delta:.1f}%")

        
        fig3 = px.line(area_por_fecha, x='Fecha', y='Area', title='Area', labels={'Area': 'Area', 'Fecha': 'Fecha'}, color_discrete_sequence=['orange'])
        fig3.update_layout(height=200,plot_bgcolor='lightgrey',  # Color de fondo del gráfico
            paper_bgcolor='lightgrey', width=325,margin=dict(l=0, r=0, t=20, b=0))  # Ajusta el tamaño de la gráfica
        st.plotly_chart(fig3)
        
        fig4 = px.line(dinero_por_fecha, x='Fecha', y='Valor USD', title='Dinero', labels={'Valor USD': 'Dinero (USD)', 'Fecha': 'Fecha'}, color_discrete_sequence=['orange'])
        fig4.update_layout(height=200, width=325,plot_bgcolor='lightgrey',  # Color de fondo del gráfico
            paper_bgcolor='lightgrey',margin=dict(l=0, r=0, t=20, b=0,))  # Ajusta el tamaño de la gráfica
        st.plotly_chart(fig4)


    if linea != 'All':
        df = df[df['Linea'] == linea]
    df = df[(df['Fecha'] >= pd.to_datetime(fecha_inicial)) & (df['Fecha'] <= pd.to_datetime(fecha_final))]
    df_filtered = df[['Pintura', 'Litros Totales', 'Valor USD', 'Area', 'Espesor']]
    df_filtered = df_filtered.groupby('Pintura').sum().reset_index()
    st.dataframe(df_filtered)
if __name__ == "__main__":
    main()