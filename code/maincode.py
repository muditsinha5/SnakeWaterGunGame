import random
cpu=0
player=0
print("Welcome to Snake Water Gun game")
print("Please enter your name:")
name=input()
for i in range(0,3):
    print("Enter your choice: Snake Water Gun")
    choice=input()
    listcomp=['snake','water','gun']
    x=random.choice(listcomp)
    if x=="snake" and choice=="water":
        print("CPU result:",x)
        print(name,"result:",choice)
        print("CPU won!")
        cpu=cpu+1

    if x=="snake" and choice=="gun":
        print("CPU result:",x)
        print(name,"result:",choice)
        print(name,"won!")
        player=player+1
    
    if x=="water" and choice=="gun":
        print("CPU result:",x)
        print(name,"result:",choice)
        print("CPU won!")
        cpu=cpu+1
    
    if x=="water" and choice=="snake":
        print("CPU result:",x)
        print(name,"result:",choice)
        print(name,"won!")
        player=player+1

    if x=="gun" and choice=="water":
        print("CPU result:",x)
        print(name,"result:",choice)
        print( name,"won!")
        player=player+1

    if x=="Gun" and choice=="Snake":
        print("CPU result:",x)
        print(name,"result:",choice)
        print("CPU won!")
        cpu=cpu+1

    if x==choice:
        print("Tie between ",name,"CPU")
        cpu=cpu+1
        player=player+1
    
if cpu>player:
    print("Total score")
    print(name,end=" ")
    print(player)
    print("CPU",cpu)
    print("CPU won the tournament")
elif cpu==player:
    print("Tie between both the players")
else:
    print("Total score")
    print(name,end=" ")
    print(player)
    print("CPU",cpu)
    print(name,"won the tournament")
    
    
