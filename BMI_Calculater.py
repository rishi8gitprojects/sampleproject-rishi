import re
class BMI():
    def __init__(self):
        self.height = None

    def height_update(self, word):
        numbers = re.findall(r"\d+\.?\d*", word)
        if not numbers:
            raise ValueError("No number found in input.")

        value = float(numbers[0])
        if "cm" in word.lower():
            self.height = value / 100
        elif "m" in word.lower():
            self.height = value
        else:
            raise ValueError("Please specify height in cm or m")
        
    def calculate_bmi(self, weight):
        bmi = weight/self.height
        return round(bmi, 2)


print("\nWelcome to measuring you BMI. \nLet's begin")
weight = float(input("Your weight => "))
print("please provide(cm/feet/meter)")
height = input("Your height => ")
bmi = BMI()
bmi.height_update(height)
print(f"YOUR BMI: {bmi.calculate_bmi(weight)}")
