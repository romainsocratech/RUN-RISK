import streamlit as st

st.set_page_config(page_title="RUN RISK", layout="wide")
st.title("RUN RISK – Cartographie des tensions structurelles")

def afficher_axe(titre, questions, recommandations):
    st.markdown("---")
    col_gauche, col_droite = st.columns([2,1])

    with col_gauche:
        st.subheader(titre)
        for question in questions:
            st.write(f"- {question}")

    with col_droite:
        st.markdown("**Recommandations associées :**")
        for reco in recommandations:
            st.write(f"- {reco}")


afficher_axe(
    "Axe 1 – Dépendance humaine & continuité",
    [
        "Si une personne clé est absente, le RUN est-il bloqué ?",
        "Le savoir est-il documenté et transmissible ?",
        "Un remplaçant peut-il être opérationnel rapidement ?"
    ],
    [
        "Réduction de la dépendance à une personne clé",
        "Binômage ciblé sur les composants critiques",
        "Documentation minimale et utile (runbooks)",
        "Cartographie des savoirs critiques"
    ]
)

afficher_axe(
    "Axe 2 – Organisation & pression RUN",
    [
        "Priorisation floue",
        "Pression organisationnelle permanente",
        "Fatigue des équipes RUN"
    ],
    [
        "Rituels RUN hebdomadaires",
        "Tableau des incidents récurrents",
        "Clarification des rôles exploitation/dev",
        "Interface claire exploitation ↔ développement"
    ]
)

afficher_axe(
    "Axe 3 – Changements & mise en production",
    [
        "Risque lors des mises en production",
        "Rollback non maîtrisé",
        "Stabilité insuffisante post-MEP"
    ],
    [
        "Rollback documenté et testé",
        "Freeze temporaire des MEP",
        "Check-list de mise en production",
        "Supervision renforcée post-MEP"
    ]
)

afficher_axe(
    "Axe 4 – Pilotage & gouvernance",
    [
        "Absence de pilotage structuré",
        "Manque de visibilité sur les priorités",
        "Absence de suivi des incidents récurrents"
    ],
    [
        "Priorisation stricte P1/P2/P3",
        "SLA clarifiés avec le métier",
        "Détection des signaux faibles",
        "Plan d'amélioration continue RUN"
    ]
)

afficher_axe(
    "Axe 5 – Sécurité & résilience",
    [
        "PRA absent ou non testé",
        "Sauvegardes non vérifiées régulièrement",
        "Dépendance à un environnement unique"
    ],
    [
        "PRA formalisé et testé",
        "Vérification régulière des sauvegardes",
        "Plan de bascule identifié",
        "Simulation annuelle de crise"
    ]
)

afficher_axe(
    "Axe 6 – Stabilité globale du RUN",
    [
        "Multiplication des incidents critiques",
        "Difficulté à absorber les changements",
        "Instabilité récurrente en production"
    ],
    [
        "Cellule RUN dédiée en période critique",
        "Réduction des changements non critiques",
        "Plan de réduction de dette technique",
        "Stabilisation avant toute évolution"
    ]
)

