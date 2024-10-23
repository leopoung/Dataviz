import streamlit as st

#Page ---

about_page = st.Page(
    "views/aboutme.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
data_visualization_page = st.Page(
    "views/plotting.py",
    title="Data Visualization",
    icon=":material/monitoring:",
)


pg = st.navigation(
    {
        "Information": [about_page],
        "Projects": [data_visualization_page],
    }
)


st.logo("image/efrei.png", size= "large")
st.sidebar.markdown("Made by Léo Poung  \nEFREI M1 Data Engineering Student")    

pg.run()