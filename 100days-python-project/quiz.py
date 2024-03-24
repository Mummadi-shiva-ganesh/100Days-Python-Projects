print("Welcome to the Quizz Game")

ask = input("Would you like to play the game (yes/no)")
if ask.lower() != "yes":
  quit(print("Goodbye:)"))

if ask == "yes":
  print("Lets start the Game")
  print("Quiz has total of 5 questions if you answer correct your score will increase to +1\n ")
  print("So, before answering  think again")
  score = 0
  print(f"Your current score is {score}")

print("1st Question")
answer = input("What is the captial city of India?\n")
if answer.lower() == "new delhi":
  print("You hava answered correctly ")
  score += 1
  print(f"Your new score is {score}\n")
else:
  print("Your answer is not perfect:(")
  print(f'You score is {score}')

print("2st Question")
answer = input("What is the short form of Hyper Text Markup Language?\n")
if answer.lower() == "html":
  print("You hava answered correctly ")
  score += 1
  print(f"Your new score is {score}\n")
else:
  print(f'You score is {score}')

print("3st Question")
answer = input("What is the short-form of Cascading style sheets?\n")
if answer.lower() == "css":
  print("You hava answered correctly ")
  score += 1
  print(f"Your new score is {score}\n")
else:
  print("Your answer is not perfect:(")
  print(f'You score is {score}')

print("4st Question")
answer = input("What is the short form of hypertext Preprocessor?\n")
if answer.lower() == "php":
  print("You hava answered correctly ")
  score += 1
  print(f"Your new score is {score}\n")
else:
  print("Your answer is not perfect:(")

print("5st Question")
answer = input("Is Python is case-sensitive Programming language?\n")
if answer.lower() == "yes":
  print("You hava answered correctly ")
  score += 1
  print(f"Your new score is {score}\n")
else:
  print("Your answer is not perfect:(")

if score == 5:
  print(f"Your final score is {score}")
  print("Congratulation You have answered all correct answers:)")
else :
  print(f"Your score is {score}")
  print("Well played:]")