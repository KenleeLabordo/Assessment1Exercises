""" Your solution must be no more than 250 lines of code.
Develop a program that presents the user with quiz of arithmetic problems. Each "play" of the quiz should be 10 questions. The user should initially be presented with a short menu of options to select a difficulty level. It could look something like this:

DIFFICULTY LEVEL
 1. Easy
 2. Moderate
 3. Advanced
The difficulty levels determine the number of digits in the numbers to be added or subtracted. Easy means only single digit numbers; moderate means double digit numbers; and advanced means 4-digit numbers. After the user picks the level they desire, your program presents problems that look like this:

45 + 9 =
34 - 88 =
etc
For each problem presented, the user is given a chance to answer. If the answer is correct, another problem is presented. If the answer is wrong, the user is to be given one more chance at that problem. The program should keep a tally of the users score, awarding 10 points for a correct answer on first attempt and 5 points on the second attempt. You should implement a random number generator (see the resources folder) to determine:

The values to be added or subtracted
Whether the problem is addition or subtraction
  The program should include the functions listed below. These functions should make use of parameters and return values as appropriate. You may include others or extend the functionality of the program if you see fit.

displayMenu: A function that displays the difficulty level menu at the beginning of the quiz.

randomInt: A function that determines the values used in each question. The min and max values of the numbers should be based on the difficulty level chosen as described above.

decideOperation: A function that randomly decides whether the problem is an addition or subtraction problem and returns a char.

displayProblem: A function that displays the question to the user and accepts their answer.

isCorrect: A function that checks whether the users answer was correct and outputs an appropriate message

displayResults: function that outputs the users final score out of a possible 100 and ranks the user based on their score (e.g. A+ for a score over 90)

  Once the user has finished the quiz, prompt them to see if they'd like to play it again.
  
  """

import random

def displayMenu():
    # Displaying the menu to let the user select difficulty level
    print("DIFFICULTY LEVEL")
    print("1. Easy")
    print("2. Moderate")
    print("3. Advanced")
    # Returning the user's choice as an integer
    return int(input("Choose Difficulty(1-3): "))

def randomInt(level):
    # Based on the level, generate random numbers of different ranges
    if level == 1:
        return random.randint(1, 9)  # Single-digit numbers for Easy
    elif level == 2:
        return random.randint(10, 99)  # Two-digit numbers for Moderate
    elif level == 3:
        return random.randint(1000, 9999)  # Four-digit numbers for Advanced

def decideOperation():
    # Randomly select whether the problem will be addition or subtraction
    return random.choice(['+', '-'])

def displayProblem(num1, num2, operation):
    # Showing the math problem to the user and waiting for their input (answer)
    print(f"{num1} {operation} {num2} = ", end="")
    return int(input())  # Return the user's input as an integer

def isCorrect(user_answer, correct_answer, attempt):
    # Checking if the user's answer is correct or not
    if user_answer == correct_answer:
        if attempt == 1:
            print("Correct!")
            return 10  # Full points for the first attempt
        else:
            print("Correct on the second attempt!")
            return 5  # Half points for the second attempt
    else:
        if attempt == 1:
            print("Wrong answer. Try again.")  # Giving a second chance
        else:
            print("Wrong again.")  # No more chances
        return 0  # No points for wrong answers

def displayResults(score):
    # Displaying the user's final score out of 100 and ranking them based on the score
    print(f"\nYour final score: {score}/100")
    if score > 90:
        print("Rank: A+")
    elif score > 80:
        print("Rank: A")
    elif score > 70:
        print("Rank: B")
    elif score > 60:
        print("Rank: C")
    else:
        print("Rank: D")  # Below 60 gets a D

def main():
    score = 0  # Initialize the score
    level = displayMenu()  # Ask the user to choose a difficulty level
    
    for i in range(10):  # Loop to present 10 questions
        num1 = randomInt(level)  # Generate the first random number
        num2 = randomInt(level)  # Generate the second random number
        operation = decideOperation()  # Randomly choose addition or subtraction
        
        if operation == '+':
            correct_answer = num1 + num2  # Calculate the correct answer for addition
        else:
            correct_answer = num1 - num2  # Calculate the correct answer for subtraction

        # First attempt
        user_answer = displayProblem(num1, num2, operation)  # Present problem and get user's answer
        points = isCorrect(user_answer, correct_answer, 1)  # Check if the answer is correct (first attempt)
        if points == 0:
            # Second attempt if the first was wrong
            user_answer = displayProblem(num1, num2, operation)  # Present the same problem again
            points = isCorrect(user_answer, correct_answer, 2)  # Check the second attempt
        
        score += points  # Add the earned points to the total score

    displayResults(score)  # Show the final score and rank

if __name__ == "__main__":
    main()  # Call the main function to start the quiz
