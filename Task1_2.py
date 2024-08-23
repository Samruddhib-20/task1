import random

def main():
    guess_number = random.randint(1, 100)
    guessed = False
    
    print("Welcome to the number guessing game.")
    
    print("guess the number between 1 to 100:")
    
    while not guessed:
        
        try:
            guess = int(input("Enter a guess :"))
            
            if guess < 1 and guess > 100:
                print("Please Enter the number between 1 and 100")
            elif guess > guess_number :
                print("Try again! The number is to High")
            elif guess < guess_number :
                print("try again! the number is to Low")
            else:
                print("congratulations! You guess the correct number.")
                guessed = True
                
        except ValueError:
            print("The number is not between 1 and 100")
            


    
    
if __name__ =="__main__":
    main()