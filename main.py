import random
'''
1 for snake
-1 for water
0 for gun 

'''

computer = random.choice([1,-1,0])
your_str = input("Enter your choice: ")
your_dict = {"snake": 1, "water":-1, "gun":0}
reverse_dict = {1:"Snake" , -1:"Water", 0:"Gun"}
you=your_dict[your_str]

print(f"You choose {reverse_dict[you]} \nComputer choose {reverse_dict[computer]}")

if you == computer:
    print("It's a draw")
else:
    if you == 1 and computer == -1:
        print("You Won")
    
    elif you == 1 and computer == 0:
        print("Computer Won")
    
    elif you == -1 and computer == 1:
        print("Computer Won")
    
    elif you == -1 and computer == 0:
        print("You Won")
    elif you == 0 and computer == -1:
        print("Computer Won")
    
    elif you == 0 and computer == 1:
        print("You Won")
    
