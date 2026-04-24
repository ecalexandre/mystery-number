#Number game program
import random

name = input("Enter your name to start the game (Press enter to finish): ")

print("*************************************************************************************************************")
print(f"Hello {name}! Welcome to the Guess The Number challenge! The game is about picking a number between 1 to 100.")
print("The game will continue as long as you did not get the right number!")
print("If you get the right number, you will win and receive the amount of tries it took you to win!")
print("So here are the rules:")
print("1. Do not put a character that is not a number because you will never get the right answer by doing it.")
print("2. If you ever put a number that is too high or too low, I am gonna give you hints to win easily.")
print("Good luck!") #Welcome message + explaining the game   
print("*************************************************************************************************************")

secret_number = random.randint(1,100) #Random number between 1 to 50 chosen by the program that the user has to input 
game_running = True
attempts = 0


while game_running:
      attempts += 1
      if game_running == False:
           break #To display the amount of tries
      
      user_input = input("Enter your number here (Press enter to finish): ")    
      try:
        val = int(user_input)
        if val == secret_number:
           print("Correct! You got the number!")
           print(f"Amount of tries to win: {attempts}")
           game_running = False
        
        elif val > secret_number and val <= 100 and val != secret_number: 
             print("Wrong number, try again")
             print("Hint : Psss, the correct number is below that") 

        elif val >= 100 and val != secret_number:
             print("Wrong number, try again")
             print("This number is too high, it has to be between 1 and 100")

        elif val < 1:
             print("Wrong number, try again")
             print("This number is too low, it has to be between 1 and 100")

        elif val < secret_number and val < 100 and val > 1 and val != secret_number:             
             print("Wrong number, try again")
             print("Hint : Pssss, the correct number is above that")   

      except ValueError:
             print("This character is not a number, try again")
      
      except ValueError:
             print("This character is not a number, try again")
      
