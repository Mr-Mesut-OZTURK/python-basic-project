import random
import math

def guess_number(name):    
    '''
    It is a funy guess number game. 
    '''
    heart = 0
    chapter = 1
    score = 0
    try_num = 0

    print("""
                        [H]=============MESUT===========[x]
                        |                                 |
                        |            Welcome!             |
                        |          Are you ready!         |
                        |                                 |
                        [*]=============================[*]
    """)

    while True:

        # When game start first time
        if heart == 0:
            cont = input("For continue press 'c' : ")
            if cont != 'c':
                break
            heart = int(input("How many attempts can you find it? : "))
            score = 100 - (heart * 10)
            chapter = 1

        rand_num = random.randint(1,100)

        print('*' * 20 + '  ' * 20 + '*' * 20)
        print(f"                  Welcome {chapter}. game :)) ")
        print(f"                  You have {heart} heart...")
        print(f"                  Your score {math.ceil(score)}...")
        print('*' * 20 + '  ' * 20 + '*' * 20)
        if chapter != 1:
            cont = input("For continue press 'c' : ").lower()
            if cont != 'c':
                break

        # Game start at here.
        print("I keep a number in my mind.")
        while heart > 0:
            guess = int(input("Guess it! : "))
            heart -= 1
            if guess == rand_num:
                print("* " * 20)
                print("Congratulations you did it in ", try_num, " try")
                print("* " * 20)
                score = score + (score * (10 * (1 + (1/try_num)))) 
                chapter += 1
                heart += 8
                break
            elif heart == 0:
                print("You lost :(")
            elif (guess < rand_num) and (guess > 0):
                print("You guessed too small!")
            elif (guess > rand_num) and (guess < 100):
                print("You guessed too high!")
            elif (guess < 0) or (guess > 100) :
                print("My number is between 1 and 100 :))")
            else:
                print("Please enter only number...")
            try_num += 1
            print("- " * 10)

if __name__ == "__main__":
    guess_number("mesut")