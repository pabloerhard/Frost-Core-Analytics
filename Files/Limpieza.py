import streamlit as st

def main():
    st.markdown("<h2 class='header'>Limpieza de Datos</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <p class='text'>
        Para llevar acabo un analizis de la manera mas eficaz se necesita llevar acabo una limpia de los datos. Por lo cual es importante entender con lo que nos enfretamos.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p class='text'>
        Se cuenta con 2 bases de datos principales
        </p>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            "<div class='container'><span class='text'><b>Revestidos</b></span></div>", 
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            "<div class='container'><span class='text'><b>Resumen Produccion</b></span></div>", 
            unsafe_allow_html=True
        )

    st.latex(r"\textcolor{black}{Rendimiento \, Diario = \dfrac{Metros \, Cuadrados}{Litros}}")

    container_pre_merge_content = "<span class='text'><b>Datos Pre Merge Revestidos:</b> 13,359</span>"
    container_after_merge_content = "<span class='text'><b>Datos Pre Merge Resumen Produccion:</b> 17,362 </span>"

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            f"<div class='container'>{container_pre_merge_content}</div>", 
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            f"<div class='container'>{container_after_merge_content}</div>", 
            unsafe_allow_html=True
        )
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        f"<div class='container'><span class='text'><b>Datos Post Merge:</b> 9897 </span</div>",
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        f"<div class='container'><span class='text'><b>Porcentaje de Datos Utilizados:</b> 57% </span</div>",
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        """
        <p class='text'>
        Una vez teniendo los datos preprocesados, se procede a realizar la limpieza de los mismos.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Proceso de Estandarizacion de Datos")
    st.latex(r"\textcolor{black}{Z = \dfrac{X - \mu}{\sigma}}")
    st.write("""
    #### Explicación:

    1. **\( X \)**: Tu número original.
    2. **\( \mu \)**: El promedio de todos los datos.
    3. **\( \sigma \)**: Qué tan dispersos están los números (desviación estándar).

    """)
    st.markdown('<br>', unsafe_allow_html=True)
    st.subheader("Proceso de Manejo de Atipicos (Winsorización)")
    st.latex(r"""
    \textcolor{black}{
    X_w = 
    \begin{cases} 
    \text{Límite Inferior} & \text{si } X < \text{Límite Inferior} \\
    X & \text{si } \text{Límite Inferior} \leq X \leq \text{Límite Superior} \\
    \text{Límite Superior} & \text{si } X > \text{Límite Superior}
    \end{cases}
    }
    """)

    st.write("""
    #### Explicación:

    La técnica de Winsorization se utiliza para manejar valores atípicos en los datos. Aquí tienes una explicación sencilla paso a paso:

    1. **\( X \)**: Tu número original.
    2. **Límite Inferior y Límite Superior**: Estos son los valores más bajos y más altos permitidos en tus datos después de aplicar Winsorization.

    #### Pasos:

    - Si \( X \) es menor que el Límite Inferior, reemplaza \( X \) con el Límite Inferior.
    - Si \( X \) está entre el Límite Inferior y el Límite Superior, deja \( X \) sin cambios.
    - Si \( X \) es mayor que el Límite Superior, reemplaza \( X \) con el Límite Superior.

    Este proceso ayuda a mantener tus datos dentro de ciertos límites, eliminando valores extremadamente altos o bajos que podrían afectar tus análisis.
    """)

    st.markdown(
        f"<div class='container'><span class='text'><b>Porcentaje de Datos Impactados:</b> 10% </span</div>",
        unsafe_allow_html=True
    )



if __name__ == "__main__":
    main()