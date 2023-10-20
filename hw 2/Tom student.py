import random

class Student:
    def __init__(self, name, age, money=0, study=100):
        self.name = name
        self.age = age
        self.money = money
        self.study = study

    def earn_money(self, amount):
        self.money += amount
        print(f"{self.name} earned {amount} money.")

    def spend_money(self, amount):
        if self.money >= amount:
            self.money -= amount
            print(f"{self.name} spent {amount} money.")
        else:
            print(f"{self.name} doesn't have enough money to spend {amount} money.")

    def study_more(self, hours):
        self.study += hours
        print(f"{self.name} studied for {hours} hours.")

    def solve_problem(self, problem):
        if random.random() < 0.5:
            print(f"{self.name} couldn't solve the problem: {problem}")
            self.earn_money(50)
        else:
            print(f"{self.name} successfully solved the problem: {problem}")

    def relax(self, hours):
        expenses = hours * 10
        self.spend_money(expenses)
        print(f"{self.name} relaxed for {hours} hours.")

    def pass_year(self):
        self.age += 1

    def make_choice(self, choice):
        if choice == "work":
            self.earn_money(100)
        elif choice == "study":
            self.study_more(10)
        elif choice == "solve_problem":
            self.solve_problem("Exam preparation")
        elif choice == "relax":
            self.relax(5)

    def __str__(self):
        return f"{self.name} ({self.age} years old), money: {self.money}, study: {self.study}"

student = Student("Tom", 18)
print(student)

choices = ["work", "study", "solve_problem", "relax"]
for _ in range(10):
    choice = random.choice(choices)
    student.make_choice(choice)

print(student)

student.pass_year()
print(student)
