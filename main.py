import random
b= random.randint(1, 100)
print("Welcome to the Guessing Game!")

a = -1
guess = 1

while ( a!= b):
   a = int(input("Guess a number : "))
   if a>b:
        print("Your guess is too High.")
        guess+=1
        
   elif a<b:
     print("Your guess is too Low.")  
     guess+=1  

print(f" Congratulations! You guessed the number right. The number was {b} and you took {guess} guesses.")
print("You have completed the game.")
print("Thank you for playing!")

