import streamlit as st

def main():
    st.markdown("<h2 class='header2'>🔍 Hallazgos Importantes</h2>", unsafe_allow_html=True)
    st.markdown("""
        <p class='text'>
            <ul>
                <li>Se perdio e impacto un total de los <b> 47.3% </b> de los datos.</li>
                <li>Los modelos mejoran significativamente cuando una pintura tiene mas registros estables. </li>
                <li>La calidad de los datos entre la linea 1 y la linea 2 es muy diferente. </li>
            </ul>
        </p>  
        """,
        unsafe_allow_html=True)
    
    st.markdown("<h2 class='header2'>👍 Recomendaciones</h2>", unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.markdown(
            "<div class='container'><span class='text'> Enfatizar la importancia de la eficiencia de los procesos y reducir el desperdicio de pintura. </span></div>", 
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
        """
        <div style='display: flex; align-items: center; justify-content: center; height: 100%;'>
            <div style='border-top: 2px solid black; border-right: 2px solid black; width: 30px; height: 30px; transform: rotate(45deg);  margin-top: 15px;'></div>
        </div>
        """,
        unsafe_allow_html=True
        )
    with col3:
        st.markdown(
            "<div class='container' ><span class='text'> Estandarizar el proceso de Ingestión de datos entre la Línea 1 y la Línea 2. </span></div>", 
            unsafe_allow_html=True
        )
    with col4:
        st.markdown(
        """
        <div style='display: flex; align-items: center; justify-content: center; height: 100%;'>
            <div style='border-top: 2px solid black; border-right: 2px solid black; width: 30px; height: 30px; transform: rotate(45deg);  margin-top: 15px'></div>
        </div>
        """,
        unsafe_allow_html=True
        )
    with col5:
        st.markdown(
            "<div class='container'><span class='text'> Recaudar un histórico de datos mas amplio. </span></div>", 
            unsafe_allow_html=True
        )
        st.markdown(
        """
        <div style='display: flex; align-items: center; justify-content: center; height: 100%;'>
            <div style='border-top: 2px solid black; border-right: 2px solid black; width: 30px; height: 30px; transform: rotate(135deg);  margin-top: 15px'></div>
        </div>
        """,
        unsafe_allow_html=True
        )
        st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col5:
        st.markdown(
            "<div class='container'><span class='text'> Correr los modelos en base a este nuevo historico. </span></div>", 
            unsafe_allow_html=True
        )
    with col4:
        st.markdown(
        """
        <div style='display: flex; align-items: center; justify-content: center; height: 100%;'>
            <div style='border-top: 2px solid black; border-right: 2px solid black; width: 30px; height: 30px; transform: rotate(-135deg);  margin-top: 15px'></div>
        </div>
        """,
        unsafe_allow_html=True
        )
    with col3:
        st.markdown(
            "<div class='container'><span class='text'> Si es necesario predecir un consumo usar los modelos ya existentes. </span></div>", 
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
        """
        <div style='display: flex; align-items: center; justify-content: center; height: 100%;'>
            <div style='border-top: 2px solid black; border-right: 2px solid black; width: 30px; height: 30px; transform: rotate(-135deg);  margin-top: 15px'></div>
        </div>
        """,
        unsafe_allow_html=True
        )
    with col1:
        st.markdown(
            "<div class='container'><span class='text'> Incluir modelos de series de tiempo a la ecuacion. </span></div>", 
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()