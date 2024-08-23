def addition(no1, no2):
    Ans = 0
    Ans = no1 + no2 
    return Ans

def substraction(no1, no2):
    Ans = 0
    Ans = no1 - no2 
    return Ans

def multiplication(no1, no2):
    Ans = 0
    Ans = no1 * no2 
    return Ans 

def division(no1,no2):
    Ans = 0 
    Ans = no1 / no2
    if no2 == 0 :
        return "Error: Division by zero is not allowed."
    return Ans 

def main():
    
    print("Select Operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    while True:
        choice = input("Enter choice (1/2/3/4): ")
        
        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"{num1} + {num2} = {addition(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {substraction(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiplication(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {division(num1, num2)}")
        else:
            print("Invalid input. Please enter a number between 1 and 4.")
        
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
    
if __name__ =="__main__":
    main()


    