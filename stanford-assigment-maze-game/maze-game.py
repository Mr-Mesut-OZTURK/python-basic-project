def main():
    """
    """
    print("""
          4    --->you are at here(1,1)
          3   /
          2  /
          1 /
          0 1 2 3 4
          """)
    a = 1
    x = 1
    y = 1
    print("Welcome to first person Karel. You're at row 1, column 1, facing East (facing column 3)")
    while True:
        mov = input("What would you like to do? You can move and turn left. Press enter to finish. ")
        if mov == "move" :
            if a == 1 and x < 3 :
                x += 1
                print(f"You moved one step forward and now you're at row {y} column {x}")
            elif a == 2 and y < 3 :
                y += 1
                print(f"You moved one step forward and now you're at row {y} column {x}")
            elif a == 3 and x > 0 :
                x -= 1
                print(f"You moved one step forward and now you're at row {y} column {x}")
            elif a == 4 and y > 0 :
                y -= 1
                print(f"You moved one step forward and now you're at row {y} column {x}")
            else:
                print("You can't move forward!")
        elif mov == "turn left" :
            if a < 4 :
                a += 1
            else:
                a = 1
            
            if a == 1:
                print("You turned left and are now facing East.")
            elif a == 2 :
                print("You turned left and are now facing North.")
            elif a == 3 :
                print("You turned left and are now facing West.")
            elif a == 4 :
                print("You turned left and are now facing South.")
  
        elif mov == "exit":
            break
        else:
            print("Error: you can write only 'move' or 'turn left' or 'exit'.")


if __name__ == "__main__":
    main()