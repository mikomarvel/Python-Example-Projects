#python example project_1
#NUMBER_GUESSING_GAME

import random #imports a random number for a fair play

while True:
     correct_guess = random.randint(1, 10) #generates a random integer
     attempt = 0
     while attempt < 3:
                attempt = attempt + 1
                print(f"This is your {attempt} attempt.")
                user_guess = int(input("enter your guess from 1-10:- ")) #casting the input data to get it as a number.
                if user_guess == correct_guess: #using this(==) because this(=)is used for assigning.
                    print(f"you guessed right🫡---> {correct_guess}")
                    break 
                elif user_guess > correct_guess:
                    print(f"a bit higher than the correct answer!! THE CORRECT GUESS IS-->{correct_guess} ")

                elif user_guess < correct_guess:
                    print(f"you are bit lower than the correct guess.!! THE CORRECT GUESS IS-->{correct_guess} ")

                else:
                    print("wroooong🫠")
