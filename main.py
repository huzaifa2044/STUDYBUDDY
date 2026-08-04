import os
from summarizer import summarize
from quiz_generator import generate_quiz
from flashcard_generator import generate_flashcards

notes_text = ""


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_title():
    print("=" * 40)
    print("           STUDY BUDDY")
    print("   Your Personal Study Assistant")
    print("=" * 40)


def show_menu():
    status = "Loaded" if notes_text != "" else "Not loaded"
    print(f"\nNotes status: {status}")
    print("-" * 40)
    print("1. Load/Enter Notes")
    print("2. View Notes Info")
    print("3. Generate Summary")
    print("4. Generate Quiz")
    print("5. Generate Flashcards")
    print("6. Exit")
    print("-" * 40)


def load_notes():
    global notes_text
    print("\nHow do you want to provide notes?")
    print("A. Type notes manually")
    print("B. Load from a file (notes/sample_notes.txt)")
    sub_choice = input("Enter A or B: ").strip().upper()

    if sub_choice == "A":
        notes_text = input("Type or paste your notes here: ")
        print("Notes saved successfully!")

    elif sub_choice == "B":
        try:
            with open("notes/sample_notes.txt", "r") as file:
                notes_text = file.read()
            print("Notes loaded successfully from file!")
        except FileNotFoundError:
            print("Error: File not found. Please check notes/sample_notes.txt exists.")

    else:
        print("Invalid option. Please choose A or B.")


def show_notes_info():
    words = notes_text.split()
    sentences = notes_text.split(".")
    print(f"\nWord count: {len(words)}")
    print(f"Sentence count: {len(sentences)}")


clear_screen()
show_title()

while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        load_notes()

    elif choice == "2":
        if notes_text == "":
            print("No notes found! Please load notes first (Option 1).")
        else:
            show_notes_info()

    elif choice == "3":
        if notes_text == "":
            print("No notes found! Please load notes first (Option 1).")
        else:
            summary = summarize(notes_text)
            print("\n----- SUMMARY -----")
            print(summary)

    elif choice == "4":
        if notes_text == "":
            print("No notes found! Please load notes first (Option 1).")
        else:
            quiz = generate_quiz(notes_text)
            if len(quiz) == 0:
                print("Not enough content to generate quiz questions.")
            else:
                score = 0
                print("\n----- QUIZ -----")
                for i in range(len(quiz)):
                    q = quiz[i]
                    print(f"\nQ{i + 1}: {q['question']}")
                    user_answer = input("Your answer: ").strip().lower()
                    correct_answer = q['answer'].strip().lower()
                    if user_answer == correct_answer:
                        print("Correct!")
                        score += 1
                    else:
                        print(f"Wrong. Correct answer: {q['answer']}")
                print(f"\nYour final score: {score}/{len(quiz)}")

    elif choice == "5":
        if notes_text == "":
            print("No notes found! Please load notes first (Option 1).")
        else:
            flashcards = generate_flashcards(notes_text)
            if len(flashcards) == 0:
                print("Not enough content to generate flashcards.")
            else:
                print("\n----- FLASHCARDS -----")
                for i in range(len(flashcards)):
                    card = flashcards[i]
                    print(f"\nCard {i + 1}")
                    print(f"Front: {card['front']}")
                    input("Press Enter to see the back...")
                    print(f"Back: {card['back']}")

    elif choice == "6":
        print("\nGoodbye! Thanks for using Study Buddy.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")