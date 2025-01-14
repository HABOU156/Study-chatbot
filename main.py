from chatbot import StudyBot
import sys

def main():
    print("Bienvenue sur StudyBot ! Tapez 'quit' pour quitter, 'upload' pour ajouter un document.")
    bot = StudyBot()

    while True:
        user_input = input("\nVous : ").strip()
        
        if user_input.lower() == 'quit':
            # Quitter le programme
            print("Au revoir !")
            break
            
        elif user_input.lower() == 'upload':
            # Permettre à l'utilisateur d'ajouter un document en tant que contexte
            print("Entrez votre texte (tapez 'END' sur une nouvelle ligne pour terminer) :")
            text_lines = []
            while True:
                line = input()
                if line.strip() == 'END':
                    break
                text_lines.append(line)
            bot.set_context('\n'.join(text_lines))
            print("Document téléchargé avec succès !")
            
        else:
            # Obtenir une réponse à la question de l'utilisateur
            answer = bot.get_answer(user_input)
            print(f"StudyBot : {answer}")

if __name__ == "__main__":
    main()
