print("RUN-RISK")
print("========================================")
print("RUN-RISK – AIDE À LA DÉCISION RUN")
print("========================================\n")

print("Évaluez les risques suivants sur une échelle de 0 à 3 :")
print("0 = Aucun risque | 1 = Faible | 2 = Moyen | 3 = Critique\n")

r1 = int(input("1. Dépendance à une personne clé (absence bloquante pour l’activité) : "))
r2 = int(input("2. Fréquence et gravité des incidents impactant la production : "))
r3 = int(input("3. Risque de rupture lors des mises en production : "))
r4 = int(input("4. Niveau de formalisation et de partage du savoir : "))
r5 = int(input("5. Pression organisationnelle et capacité à absorber les urgences : "))

score = r1 + r2 + r3 + r4 + r5
pourcentage = (score / 15) * 100

print("\n----------------------------------------")
print(f"Indice de criticité RUN : {score} / 15")
print(f"Niveau de risque : {pourcentage:.0f} %")
print("Plus l’indice est élevé, plus le niveau de risque est important.")
print("----------------------------------------\n")

print("Diagnostic et actions recommandées :\n")

if score >= 10:
    print("RUN CRITIQUE – situation nécessitant une action immédiate\n")
    print("- Mise en place d’une cellule de pilotage RUN")
    print("- Sécurisation immédiate des compétences critiques")
    print("- Gel des changements non essentiels")
    print("- Priorisation stricte des incidents majeurs")

elif score >= 5:
    print("RUN FRAGILE – situation présentant un risque à court terme\n")
    print("- Identification des fragilités prioritaires")
    print("- Plan d’actions ciblé sur 30 jours")
    print("- Réduction de la dépendance aux personnes clés")
    print("- Amélioration minimale de la documentation")

else:
    print("RUN STABLE – situation maîtrisée sous réserve de vigilance\n")
    print("- Maintien des dispositifs actuels")
    print("- Surveillance des signaux faibles")
    print("- Capitalisation et documentation des pratiques")
    print("- Anticipation des risques futurs")

print("\n========================================")
print("Fin de l’évaluation RUN-RISK")
print("========================================")

3