import streamlit as st

def apply_custom_css():
    st.markdown(
        """
        <style>
        .main {
            background-color: #d1d1cf; /* Fondo gris */
        }
        .title {
            color: #FF5733;
            text-align: center;
            font-size: 3em;
            margin-bottom: 0.5em;F
        }
        .header {
            color: #3b3b3b;
            text-align: center;
            font-size: 2em;
            margin-top: 1em;F
            margin-bottom: 0.5em;
        }
        .header2 {
            font-size: 24px;
            font-weight: bold;
            color: #333; /* Dark text color */
            margin-bottom: 12px; /* Add space below the header */
        }
        .text ul {
            margin-left: 24px; /* Indent the list */
        }
        .text {
            text-align: justify;
            font-size: 1.2em;
            color: #636363;
        }
        .text-area {
            width: 100%;
            margin: 1em 0;
        }
        .sidebar-content {
            background-color: #ff9903 !important;
        }
        .container {
            border: 1px solid black;
            text-align: center;
            padding: 10px;
            background-color: white;
            border-radius: 15px;
        }
        .text {
            font-size: 18px;
            color: #333;
        }
        .text b {
            color: #FF8C00; /* Primary color for emphasis */
        }
        .arrow {
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100%;
        }
        .arrow div {
            border-top: 3px solid #333;
            border-right: 3px solid #333;
            width: 40px;
            height: 40px;
            transform: rotate(45deg);
        }
        .container:hover .text b {
            color: #A0522D; /* Darker shade on hover */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
