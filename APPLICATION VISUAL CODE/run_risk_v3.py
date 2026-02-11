import streamlit as st

st.set_page_config(layout="wide")

st.title("RUN RISK")


col_gauche, col_droite = st.columns([1,1])

# ===================== COLONNE GAUCHE =====================

with col_gauche:

    st.markdown("## Cartographie des incidents")

    st.markdown("### Axe 1 – Dépendance humaine")
    st.write("- Concentration du savoir sur une personne clé")
    st.write("- Absence de back-up opérationnel")
    st.write("- Documentation insuffisante")
    st.write("- Savoir tribal non formalisé")
    st.write("- Onboarding long")
    st.write("- Stress lors des absences")

    st.markdown("### Axe 2 – Incidents & stabilité RUN")
    st.write("- Incidents critiques fréquents")
    st.write("- Incidents récurrents non traités")
    st.write("- Causes racines non analysées")
    st.write("- Priorisation floue")
    st.write("- RUN subi plutôt que piloté")
    st.write("- Multiplication des correctifs urgents")

    st.markdown("### Axe 3 – Mise en production")
    st.write("- Stress lors des MEP")
    st.write("- Rollback non maîtrisé")
    st.write("- Absence de checklist MEP")
    st.write("- Instabilité post-déploiement")
    st.write("- Environnement de test fragile")
    st.write("- Changements simultanés risqués")

    st.markdown("### Axe 4 – Sécurité & résilience")
    st.write("- PRA absent ou non testé")
    st.write("- Sauvegardes non vérifiées")
    st.write("- RTO/RPO non définis")
    st.write("- Dépendance à un environnement unique")
    st.write("- Accès non contrôlés")
    st.write("- Risque de paralysie en cas de panne")

    st.markdown("### Axe 5 – Gouvernance & pilotage")
    st.write("- Absence de COPIL RUN structuré")
    st.write("- KPI RUN inexistants")
    st.write("- Arbitrages informels")
    st.write("- SLA non suivis")
    st.write("- Décisions tardives")
    st.write("- Manque de visibilité stratégique")

    st.markdown("### Axe 6 – Vision & dette structurelle")
    st.write("- Absence de cartographie applicative")
    st.write("- Flux critiques non identifiés")
    st.write("- Dette technique non priorisée")
    st.write("- Roadmap RUN inexistante")
    st.write("- Tensions organisationnelles invisibles")
    st.write("- Risque global non objectivé")


# ===================== COLONNE DROITE =====================

with col_droite:

    st.markdown("## Recommandations")

    st.markdown("### Axe 1")
    st.write("- Identifier les compétences critiques")
    st.write("- Mettre en place un binômage structuré")
    st.write("- Formaliser les procédures vitales")
    st.write("- Créer un référentiel documentaire unique")
    st.write("- Organiser des transferts de compétences")
    st.write("- Structurer un parcours d’onboarding")
    st.write("- Cartographier les dépendances humaines")
    st.write("- Sécuriser les connaissances critiques")

    st.markdown("### Axe 2")
    st.write("- Classifier les incidents P1/P2/P3")
    st.write("- Mettre en place un tableau de suivi RUN")
    st.write("- Traiter les causes racines")
    st.write("- Mettre en place un rituel RUN hebdomadaire")
    st.write("- Stabiliser avant évolution")
    st.write("- Suivre le temps moyen de résolution")
    st.write("- Réduire les incidents récurrents")
    st.write("- Prioriser 3 correctifs majeurs")

    st.markdown("### Axe 3")
    st.write("- Créer une checklist de mise en production")
    st.write("- Documenter les procédures de rollback")
    st.write("- Tester les plans de retour arrière")
    st.write("- Clarifier les responsabilités post-MEP")
    st.write("- Superviser 48h après MEP")
    st.write("- Geler les évolutions en période critique")
    st.write("- Réduire les changements simultanés")
    st.write("- Valider métier avant déploiement")

    st.markdown("### Axe 4")
    st.write("- Formaliser un PRA réaliste")
    st.write("- Tester régulièrement les sauvegardes")
    st.write("- Définir des RTO/RPO adaptés")
    st.write("- Auditer les droits d’accès")
    st.write("- Mettre en place un PCA simplifié")
    st.write("- Identifier les points de bascule critiques")
    st.write("- Simuler un scénario de crise")
    st.write("- Sécuriser les environnements sensibles")

    st.markdown("### Axe 5")
    st.write("- Instaurer un COPIL RUN mensuel")
    st.write("- Définir des KPI RUN simples")
    st.write("- Formaliser les arbitrages")
    st.write("- Clarifier le rôle MOA / MOE")
    st.write("- Mettre en place un reporting synthétique")
    st.write("- Aligner RUN & enjeux métier")
    st.write("- Objectiver les tensions structurelles")
    st.write("- Prioriser les actions correctives")

    st.markdown("### Axe 6")
    st.write("- Cartographier les flux applicatifs critiques")
    st.write("- Identifier la dette technique prioritaire")
    st.write("- Mettre en place une roadmap RUN à 12 mois")
    st.write("- Formaliser un plan d’actions 90 jours")
    st.write("- Objectiver le risque global RUN")
    st.write("- Identifier les fragilités organisationnelles")
    st.write("- Sécuriser les systèmes legacy critiques")
    st.write("- Réduire la dépendance aux environnements obsolètes")
