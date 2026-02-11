import streamlit as st

st.set_page_config(page_title="RUN-RISK", layout="wide")

st.title("RUN-RISK – Cartographie des tensions structurelles")

# ===============================
# DONNÉES
# ===============================

axes = {
    "Axe 1 – Dépendance humaine": {
        "questions": [
            "Si une personne clé est absente, le RUN est-il bloqué ?",
            "Le savoir est-il documenté et transmissible ?",
            "Un remplaçant peut-il être opérationnel rapidement ?"
        ],
        "reco": [
            "Réduction de la dépendance à une personne clé",
            "Binômage ciblé",
            "Documentation minimale utile",
            "Cartographie des savoirs critiques"
        ]
    },
    "Axe 2 – Organisation RUN": {
        "questions": [
            "Priorisation floue",
            "Pression organisationnelle permanente",
            "Fatigue des équipes RUN"
        ],
        "reco": [
            "Rituels RUN hebdomadaires",
            "Tableau incidents récurrents",
            "Clarification des rôles",
            "Interface exploitation ↔ dev"
        ]
    },
    "Axe 3 – Mise en production": {
        "questions": [
            "Risque lors des MEP",
            "Rollback non maîtrisé",
            "Instabilité post-MEP"
        ],
        "reco": [
            "Checklist MEP",
            "Rollback documenté",
            "Supervision 48h post-MEP",
            "Validation métier"
        ]
    },
    "Axe 4 – Pilotage": {
        "questions": [
            "Absence de pilotage structuré",
            "Manque de visibilité",
            "Suivi incidents absent"
        ],
        "reco": [
            "Priorisation P1/P2/P3",
            "SLA clarifiés",
            "Plan d'amélioration RUN",
            "Reporting synthétique"
        ]
    },
    "Axe 5 – Résilience": {
        "questions": [
            "PRA absent",
            "Sauvegardes non testées",
            "Risque de paralysie"
        ],
        "reco": [
            "Formaliser PRA",
            "Tester sauvegardes",
            "Définir RTO/RPO",
            "Simulation de crise"
        ]
    },
    "Axe 6 – Vision RUN": {
        "questions": [
            "Dette technique non priorisée",
            "Cartographie absente",
            "Roadmap inexistante"
        ],
        "reco": [
            "Cartographie applicative",
            "Roadmap 12 mois",
            "Plan 90 jours",
            "Objectiver risque global"
        ]
    }
}

# ===============================
# TABLEAU PRINCIPAL (reste fixe)
# ===============================

st.markdown("## Vue globale des axes")

for axe, data in axes.items():
    col_g, col_d = st.columns([2,1])

    with col_g:
        st.subheader(axe)
        q1 = st.slider(data["questions"][0], 0, 10, 5, key=axe+"q1")
        q2 = st.slider(data["questions"][1], 0, 10, 5, key=axe+"q2")
        q3 = st.slider(data["questions"][2], 0, 10, 5, key=axe+"q3")

    score = q1 + q2 + q3

    with col_d:
        st.markdown("Score")
        st.progress(score / 30)
        st.write(f"{score} / 30")

    st.markdown("---")


# ===============================
# LECTURE PROGRESSIVE EN DESSOUS
# ===============================

st.markdown("## Lecture progressive des recommandations")

if "axe_index" not in st.session_state:
    st.session_state.axe_index = 0

axes_list = list(axes.keys())
axe_selectionne = axes_list[st.session_state.axe_index]
data = axes[axe_selectionne]

st.markdown(f"### Axe analysé : {axe_selectionne}")

st.markdown("#### Recommandations associées")
for r in data["reco"]:
    st.write(f"- {r}")

col_prev, col_next = st.columns(2)

with col_prev:
    if st.button("⬅️ Axe précédent"):
        if st.session_state.axe_index > 0:
            st.session_state.axe_index -= 1

with col_next:
    if st.button("➡️ Axe suivant"):
        if st.session_state.axe_index < len(axes_list) - 1:
            st.session_state.axe_index += 1
