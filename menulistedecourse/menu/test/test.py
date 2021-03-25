chemin = r'C:\Users\piedf\OneDrive\Bureau\developpement_web\python\Liste_de_courses\Menu\test\recette.txt'

with open(chemin, "r") as f:
    contenu = f.read()
    print(contenu)

if contenu != 'recette : ':
    print(contenu)
else:
    print("fin") 


