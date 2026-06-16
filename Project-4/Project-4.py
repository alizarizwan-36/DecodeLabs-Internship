# General Knowledge Quiz
# Project 4

score = 0

# Question 1
answer = input("1.What is the chemical symbol for water? ").strip().lower()

if answer == "h2o":
    score += 1
    print("Correct!")
else:
    print("Incorrect! The correct answer is H2O.")

# Question 2
answer = input("2. Which planet is known as the Red Planet? ").strip().lower()

if answer == "mars":
    score += 1
    print("Correct!")
else:
    print("Incorrect! The correct answer is Mars.")

# Question 3
answer = input("3. Who wrote 'Romeo and Juliet'? ").strip().lower()

if answer == "william shakespeare":
    score += 1
    print("Correct!")
else:
    print("Incorrect! The correct answer is William Shakespeare.")

# Final Result
print("\nQuiz Complete!")
print(f"Your final score is {score}/3")
