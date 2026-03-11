score = 0

answer = input("What is the capital of Pakistan? ")

if answer.lower() == "islamabad":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("Your score:", score)
