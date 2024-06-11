import streamlit as st
import numpy as np
import plotly.express as px
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import explained_variance_score
import plotly.graph_objects as go

st.set_page_config(layout="wide")


# Custom CSS to adjust font size and column widths
st.markdown(
    """
    <style>
    /* Your existing CSS styles */
    /* Adjusting the width and height of select boxes and buttons */
    div[data-baseweb="select"] {
        width: 200px !important; /* Adjust the width as needed */
        height: 1px !important; /* Adjust the height as needed */
    }
    button[kind="primary"] {
        width: 90px !important; /* Adjust the width as needed */
        height: 10px !important; /* Adjust the height as needed */
    }

    /* Adjusting the font size of labels above select boxes */
    .stSelectbox label {
        font-size: 5px; /* Adjust the font size as needed */
    }

    /* Adjusting the metrics' background and font size */
    .stMetric {
        background-color: #F5F5F5; /* Light grey background for metrics */
        padding: 0px;
        border-radius: 4px;
    }

    /* Adjusting the font size of values within metrics */
    .stMetric > div > div > span {
        font-size: 11px !important; /* Adjust the font size as needed */
    }

    /* Adjusting the font size for tables */
    .css-1d391kg, .css-1y0tads {
        font-size: 14px; /* Adjust table font size */
    }

    /* Reduce the padding and margin for the top container */
    .css-1d3z3hw {
        padding-top: 0px;
        padding-bottom: 0px;
    }

    /* Custom table styles */
    .dataframe {
        font-size: 10px; /* Smaller font size */
        padding: 0px;
        margin: 0px;
    }

    /* Adjusting the width of input text boxes */
    .stTextInput div {
        width: 100px !important; /* Adjust the width as needed */
    }
    
    /* Adjusting the font size of metric values */
    [data-testid="stMetricValue"] {
        font-size: 20px !important;
    }

    /* Reduce padding/margin between elements */
    .css-1v0mbdj, .css-1owbyjr, .css-1b4mlwb {
        margin: 0px !important; /* Reduce margins */
        padding: 0px !important; /* Reduce padding */
    }

    /* Additional styles for further customization */
    .stMarkdown {
        margin-bottom: 0px !important; /* Reduce bottom margin of st.markdown */
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Sample data for graphs
df = pd.read_csv('DF_Final_Reto_2.0.csv', index_col=2)
unnamed_columns = df.columns[df.columns.str.contains('Unnamed')]
df.drop(columns=unnamed_columns, inplace=True)

comparacion_columns = df.columns[df.columns.str.contains('_comparacion')]
df.drop(columns=comparacion_columns, inplace=True)
pintura_ranking = df.groupby('Pintura')['Litros Totales'].sum().sort_values(ascending=False)

total_litros = pintura_ranking.sum()
cumulative_percent = pintura_ranking.cumsum() / total_litros
top_pinturas = cumulative_percent[cumulative_percent <= 0.3].index.tolist()

df_top_pinturas = df[df['Pintura'].isin(top_pinturas)].copy()

label_encoder = LabelEncoder()
df_top_pinturas['Linea_encoded'] = label_encoder.fit_transform(df_top_pinturas['Linea'])

pintura_options = ["Todas"] + df_top_pinturas['Pintura'].unique().tolist()

def random_forest(df, test_size):
    X = df[[ 'Rendimiento Std', 'Area', 'Espesor']]
    y = df['Litros Totales']

    # Dividir los datos en conjunto de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=(test_size / 100), random_state=42)

    # Inicializar y ajustar el modelo RandomForestRegressor
    modelRF = RandomForestRegressor(n_estimators=70, random_state=42)
    modelRF.fit(X_train, y_train)

    # Realizar predicciones en los conjuntos de entrenamiento y prueba
    y_train_pred_RF = modelRF.predict(X_train)
    y_test_pred_RF = modelRF.predict(X_test)

    # Calcular métricas de evaluación
    mse_test_RF = mean_squared_error(y_test, y_test_pred_RF)
    r2_test_RF = r2_score(y_test, y_test_pred_RF)
    mape_test_RF = np.mean(np.abs((y_test - y_test_pred_RF) / y_test)) * 100
    explained_variance = explained_variance_score(y_test, y_test_pred_RF)

    # Devolver las métricas de evaluación, los datos de entrenamiento y prueba, las predicciones y el modelo entrenado
    return mse_test_RF, r2_test_RF,explained_variance, y_train, y_train_pred_RF, y_test, y_test_pred_RF, modelRF,mape_test_RF
def gradient_boosting(df, test_size):
    X = df[[ 'Rendimiento Std', 'Area', 'Espesor']].values
    y = df['Litros Totales'].values

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=(test_size/100), random_state=42)

    # Scale the features and target variable
    scaler_X = MinMaxScaler(feature_range=(0, 1))
    X_train_scaled = scaler_X.fit_transform(X_train)
    X_test_scaled = scaler_X.transform(X_test)
    scaler_y = MinMaxScaler(feature_range=(0, 1))
    y_train_scaled = scaler_y.fit_transform(y_train.reshape(-1, 1)).ravel()
    y_test_scaled = scaler_y.transform(y_test.reshape(-1, 1)).ravel()

    # Initialize and train the GradientBoostingRegressor model
    model = GradientBoostingRegressor(random_state=42)
    model.fit(X_train_scaled, y_train_scaled)

    # Make predictions on the training and testing sets
    y_train_pred_scaled = model.predict(X_train_scaled)
    y_test_pred_scaled = model.predict(X_test_scaled)
    
    # Inverse transform the predictions to the original scale
    y_train_pred = scaler_y.inverse_transform(y_train_pred_scaled.reshape(-1, 1)).flatten()
    y_test_pred = scaler_y.inverse_transform(y_test_pred_scaled.reshape(-1, 1)).flatten()

    # Calculate evaluation metrics
    mse_train = mean_squared_error(y_train, y_train_pred)
    r2_train = r2_score(y_train, y_train_pred)

    mse_test = mean_squared_error(y_test, y_test_pred)
    r2_test = r2_score(y_test, y_test_pred)
    
    # Calculate MAPE
    mape_test = np.mean(np.abs((y_test - y_test_pred) / y_test)) * 100

    explained_variance = explained_variance_score(y_test, y_test_pred)

    # Return the evaluation metrics, training/testing data and predictions, and the trained model
    return mse_train, r2_train,explained_variance,  y_train, y_train_pred, y_test, y_test_pred, model,mape_test, scaler_X, scaler_y




# Main container
with st.container():
    # First row: Select boxes on top
    select_cols = st.columns([2, 1, 2, 4])  # Adjust column ratios as needed
    with select_cols[0]:
        pintura = st.selectbox("Pintura", options=pintura_options)
    with select_cols[1]:
        entrenamiento = st.text_input("Entrenamiento", "30")  # Default value is 50%
    with select_cols[2]:
        variable = st.selectbox("Modelo", options=["Random Forest", "Gradient Boosting Regressor"])
    with select_cols[3]:
        linea = st.selectbox('Linea', options=['Todas', 'Pintado 1', 'Pintado 2'])

    # Filter data based on the selected pintura and linea
    df_selected = df_top_pinturas.copy()
    if pintura != "Todas":
        df_selected = df_selected[df_selected["Pintura"] == pintura]
    if linea != 'Todas':
        df_selected = df_selected[df_selected["Linea"] == linea]

    # Initialize metrics
    mse_test,r2_test,explained_variance,x_mod,y_mod,y_test,y_test_pred,model,mape,scaler_x,scaler_y = None, None,None,None,None,None,None,None,None,None,None

    # Run the selected model
    if variable == 'Random Forest':
        mse_test,  r2_test,explained_variance,x_mod,y_mod,y_test,y_test_pred,model,mape= random_forest(df_selected, int(entrenamiento))
    elif variable=='Gradient Boosting Regressor':
        mse_test,r2_test,explained_variance,x_mod,y_mod,y_test,y_test_pred,model,mape,scaler_x,scaler_y=gradient_boosting(df_selected,int(entrenamiento))
   
    df_results = pd.DataFrame({'Actual': y_test,'Predicted': y_test_pred})
    # Second row: Graphs and Controls/Metrics
    main_cols = st.columns([4, 2])  # Adjust the ratio as needed
    with main_cols[0]:
        st.write("##### Predicción")
         
        # Create a scatter plot with a trendline using plotly.express
        fig1 = px.scatter(x=y_test, y=y_test_pred, labels={'x': 'Actual', 'y': 'Predicción'}, title='Actual vs Predicción', trendline='ols')

        # Extract the scatter and trendline data
        scatter = fig1.data[0]
        trendline = fig1.data[1]

        # Update the scatter points color
        scatter.update(marker=dict(color='#FFA500'))

        # Update the trendline style
        trendline.update(line=dict(color='black', dash='dot'))

        # Create the final figure
        final_fig = go.Figure(data=[scatter, trendline])

        # Update layout
        final_fig.update_layout(height=400, width=600, xaxis_title='Actual', yaxis_title='Predicción')

        # Plot the figure
        st.plotly_chart(final_fig)

        st.write("##### Predicción de un valor")
        submain_cols=st.columns(2)
        subsub_cols=st.columns([0.2, 1])
        with submain_cols[0]:
            with subsub_cols[0]:
                rendimiento_input = st.text_input("Rendimiento Std", "40")
            
                
                
                
            

            with subsub_cols[0]:
                area_input = st.text_input("Area", "200")
            with subsub_cols[1]:
                espesor_input= st.text_input("Espesor", "5")
        with submain_cols[1]:
            if variable== 'Random Forest':
                new_data_RF = [[int(rendimiento_input),  int(area_input), int(espesor_input)]]  # Example new input values for 'Espesor', 'Linea_encoded', 'Area', 'Litros Totales'
                prediction_RF = model.predict(new_data_RF)

                st.metric(label="Litros Totales", value=f"{round(prediction_RF[0],2)}")
            elif variable=='Gradient Boosting Regressor':
                new_data = np.array([[int(rendimiento_input),  int(area_input), int(espesor_input)]])  # Example new input values for 'Litros Totales', 'Valor USD', 'Area', 'Espesor'
                new_data_scaled = scaler_x.transform(new_data)
                prediction_scaled = model.predict(new_data_scaled)
                prediction = scaler_y.inverse_transform(prediction_scaled.reshape(-1, 1)).flatten()
                print(f"Prediction for new input values: {prediction[0]}")
                st.metric(label="Litros Totales", value=f"{round(prediction[0],2)}")

        
        




        
       

        # Plotting the predicted values versus time
       
    # Right side: Metrics in a 2x3 layout
    with main_cols[1]:
        st.write("##### Metricas")
        
        sub_cols = st.columns(3)
        with sub_cols[0]:
            st.metric(label="Explained variance", value=f'{explained_variance:.2f}'if explained_variance is not None else "N/A")
        with sub_cols[1]:
            st.metric(label="MAPE", value=f'{mape:.2f}%'if mape is not None else "N/A")
        with sub_cols[2]:
            st.metric(label="MSE", value=f"{mse_test:.2f}" if mse_test is not None else "N/A")
        sub_cols = st.columns(3)
        with sub_cols[0]:
            st.metric(label="R^2", value=f"{r2_test:.2f}" if r2_test is not None else "N/A")
        
        with sub_cols[1]:
            st.metric(label="# Registros", value=f'{df_selected.shape[0]}')
        
        st.write("### Prueba vs Predicción")
        
        st.dataframe(df_results.head(3))  # Adjust table width as needed

