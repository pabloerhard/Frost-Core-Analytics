import streamlit as st

def main():
    st.markdown("<h2 class='header'>Contexto Y Problematica</h2>", unsafe_allow_html=True)
    st.subheader("Contexto")
    st.markdown(
        """
        <p class='text'>
        Ternium cuenta con un proceso de Revestido de Metales el cual han estado recopilando datos relacionados a este para tener un mejor entendimiento del proceso        
        </p> <br>
        <p class='text'>
        Para mejorar el entendimiento de la problemática es importante entender la magnitud de los procesos de Revestidos.
        </p>
        """,
        unsafe_allow_html=True
    )
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(
            "<div class='container'><span class='text'><b>Litros Totales: </b> 6,512,483 </span></div>", 
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            "<div class='container'><span class='text'><b>Metros Cuadrados: </b>324,332,333</span></div>", 
            unsafe_allow_html=True
        )
    with col3:
        st.markdown(
            "<div class='container'><span class='text'><b>Valor USD: </b> 57,651,970 </span></div>", 
            unsafe_allow_html=True
        )
    with col4:
        st.markdown(
            "<div class='container'><span class='text'><b>Rendimiento General: </b> 49.80 </span></div>", 
            unsafe_allow_html=True
        )

    
    st.subheader("Problemática")
    st.markdown(
        """
        <p class='text'>
        </p>
        <p class='text'>
        Teniendo la magnitud en cuenta es mas facil entender la importancia de tener un proceso estandarizado y sin desperdicio.
        <br>
        </p>

        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            "<div class='container'><span class='text'><b>Eficiencia de Proceso: </b> 99% </span></div>", 
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
        """
        <div style='display: flex; align-items: center; justify-content: center; height: 100%;'>
            <div style='border-top: 2px solid black; border-right: 2px solid black; width: 30px; height: 30px; transform: rotate(45deg);'></div>
        </div>
        """,
        unsafe_allow_html=True
        )
    with col3:
        st.markdown(
            "<div class='container'><span class='text'><b>Perdida USD: </b> 570,651 </span></div>", 
            unsafe_allow_html=True
        )
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            "<div class='container'><span class='text'><b>Eficiencia de Proceso: </b> 95% </span></div>", 
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
        """
        <div style='display: flex; align-items: center; justify-content: center; height: 100%;'>
            <div style='border-top: 2px solid black; border-right: 2px solid black; width: 30px; height: 30px; transform: rotate(45deg);'></div>
        </div>
        """,
        unsafe_allow_html=True
        )
    with col3:
        st.markdown(
            "<div class='container'><span class='text'><b>Perdida USD: </b> 2,853,255 </span></div>", 
            unsafe_allow_html=True
        )
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            "<div class='container'><span class='text'><b>Eficiencia de Proceso: </b> 90% </span></div>", 
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
        """
        <div style='display: flex; align-items: center; justify-content: center; height: 100%;'>
            <div style='border-top: 2px solid black; border-right: 2px solid black; width: 30px; height: 30px; transform: rotate(45deg);'></div>
        </div>
        """,
        unsafe_allow_html=True
        )
    with col3:
        st.markdown(
            "<div class='container'><span class='text'><b>Perdida USD: </b>5,706,510 </span></div>", 
            unsafe_allow_html=True
        )

    st.markdown(
    """
    <br>
    <p class='text'>
    La comparación de estos datos muestra claramente cómo pequeñas variaciones en la eficiencia del proceso pueden resultar en enormes diferencias en las pérdidas económicas. Esto subraya la necesidad crítica de optimizar los procesos y minimizar el desperdicio para mantener la competitividad y sostenibilidad de la operación.
    </p>
    """,
    unsafe_allow_html=True
    )
if __name__ == "__main__":
    main()
