import streamlit as st

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.title("Poung Léo", anchor=False)
    st.write(
        "EFREI M1 Data Engineering Student  \nPromo 2026"
    )
with col2:
    st.image('image/profil.jpg')

st.write("\n")
st.write("My name is Léo, and I am currently a Master 1 student at EFREI Paris, majoring in Data Engineering. Throughout my academic journey, I have developed a strong foundation in programming, data analysis, and database management. I have worked with tools such as Python, SQL, and Power BI, as well as frameworks like Spark and Kafka, giving me hands-on experience in big data projects.")


st.write("\n")
st.subheader("Skills")
st.write(
    """
    - Programming: Python (Pandas)
                   HTML
                   C languages
                   Java (Object-Oriented Programming)
                   HTML
    - Data Analytics: Power Bi   
    - Databases: MongoDB, MySQL
    """
)


st.write("\n")
st.subheader("Soft Skills")
st.write(
    """
    - Adaptability
    - Communication
    - Teamwork
    - Stress management
    """
)


st.write("\n")
st.subheader("My Link")


# Affichage du texte "logo GitHub" et d'une image cliquable
st.write("""
<p>GitHub : <a href="https://github.com/leopoung" style="float:center">
    <img src="https://w7.pngwing.com/pngs/115/663/png-transparent-github-computer-icons-directory-github-mammal-cat-like-mammal-carnivoran.png" width="22px" style="vertical-align:middle">
    </img>
</a></p>
""", unsafe_allow_html=True)


st.write("""
<p>LinkedIn : 
    <a href="https://www.linkedin.com/in/l%C3%A9o-poung-a1881a222/" style="float:center">
        <img src="https://img.freepik.com/vecteurs-premium/icone-du-logo-du-cercle-vectoriel-linkedin_534308-21668.jpg?w=740" width="40px" style="vertical-align:middle">
        </img>
    </a>
</p>
""", unsafe_allow_html=True)
