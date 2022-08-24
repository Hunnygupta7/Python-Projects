print("Welcome To Quizz Game!!")

playing = input("Do You Want To Play? ")
if playing.lower() != "yes":
    quit()

score = 0

print("Okay, Let's Play:)")

answer = input("Your First Question is:\nWhat Does RAM Stands For? ")
if answer.lower() == "random access memory":
    print("Correct Answer!!")
    score += 1
else:
    print("Incorrect Answer!!")

answer = input("Your Second Question is:\nWhat Does GPU Stands For? ")
if answer.lower() == "graphics processing unit":
    print("Correct Answer!!")
    score += 1
else:
    print("Incorrect Answer!!")

answer = input("Your Third Question is:\nWhat Does CPU Stands For? ")
if answer.lower() == "central processing unit":
    print("Correct Answer!!")
    score += 1
else:
    print("Incorrect Answer!!")

answer = input("Your Fourth Question is:\nWhat Does PSU Stands For? ")
if answer.lower() == "power supply":
    print("Correct Answer!!")
    score += 1
else:
    print("Incorrect Answer!!")

print("Congratulations! You Got " + str(score) + " Questions Correct")
print("Congratulations! You Got " + str((score/4) * 100) + "%.")
