from pathlib import Path

def rechercher_fichiers_txt(dossier_racine):
    chemin = Path(dossier_racine)
    return list(chemin.rglob("*.txt"))


if __name__ == "__main__":
    dossier = input("Entrez le dossier à analyser (ex: C:\\ ou /) : ")

    print("Recherche en cours...\n")
    resultats = rechercher_fichiers_txt(dossier)

    print(f"\n{len(resultats)} fichier(s) .txt trouvé(s) :\n")
    for fichier in resultats:
        print(fichier)