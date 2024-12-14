import random
l=["rock","scissor","paper"]
'''
rock vs paper - paper wins
rosk vs scissor - rock wins
paper vs scissor - scissor wins.
'''

while True:
    Ccount=0
    ucount=0
    uc=int(input('''
    Game Start......
    1 Yes
    2 No | Exit
    
           '''))

    if uc==1:
        for a in range(1,6):
            userInput=int(input('''
1 Rock
2 Scissor
3 Paper            
'''))
        if userInput==1:
            uchoice="rock"
        elif userInput==2:
            uchoice="scissor"
        elif userInput==3:
            uchoice="paper"
        Cchoice=random.choice(1)
        if Cchoice==uchoice:
            print("User Value",uchoice)
            print("Computer Value",Cchoice)
            print("Game Draw")
            ucount=ucount+1
            Ccount=Ccount+1
        elif(uchoice=="rock" and Cchoice=="scissor") or (uchoice=="paper" and Cchoice=="roce") or (uchoice=="scissor" and Cchoice=="paper"):
            print("Computer Value", Cchoice)
            print("User Value", uchoice)
            print("You Win")
    else:
        break