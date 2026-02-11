import streamlit as st

st.set_page_config(page_title="RUN Risk", layout="wide")

st.title("RUN Risk – Outil d’aide à la décision")

col1, col2 = st.columns(2)

with col1:
    axe1 = st.slider("Dépendance humaine", 0, 3, 0)
    axe2 = st.slider("Stabilité incidents", 0, 3, 0)
    axe3 = st.slider("Clarté des rôles RUN", 0, 3, 0)

with col2:
    axe4 = st.slider("Sécurité & PRA", 0, 3, 0)
    axe5 = st.slider("Documentation critique", 0, 3, 0)
    axe6 = st.slider("Maîtrise des mises en production", 0, 3, 0)

score = axe1 + axe2 + axe3 + axe4 + axe5 + axe6
max_score = 18

st.divider()
st.subheader("Synthèse")
st.write(f"Score global : {score} / {max_score}")

if score <= 5:
    st.success("RUN maîtrisé – aucune action prioritaire requise.")
elif score <= 12:
    st.warning("RUN sous tension – sécurisation recommandée.")
else:
    st.error("RUN critique – plan de stabilisation immédiat recommandé.")

st.divider()
st.caption("Contact : romainbrubach@socratec.fr")

