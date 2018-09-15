import random

winning_num=random.randint(1,10)

print("WELCOME TO Number guessing game: guess the number between 1 to 10")

Player1=input("Enter Player1 name:")
Player2=input("Enter Player2 name:")

num1=int(input(f"{Player1} enter number:"))
num2=int(input(f"{Player2} enter number:"))

game_over=False
guess1=0
guess2=0

while not game_over:
    guess1 += 1
    guess2 += 1
    if (num1==winning_num and num2==winning_num):
        print(f"{Player1} you win, you guessed {guess1} times")
        print(f"{Player2} you win, you guessed {guess2} times")
        break

    elif (num1==winning_num and num2<winning_num):
        win1=(f"{Player1} you win, you guessed {guess1} times")
        print(win1)
        print(f"{Player2} your guess is low")
        num2=int(input(f"{Player2} guess again:"))
        game_over = True 
        while game_over:
            guess2 += 1
            if num2==winning_num:
                win2=(f"{Player2} you win, you guessed {guess2} times")
                print(win2)
                break
            elif num2<winning_num:
                print(f"{Player2} your guess is low")
                num2=int(input(f"{Player2} guess again:"))
            elif num2>winning_num:
                print(f"{Player2} your guess is high")    
                num2=int(input(f"{Player2} guess again:"))    

    elif (num1==winning_num and num2>winning_num):
        win1=(f"{Player1} you win, you guessed {guess1} times")
        print(win1)
        print(f"{Player2} your guess is high")
        num2=int(input(f"{Player2} guess again:"))
        game_over = True
        while game_over:
            guess2 += 1
            if num2==winning_num:
                win2=(f"{Player2} you win, you guessed {guess2} times")
                print(win2)
                break
            elif num2<winning_num:
                print(f"{Player2} your guess is low")
                num2=int(input(f"{Player2} guess again:"))
            elif num2>winning_num:
                print(f"{Player2} your guess is high")    
                num2=int(input(f"{Player2} guess again:"))  

    elif (num1<winning_num and num2==winning_num):
        win2=(f"{Player2} you win, you guessed {guess2} times")
        print(win2)
        print(f"{Player1} your guess is low")
        num1=int(input(f"{Player1} guess again:"))
        game_over = True
        while game_over:
            guess1 += 1
            if num1==winning_num:
                win1=(f"{Player1} you win, you guessed {guess1} times")
                print(win1)
                break
            elif num1<winning_num:
                print(f"{Player1} your guess is low")
                num1=int(input(f"{Player1} guess again:"))
            elif num1>winning_num:
                print(f"{Player1} your guess is high")    
                num1=int(input(f"{Player1} guess again:"))    
       
    elif (num1>winning_num and num2==winning_num):
        win2=(f"{Player2} you win, you guessed {guess2} times")
        print(win2)
        print(f"{Player1} your guess is high")
        num1=int(input(f"{Player2} guess again:"))
        game_over = True
        while game_over:
            guess1 += 1
            if num1==winning_num:
                win1=(f"{Player1} you win, you guessed {guess1} times")
                print(win1)
                break
            elif num1<winning_num:
                print(f"{Player1} your guess is low")
                num1=int(input(f"{Player1} guess again:"))
            elif num1>winning_num:
                print(f"{Player1} your guess is high")    
                num1=int(input(f"{Player1} guess again:")) 
       
    elif (num1<winning_num and num2<winning_num):
        print(f"{Player1} your guess is low")
        print(f"{Player2} your guess is low")
        num1=int(input(f"{Player1} guess again:"))
        num2=int(input(f"{Player2} guess again:"))

    elif (num1<winning_num and num2>winning_num):
        print(f"{Player1} your guess is low")
        print(f"{Player2} your guess is high")
        num1=int(input(f"{Player1} guess again:"))
        num2=int(input(f"{Player2} guess again:"))

    elif (num1>winning_num and num2>winning_num):
        print(f"{Player1} your guess is high")
        print(f"{Player2} your guess is high")
        num1=int(input(f"{Player1} guess again:"))
        num2=int(input(f"{Player2} guess again:"))

    elif (num1>winning_num and num2<winning_num):
        print(f"{Player1} your guess is high")
        print(f"{Player2} your guess is low")
        num1=int(input(f"{Player1} guess again:"))
        num2=int(input(f"{Player2} guess again:"))                               

if game_over:
    print("\nFinal score:")
    print(win1)
    print(win2)   

print("\nFinal result:")
if (guess1<guess2):
    print(f"{Player1} you win")
elif (guess1>guess2):
    print(f"{Player2} you win")
elif (guess1==guess2):
    print("Both are winner")    