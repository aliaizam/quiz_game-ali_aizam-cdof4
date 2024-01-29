import random

# Définition des questions, avec les options de réponse et l'indice de la réponse correcte
questions = {
    "Quelle est la capitale de la France?": ["a) Londres", "b) Berlin", "c) Paris", "d) Rome", 2],
    "Qui a écrit 'Romeo et Juliette'?": ["a) Charles Dickens", "b) Jane Austen", "c) William Shakespeare", "d) Ernest Hemingway", 2],
    "Combien de continents y a-t-il sur Terre?": ["a) 5", "b) 6", "c) 7", "d) 8", 2]
}

def afficher_question(question, options):
    print(question)
    for option in options:
        print(option)
    reponse = input("Votre réponse (a, b, c, d) : ").strip().lower()
    return reponse

def jouer_quiz():
    print("Bienvenue dans le jeu de quiz !")
    score = 0
    questions_liste = list(questions.keys())
    random.shuffle(questions_liste)

    for question in questions_liste[:3]:  # Choisissez 3 questions aléatoires
        question_text = question
        options = questions[question_text][:-1]
        reponse_utilisateur = afficher_question(question_text, options)
        index_reponse_correcte = questions[question_text][-1]

        if reponse_utilisateur == 'a':
            reponse_index = 0
        elif reponse_utilisateur == 'b':
            reponse_index = 1
        elif reponse_utilisateur == 'c':
            reponse_index = 2
        elif reponse_utilisateur == 'd':
            reponse_index = 3
        else:
            print("Option invalide.")
            continue

        if reponse_index == index_reponse_correcte:
            print("Correct !")
            score += 1
        else:
            print(f"Faux. La réponse correcte est: {options[index_reponse_correcte]}")

    print(f"Vous avez obtenu {score} sur 3 questions correctes.")

if __name__ == "__main__":
    jouer_quiz()
