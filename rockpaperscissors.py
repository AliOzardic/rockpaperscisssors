import random
options = ("rock", "paper" ,"scissors")

player_points = 0
cpu_points = 0

playing = True
while playing:
    cpu = random.choice(options)
    player = None
    while player not in options:
            player = input("enter your choice(rock,paper,scissors):").lower()
    if player == cpu:
        print("It's a tie")
        player_points+=1
        cpu_points+=1
    elif player =="rock" and cpu == "scissors":
        print("YOU WİN!")
        player_points+=1
    elif player == "paper" and cpu =="rock":
        print("YOU WİN!")
        player_points+=1
    elif player == "scissors" and cpu == "paper":
        print("YOU WİN!")
        player_points+=1
    else:
        print("YOU LOST!")
        cpu_points+=1
    print(f"player:{player}")
    print(f"cpu: {cpu}") 
    print(f"total: cpu={cpu_points} player={player_points}")

    if not input("do you want to play again(y or n).").lower() == "y":
        playing = False
print("thanks for playing")