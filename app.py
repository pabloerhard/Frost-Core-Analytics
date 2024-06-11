import streamlit as st
import base64
import Files.Introduccion as Introduccion
import Files.Limpieza as Limpieza
import Files.Tableros as Tableros
import Files.Conclusiones as Conclusiones
import Files.Tableros as Tableros
from Statics.Styles import styles as styles
import Files.TablerosModelos as TablerosModelos

def main():
    styles.apply_custom_css()
    def get_image_base64(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()

    # Get the base64 encoded string of the image
    image_path = "./Statics/Images/Ternium_Logo.png"
    image_base64 = get_image_base64(image_path)
    image_html = f"data:image/png;base64,{image_base64}"

    # Use the base64 string in the HTML
    st.markdown(
        f"""
        <div style='display: flex; justify-content: center;'>
            <img src='{image_html}' width='400'/>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <style>
        .st-emotion-cache-1gv3huu {
            background-image: linear-gradient(#FFA500,#FFA500);
            color: green;
        }
        .st-emotion-cache-12fmjuu {
            background-image: linear-gradient(#FF8C00,#FF8C00);
            color: green;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.markdown("<h2>🔍 Navegación</h2>", unsafe_allow_html=True)

    # Define the menu options with emojis
    menu_options = [
        "📝 Contexto Y Problematica", 
        "🧹 Limpieza de Datos", 
        "📊 Tableros", 
        "🎓 Conclusiones"
    ]

    # Add a radio button widget for navigation
    menu = st.sidebar.radio(
        "Ir a:", 
        menu_options,
        index=0
    )

    if menu == "📝 Contexto Y Problematica":
        Introduccion.main()

    elif menu == "🧹 Limpieza de Datos":
        Limpieza.main()

    elif menu == "📊 Tableros":
        Tableros.main()

    elif menu == "🎓 Conclusiones":
        Conclusiones.main()

if __name__ == "__main__":
    st.set_page_config(layout="wide")
    main()