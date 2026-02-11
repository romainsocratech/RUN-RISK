# =====================================
# RUN RISK SNAPSHOT – V2 ALIGNÉE MVP
# =====================================

from dataclasses import dataclass
from typing import List

# -----------------------------
# Modèle de risque
# -----------------------------
@dataclass
class Risk:
    name: str
    score: int  # 0 à 3

# -----------------------------
# Référentiel RUN (figé)
# -----------------------------
RISKS = [
    "Dépendance humaine",
    "Instabilité du RUN",
    "Mises en production à risque",
    "Savoir non sécurisé",
    "Pilotage RUN"
]

# -----------------------------
# Saisie des scores
# -----------------------------
def assess_risks() -> List[Risk]:
    risks = []
    print("\nÉvaluer les risques RUN (0 = maîtrisé | 3 = critique)\n")

    for name in RISKS:
        while True:
            try:
                score = int(input(f"{name} : "))
                if 0 <= score <= 3:
                    risks.append(Risk(name, score))
                    break
            except ValueError:
                pass
            print("Score invalide (0 à 3).")

    return risks

# -----------------------------
# Calcul global
# -----------------------------
def global_score(risks: List[Risk]) -> int:
    return sum(r.score for r in risks)

def decision(score: int) -> str:
    if score <= 5:
        return "RUN maîtrisé – surveillance standard"
    elif score <= 10:
        return "RUN sous tension – actions correctives ciblées"
    else:
        return "RUN critique – sécurisation immédiate requise"

def recommended_actions(score: int) -> List[str]:
    if score <= 5:
        return [
            "Maintenir le cadre RUN existant",
            "Poursuivre la surveillance"
        ]
    elif score <= 10:
        return [
            "Identifier les points de fragilité",
            "Lancer des actions correctives prioritaires"
        ]
    else:
        return [
            "Mise en place d’une cellule de pilotage RUN",
            "Sécurisation immédiate du fonctionnement",
            "Réduction des dépendances critiques"
        ]

# -----------------------------
# Restitution
# -----------------------------
def summary(risks: List[Risk]):
    score = global_score(risks)
    max_score = len(risks) * 3
    percent = int((score / max_score) * 100)

    print("\n===== RUN RISK SNAPSHOT =====")
    for r in risks:
        print(f"- {r.name} : {r.score}/3")

    print("-----------------------------")
    print(f"Score global : {score} / {max_score}")
    print(f"Niveau       : {percent} %")
    print(f"Décision     : {decision(score)}")
    print("\nActions recommandées :")
    for a in recommended_actions(score):
        print(f"- {a}")
    print("=============================")

# -----------------------------
# Main
# -----------------------------
if __name__ == "__main__":
    risks = assess_risks()
    summary(risks)
