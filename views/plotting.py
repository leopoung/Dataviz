import streamlit as st
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import json
import folium
from streamlit_folium import st_folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster
from folium import Choropleth



# Charger les données de vote depuis un fichier Excel

df = pd.read_excel('Dataset.xls', sheet_name = "Tour 1")
df1 = pd.read_excel('Dataset.xls', sheet_name = "Tour 2")

st.title("Étude des Résultats de l'Élection Présidentielle Française de 2012")

#COL 1---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Créer deux colonnes pour afficher les visualisations côte à côte
col1, col2 = st.columns(2)

# Première visualisation -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
with col1:
    st.subheader("Répartition des pourcentages de votes par candidat au premier tour")

    # Charger les données pour le premier tour
    df = pd.read_excel('Dataset.xls', sheet_name='Tour 1')

    # Extraire uniquement les colonnes des noms des candidats et des voix
    noms_candidats = df.iloc[0, [16, 22, 28, 34, 40, 46, 52, 58, 64, 70]]  # Colonnes des noms 
    voix_candidats = df.iloc[:, [18, 24, 30, 36, 42, 48, 54, 60, 66, 72]]  # Colonnes des voix

    # Total des voix pour chaque candidat
    total_voix_candidats = voix_candidats.sum()

    # Utiliser uniquement le nom des candidats pour les étiquettes
    noms_complets = noms_candidats.values

    # Calcul du pourcentage des voix pour chaque candidat
    total_voix_sum = total_voix_candidats.sum()
    pourcentages = (total_voix_candidats / total_voix_sum) * 100

    # Camembert
    plt.figure(figsize=(6, 6))
    plt.pie(pourcentages, labels=noms_complets, autopct='%1.1f%%', labeldistance=1.2)

    # Ajouter un titre
    plt.title('Résultat du premier tour')

    # Afficher le graphique avec Streamlit
    st.pyplot(plt)

# Deuxième visualisation -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
with col2:
    st.subheader("Répartition des pourcentages de votes par candidat au second tour")

    # Charger les données pour le deuxième tour
    df = pd.read_excel('Dataset.xls', sheet_name='Tour 2')

    # Extraire uniquement les colonnes des noms des candidats et des voix
    noms_candidats = df.iloc[0, [16, 22]]  # Colonnes des noms des candidats
    voix_candidats = df.iloc[:, [18, 24]]  # Colonnes des voix

    # Total des voix pour chaque candidat
    total_voix_candidats = voix_candidats.sum()

    # Utiliser uniquement le nom des candidats pour les étiquettes
    noms_complets = noms_candidats.values

    # Calcul du pourcentage des voix pour chaque candidat
    total_voix_sum = total_voix_candidats.sum()
    pourcentages = (total_voix_candidats / total_voix_sum) * 100

    # Camembert
    plt.figure(figsize=(6, 6))
    plt.pie(pourcentages, labels=noms_complets, autopct='%1.1f%%', labeldistance=1.2)

    # Ajouter un titre
    plt.title('Résultat du deuxième tour')

    # Afficher le graphique avec Streamlit
    st.pyplot(plt)

# COL2 -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
st.title("Comparaison des communes avec le plus de votants")

# Créer deux colonnes pour afficher les visualisations côte à côte
col1, col2 = st.columns(2)

# Troisième visualisation -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
with col1:
    st.subheader("Top 10 des communes ayant le plus voté")
    # Trier les départements en fonction du nombre de votes
    df_sorted = df.sort_values(by="Votants", ascending=False)

    # Sélectionner les 10 communes avec le plus grand nombre de votes
    top_10_departments = df_sorted.head(10)

    # Créer l'histogramme des 10 communes ayant le plus voté
    plt.figure(figsize=(5, 4))  
    plt.bar(top_10_departments["Libellé de la commune"], top_10_departments["Votants"], color='skyblue')
    plt.xlabel('Nom de la commune')
    plt.ylabel('Nombre de Votants')
    plt.yticks([0, 200000, 400000, 600000, 800000, 1000000], ['0', '200k', '400k', '600k', '800k', '1M'])
    plt.xticks(rotation=90)  
    plt.title('Top 10 des Communes ayant le plus voté')
    
    # Afficher l'histogramme 
    st.pyplot(plt)

# Quatrième visualisation------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
with col2:
    st.subheader("Top 10 des communes par pourcentage d'inscrit")
    # Trier les départements en fonction du pourcentage de vote par inscription dans les communes > 100 000 inscrits
    df_100000 = df[df["Inscrits"] > 100000]
    df_sorted = df_100000.sort_values(by="% Vot/Ins", ascending=False)

    # Sélectionner les 10 communes avec le plus grand nombre de votes par pourcentage
    top_10_VotIns = df_sorted.head(10)

    # Créer l'histogramme des 10 communes ayant le plus voté par pourcentage
    plt.figure(figsize=(5, 4))  
    plt.bar(top_10_VotIns["Libellé de la commune"], top_10_VotIns["% Vot/Ins"], color='skyblue')
    plt.xlabel('Nom de la commune')
    plt.ylabel('Pourcentage de votant par inscrit')
    plt.xticks(rotation=90) 
    plt.title("Top 10 des Communes par pourcentage d'inscrit")

    # Afficher l'histogramme 
    st.pyplot(plt)



#Cinquième visualisation ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
st.title("Comparaison des zones urbaines et rurales")

#On défini les communes au nombre d'inscrits supérieur à 100000 qu'on considère comme urbain
df_urbain = df[df["Inscrits"] > 100000]
#On défini les communes au nombre d'inscrits inférieur à 10000 qu'on considère comme rural
df_rural = df[df["Inscrits"] < 10000]

# Calcul des moyennes pour les votes communes urbaines
moyenne_urbain = df_urbain[["% Vot/Ins", "% BlNuls/Vot", "% Exp/Vot"]].mean()
#Calcul des moyennes pour les votes, communes rurales
moyenne_rural = df_rural[["% Vot/Ins", "% BlNuls/Vot", "% Exp/Vot"]].mean()

#Les 3 critères qu'on compare
labels = ['Participation', 'Blancs et Nuls', 'Votes Exprimés']

valeur_urbain = [moyenne_urbain["% Vot/Ins"], moyenne_urbain["% BlNuls/Vot"], moyenne_urbain["% Exp/Vot"]]
valeur_rural = [moyenne_rural["% Vot/Ins"], moyenne_rural["% BlNuls/Vot"], moyenne_rural["% Exp/Vot"]]

x = range(len(labels))

plt.figure(figsize=(12, 6))
plt.bar(x, valeur_urbain, width=0.4, label="Urbain", align="center", color="red")
plt.bar(x, valeur_rural, width=0.4, label="Rural", align="edge", color="green")
plt.xticks(x, labels)
plt.ylabel("Pourcentage")
plt.title("Comparaison entre zones urbaines et rurales")
plt.legend()

# Afficher l'histogramme 
st.pyplot(plt)


#Sixième visualisation ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

st.title("Relation entre taux de participation et voix exprimées")

# Charger les données électorales
df = pd.read_excel('Dataset.xls', sheet_name='Tour 1')

# Créer un scatter plot
plt.figure(figsize=(10, 6))

# Variables à tracer
x = df['% Vot/Ins']  # Taux de participation (pourcentage de votants par rapport aux inscrits)
y = df['Exprimés']  # Nombre de voix exprimées
sizes = df['Inscrits'] / 100  # Taille des points basée sur le nombre d'inscrits dans la commune

# Créer le scatter plot
plt.scatter(x, y, s=sizes, alpha=0.5, c='blue')

plt.ticklabel_format(style='plain', axis='y')


# Ajouter des labels et un titre
plt.xlabel('Taux de participation (%)')
plt.ylabel('Nombre de voix exprimées')
plt.title('Relation entre le taux de participation et les voix exprimées par commune')

# Afficher le scatter plot avec Streamlit
st.pyplot(plt)


#Septième visualisation -------------------------------------------------------------------------------------------------------------------------------------------

st.title("Carte interactive du taux d'abstention par département au premier tour")

df = pd.read_excel('Dataset.xls', sheet_name='Tour 1')

# Charger le fichier GeoJSON des départements français 
with open('departements-france.geojson') as f:
    geojson_departments = json.load(f)

# Extraire les colonnes de code des départements et de taux d'abstention
df['Taux_abstention'] = df['% Abs/Ins'] 
df = df[['Code du département', 'Taux_abstention']]

# Créer une carte centrée sur la France
map_france = folium.Map(location=[46.603354, 1.888334], zoom_start=6)

# Ajouter la carte Choropleth pour le taux d'abstention
Choropleth(
    geo_data=geojson_departments,
    data=df,
    columns=['Code du département', 'Taux_abstention'],  # Associer le code du département au taux d'abstention
    key_on='feature.properties.code',  # Identifier les départements dans le GeoJSON par le code département
    fill_color='Blues',  
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Taux d'abstention (%)"
).add_to(map_france)

# Afficher la carte
folium_static(map_france)

#Huitième visualisation-------------------------------------------------------------------------
st.title("Carte interactive du taux d'abstention par département au second tour")

df = pd.read_excel('Dataset.xls', sheet_name='Tour 2')

# Charger le fichier GeoJSON des départements français 
with open('departements-france.geojson') as f:
    geojson_departments = json.load(f)

# Extraire les colonnes de code des départements et de taux d'abstention
df['Taux_abstention'] = df['% Abs/Ins'] 
df = df[['Code du département', 'Taux_abstention']]

# Créer une carte centrée sur la France
map_france = folium.Map(location=[46.603354, 1.888334], zoom_start=6)

# Ajouter la carte Choropleth pour le taux d'abstention
Choropleth(
    geo_data=geojson_departments,
    data=df,
    columns=['Code du département', 'Taux_abstention'],  # Associer le code du département au taux d'abstention
    key_on='feature.properties.code',  # Identifier les départements dans le GeoJSON par le code département
    fill_color='Blues',  
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Taux d'abstention (%)"
).add_to(map_france)

# Afficher la carte
folium_static(map_france)

#Neuvième visualisation ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
st.title("Carte interactive des résultats électoraux par commune")

# Charger les données électorales
df = pd.read_excel('Dataset.xls', sheet_name='Tour 1')

# Charger les données de latitude et longitude des communes
df_geo = pd.read_csv('communes-departement-region.csv')

# Extraire les colonnes des voix des candidats
voix_candidats = df.iloc[:, [18, 24, 30, 36, 42, 48, 54, 60, 66, 72]]

# Extraire les colonnes des noms des candidats (ligne 0) et obtenir les noms 
noms_candidats = df.iloc[0, [16, 22, 28, 34, 40, 46, 52, 58, 64, 70]].values  # Obtenir les noms sous forme de tableau

# Déterminer le candidat ayant le plus de voix pour chaque commune
df['Candidat_majoritaire'] = voix_candidats.idxmax(axis=1)
df['Voix_max'] = voix_candidats.max(axis=1)

# Dataset des données électorales avec les coordonnées géographiques des communes
df_merged = pd.merge(df, df_geo, left_on='Libellé de la commune', right_on='nom_commune')

# On enlève les lignes où les coordonnées sont manquantes
df_merged = df_merged.dropna(subset=['latitude', 'longitude'])

# Créer une carte centrée sur la France
map_france = folium.Map(location=[46.603354, 1.888334], zoom_start=6)

# Ajouter les communes sur la carte avec un popup affichant le candidat gagnant et ses voix
for idx, row in df_merged.iterrows():
    # Extraire le numéro de la colonne du candidat gagnant
    colonne_majoritaire = row['Candidat_majoritaire']
    
    # Trouver l'indice de cette colonne dans voix_candidats et obtenir le nom correspondant
    indice_candidat = voix_candidats.columns.get_loc(colonne_majoritaire)
    candidat_gagnant = noms_candidats[indice_candidat]
    
    # Récupérer le nombre de voix du candidat gagnant
    voix_gagnant = row['Voix_max']
    
    # Ajouter un marqueur avec un popup affichant les informations
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=5,
        popup=f"Commune: {row['Libellé de la commune']}<br>Candidat gagnant: {candidat_gagnant}<br>Nombre de voix: {voix_gagnant}",
        color='blue',  # Couleur par défaut pour tous les marqueurs
        fill=True,
        fill_color='blue'
    ).add_to(map_france)

# Afficher la carte 
folium_static(map_france)