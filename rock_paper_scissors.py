# -*- coding: utf-8 -*-
"""
@Python Programming I-Homework2
Created on Sun Apr 14 15:43:47 2019

@author: Karen (Hui) Xiao
"""
import random
import sys
yourChocie = 0
yourScore=0
computerScore=0

condition1= True
condition2=True

while condition1:
    
    
    print ("make a move! (r/s/p)") ##prompt the user to make a move
    yourMove=input()

    if yourMove=='r':
        yourChoice=1
        condition1=False
    elif yourMove=='p':
        yourChoice=2
        condition1=False        
    elif yourMove=='s':
        yourChoice=3
        condition1=False       
    else: ##if the input is none of the 3 options (r/s/p), prompt the user to enter choice again
        yourChoice=0
        print("Invalid Input.Please make a move from r(rock), p(paper), and s(scissors)!")
        condition1=True
        continue ##continues the loop by asking 'make a move!'
    
    computerChoice=random.randint(1,3)

    
    if yourChoice==computerChoice:
        print("You Tie!")       
    elif yourChoice == 1:
        if computerChoice==2:
            print("You chose rock and the computer chose paper. You Lose!")
            computerScore=computerScore+1
        elif computerChoice==3:
            print("You chose rock and the computer chose scissors. You Win!")
            yourScore=yourScore+1
    elif yourChoice == 2:
        if computerChoice==1:
            print("You chose paper and the computer chose rock. You Win!")
            yourScore=yourScore+1
        elif computerChoice==3:
            print("You chose paper and the computer chose scissors. You Lose!")
            computerScore=computerScore+1
    elif yourChoice == 3:
        if computerChoice==1:
            print("You chose scissors and the computer chose rock. You Lose!")
            computerScore=computerScore+1
        elif computerChoice==2:
            print("You chose scissors and the computer chose paper. You Win!")
            yourScore=yourScore+1
    

    ScoreRequest1 = input()
    if ScoreRequest1=='sc':
        print('human:'+str(yourScore)+',computer:'+str(computerScore))
        
        
    while condition2:
        print('Do you want to play again? (Y/N)?')
        yourAnswer=input()
       
        if yourAnswer == 'y':
            condition1 = True
            break
        elif yourAnswer == 'n':
            print('thanks bye!')   
            exit()
        elif yourAnswer != 'y' or yourAnswer != 'n':
            print("Invalid Input.Please answer the question using 'y' or 'n'.") ##if the user does not enter y or n, prompt them to answer again
            condition2 = True
            condition1 = False
            
           
    
    
    


        



