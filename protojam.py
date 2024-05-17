import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Présentation quête
st.title('Analyse dataset :blue[DreamDestiny]✈️')

st.markdown("""
- Data Set récupéré sur la plateforme Kaggle.
""")

# Lecture du dataset
df = pd.read_parquet(r"table_voyage_all")

# Définir une taille de police et un style uniformes
plt.rcParams.update({'font.size': 10})

# Top 3 des destinations de voyages
genre = df["Country"].value_counts().head(3)
fig1, ax1 = plt.subplots()
ax1.bar(genre.index, genre.values, color='skyblue')
ax1.set_title('Top 3 des destinations de voyages', fontsize=14)
ax1.set_xlabel('Pays', fontsize=12)
ax1.set_ylabel('Nombre de voyages', fontsize=12)

# Top 3 des transports les plus utilisés
top_3_transports = df['Transportation type'].value_counts().head(3)
fig2, ax2 = plt.subplots()
ax2.bar(top_3_transports.index, top_3_transports.values, color='skyblue')
ax2.set_title('Top 3 des transports les plus utilisés', fontsize=14)
ax2.set_xlabel('Type de transport', fontsize=12)
ax2.set_ylabel('Nombre de voyages', fontsize=12)

# Moyenne d'âge des voyageurs par pays
avg_age_by_country = df.groupby('Country')['Traveler age'].mean()
fig3, ax3 = plt.subplots()
avg_age_by_country.plot(kind='bar', color='skyblue', ax=ax3)
ax3.set_title("Moyenne d'âge des voyageurs par pays", fontsize=14)
ax3.set_xlabel('Pays', fontsize=12)
ax3.set_ylabel('Âge moyen', fontsize=12)
ax3.set_xticklabels(avg_age_by_country.index, rotation=90)

# Coût moyen par pays
avg_cost_by_country = df.groupby('Country')['Total cost'].mean()
fig4, ax4 = plt.subplots()
avg_cost_by_country.plot(kind='bar', color='skyblue', ax=ax4)
ax4.set_title('Coût moyen par pays', fontsize=14)
ax4.set_xlabel('Pays', fontsize=12)
ax4.set_ylabel('Coût moyen (en $)', fontsize=12)
ax4.set_xticklabels(avg_cost_by_country.index, rotation=90)

# Top 3 des logements les plus utilisés
top_3_accommodations = df['Accommodation type'].value_counts().head(3)
fig5, ax5 = plt.subplots()
ax5.bar(top_3_accommodations.index, top_3_accommodations.values, color='skyblue')
ax5.set_title('Top 3 des logements les plus utilisés', fontsize=14)
ax5.set_xlabel('Type de logement', fontsize=12)
ax5.set_ylabel('Nombre de voyages', fontsize=12)

# Disposition des graphiques
col1, col2 = st.columns(2)

# Afficher les graphiques côte à côte
with col1:
    st.pyplot(fig1)
    st.pyplot(fig5)
    st.pyplot(fig3)

with col2:
    st.pyplot(fig2)
    st.pyplot(fig4)


# Présentation quête
st.markdown('## 😎 Conclusion 🏝️')

st.markdown("""
- Le data set a des données variées.
- Nous avons pu donc l'exploiter pour réaliser un proof of concept
""")
