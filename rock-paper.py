
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
import random as r
u1=int(input("Hello there welcome to rock paper scissors .\nPlease enter number of Trial "))
print(f'Please choose your move :\n1.Rock \n2.Paper \n3.Scissors ')
def dec():
    global comcount
    global usercount
    if user==com:
        print(f"Drawwwww")
    elif user==1:
        if com==3  :
            print(f"Congratulations, You win !!")
            usercount+=1
        elif com==2  :
            print(f"Better Luck next time!!")
            comcount+=1
    elif user==2:
        if com== 1 :
            print(f"Congratulations, You win !!")
            usercount+=1
        elif com== 3 :
            print(f"Better Luck next time!!")
            comcount+=1
    elif user==3 :
        if com== 1 :
            print(f"Congratulations, You win !!")
            usercount+=1
        elif com== 2 :
            print(f"Better Luck next time!!")
            comcount+=1
comcount=0
usercount=0
for i in range(u1):
    user=int(input("Enter your move 1 OR 2 OR 3 = "))
    com=r.randint(1,3)
    if user==1 or user==2 or user==3:
            
    #output 
        if user==1:
            print(f"You choose {rock}")
        elif user==2:
            print(f"You choose {paper}")
        else:
            print(f"You choose {scissors}")
        if com==1:
            print(f"Computer choosen {rock}")
        elif com==2:
            print(f"Computer choosen {paper}")
        else:
            print(f"Computer choosen {scissors}")
    
        dec()
        
    else :
        print("You chose a invalid number . You LOOse")

print("Hoorahhhh!! U win " if usercount>comcount else " Better luck next time" )




