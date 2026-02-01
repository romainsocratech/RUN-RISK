import streamlit as st

st.set_page_config(page_title="RUN Risk – Aide à la décision", layout="wide")

st.title("RUN Risk – Outil d’aide à la décision")
st.caption("Destiné au pilotage RUN / responsables applicatifs / chefs de projet / COPIL")

st.markdown("---")

st.subheader("Évaluation des risques RUN (0 = faible · 3 = critique)")

# === QUESTIONS (18) ===
questions = {
    "Dépendance humaine": [
        "Dépendance à une personne clé",
        "Absence de back-up de compétences",
        "Documentation insuffisante"
    ],
    "Stabilité RUN": [
        "Fréquence des incidents",
        "Gravité des incidents",
        "Capacité de résolution rapide"
    ],
    "Changements & MEP": [
        "Risque lors des mises en production",
        "Rollback non maîtrisé",
        "Tests insuffisants avant MEP"
    ],
    "Organisation": [
        "Priorisation des incidents floue",
        "Pression organisationnelle permanente",
        "Fatigue des équipes RUN"
    ],
    "Gouvernance": [
        "Rôles et responsabilités peu clairs",
        "Décisions lentes ou bloquées",
        "Manque de pilotage RUN"
    ],
    "Sécurité & Continuité": [
        "PRA insuffisant ou absent",
        "Sécurité applicative faible",
        "Manque de supervision / alerting"
    ]
}

scores = {}
total_score = 0
max_score = 18 * 3

# === UI ===
col1, col2 = st.columns([2, 1])

with col1:
    for axe, qs in questions.items():
        st.markdown(f"### {axe}")
        axe_score = 0
        for q in qs:
            val = st.slider(q, 0, 3, 1)
            axe_score += val
            total_score += val
        scores[axe] = axe_score
        st.markdown("---")

with col2:
    st.markdown("## Synthèse RUN")
    pourcentage = round((total_score / max_score) * 100, 1)

    st.metric("Score global RUN", f"{total_score} / {max_score}")
    st.metric("Criticité (%)", f"{pourcentage} %")

    if pourcentage < 33:
        niveau = "🟢 RUN maîtrisé"
        message = "Situation stable. Surveillance et amélioration continue."
    elif pourcentage < 66:
        niveau = "🟠 RUN sous tension"
        message = "Risque significatif. Actions correctives à engager."
    else:
        niveau = "🔴 RUN critique"
        message = "Risque élevé. Pilotage renforcé et décisions immédiates requises."

    st.markdown(f"### {niveau}")
    st.markdown("## Actions proposées")

if criticite < 30:
    st.success("RUN maîtrisé – aucune action prioritaire requise.")
elif criticite < 60:
    st.warning("Risque modéré – recommandations ciblées à prévoir.")
    st.markdown("- Renforcer la documentation")
    st.markdown("- Sécuriser les mises en production")
else:
    st.error("Risque élevé – actions prioritaires immédiates.")
    st.markdown("- Mettre en place une cellule de pilotage RUN")
    st.markdown("- Réduire la dépendance humaine")
    st.markdown("- Formaliser rollback et PRA")

    st.write(message)

    st.markdown("---")
    st.subheader("Lecture par axe")
    for axe, score in scores.items():
        st.progress(score / 9)
        st.write(f"{axe} : {score} / 9")




