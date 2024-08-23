class KBCGame:
    def __init__(self):
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
                "answer": "C"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
                "answer": "B"
            },
            {
                "question": "What is the largest mammal in the world?",
                "options": ["A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Rhinoceros"],
                "answer": "B"
            }
        ]
        self.score = 0
        self.current_question = 0

    def ask_question(self):
        if self.current_question < len(self.questions):
            q = self.questions[self.current_question]
            print(f"\nQuestion {self.current_question + 1}: {q['question']}")
            for option in q['options']:
                print(option)
            answer = input("Your answer (A, B, C, D): ").strip().upper()
            
            if answer == q['answer']:
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was {q['answer']}.")
                
            self.current_question += 1
        else:
            print("No more questions available.")

    def display_score(self):
        print(f"\nYour final score is: {self.score}/{len(self.questions)}")

    def play(self):
        print("Welcome to KBC - Kaun Banega Crorepati!")
        while self.current_question < len(self.questions):
            self.ask_question()
        self.display_score()
        print("Thank you for playing!")

if __name__ == "__main__":
    game = KBCGame()
    game.play()
