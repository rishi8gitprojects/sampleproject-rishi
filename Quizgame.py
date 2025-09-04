import json
import random
import os
os.chdir(r"C:\Users\Rishi Roychowdhury\Documents\Python Course\Python Projects\sampleproject-rishi")
class QustionAnswer:
    def __init__(self):
        pass
    
    def get_question(self):
    
        with open("questions.json", "r") as f:
            products = json.load(f)
        q = random.choice(products)
        return q
    def main(self):
        loss = 0
        q = self.get_question()
        question = q["question"]
        option = q["options"]
        answer = q["answer"]
        print("Do you want to play(Yes, No)")
        command = input(">").lower()
        score = 0
        for i in range(5):
            if command == "no":
                print("Okay have a great day!!")
                break
            elif command == "yes":
                q = self.get_question()
                question = q["question"]
                option = q["options"]
                answer = q["answer"]

                print("Okay then, Lets begin")
                print(question)
                print(option)

                cmd = input("> ").lower()

                if cmd == answer.lower():
                    print("congratulation")
                    score += 1
                else:
                    print(f"Wrong answer, right answer is {answer}")
                    print(f"Your score is {score}")
                    break

begin = QustionAnswer()
begin.main()
