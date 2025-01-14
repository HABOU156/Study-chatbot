from chatbot import StudyBot
import sys

def main():
    print("Bienvenue sur StudyBot ! Tapez 'quit' ou 'END' pour quitter, 'upload' pour ajouter un document.")
    bot = StudyBot()

    while bot.is_running:
        user_input = input("\nVous : ").strip()
        
        if user_input.lower() in ['quit', 'end']:
            bot.stop()
            print("Au revoir !")
            break
            
        elif user_input.lower() == 'upload':
            print("Entrez votre texte (tapez autre chose que 'END' pour terminer) :")
            text_lines = []
            while True:
                line = input()
                if line.strip().lower() == 'end':
                    bot.stop()
                    print("Au revoir !")
                    return
                text_lines.append(line)
            bot.set_context('\n'.join(text_lines))
            print("Document téléchargé avec succès !")
            
        else:
            answer = bot.get_answer(user_input)
            print(f"StudyBot : {answer}")

if __name__ == "__main__":
    main()
