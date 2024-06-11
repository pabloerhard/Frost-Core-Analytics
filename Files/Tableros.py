import streamlit as st
import Files.TablerosModelos as TablerosModelos
import Files.TableroDescriptivo as TableroDescriptivo
def main():
    col1, col2 = st.columns(2);

    st.markdown("<h2 class='header2'>📊 Tablero de Monitoreo</h2>", unsafe_allow_html=True)
    TableroDescriptivo.main()
    st.markdown("<h2 class='header2'>🤖 Tablero de Modelos</h2>", unsafe_allow_html=True)
    TablerosModelos.main()

if __name__ == "__main__":
    main()