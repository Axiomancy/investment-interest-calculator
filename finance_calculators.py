"""
1)Create a program that allows the user to access
two different financial calculators: 
an investment calculator and a home loan repayment calculator.
2)Import math module.
3)Write the code that will do the following:
    1.The user should be allowed to choose which calculation they want to do:
        investment - to calculate the amount of interest you'll earn on your investment
        bond - to calculate the amount you'll have to pay on a home loan
    2. then promp the user to enter either 'investment' or 'bond' from the menu above to proceed,
    (note that how the user capitalises their selection should not affect how the prognarm runs)
    3.If the user doesnt type in a valid input, show an appropriate error message.
    4.If the user selects 'investment', do the following:
        1;Ask the user to input:
            The amount of money that they are depositing.
            The interest rate (as a percentage). Only the number of the interest
            The number of years they plan on investing.
        2;Then ask the user to input if they want “simple” or “compound” interest and store this in a variable called interest. 
        3;Depending on whether or not they typed “simple” or “compound”, output the appropriate amount that they will get back.
    5.If the user selects 'bond', do the following:
        1;Ask the user to input:
            The present value of the house.
            The annual interest rate.
            The number of months they plan to take to repay the bond.
        2;Calculate how much money the user will have to repay each month and output the answer.

"""

import sys #I imported this just for a cleaner exit form the program

import math #This imports the math module


while True: #I have used a while loop here, this is to prevent an invalid user response from STILL generating the 'finance details' output/inputs, before eventually telling the user that their response was invalid. 
    print("\n")
    print("investment - to calculate the amount of interest you'll earn on your investment. ")
    print("bond - to calculate the amount you'll have to pay on a home loan. ")
    print("\n")
    user_input = input("Enter either 'investment' or 'bond' to proceed: ").lower()
    print("\n")
    if user_input == 'investment' or user_input == 'bond':
        break #If the user inputs a valid response then the while loop will 'break', and the rest of the program will run.
    else:
        print("im sorry your answer was not valid, please enter a valid resopnse from the list below: ") #If the user dosent give a valid respose this message shows and the loop runs again.

answer1 = 'investment' #I issued these with variable as part of trying to figure out how to stop the 'finance details' running even if the user input was not a valid response.
answer2 = 'bond'

#Finance details
print("\n")
if user_input == answer1:
    p = int(input("please input your investment to the nearest £ "))
    r = float(input("please enter your interest percentage: ")) / 100
    t = int(input("please enter the amount of years that you wish to make your investment for: "))
    print("\n")
    
    user_input2 = input("would you like a 'simple' or 'compound' investment? ")
    if user_input2 == 'simple':#simple investment calculation
        A = p * (1 + r * t)
        print("\n")
        print(f"The amount of interest you'll earn on your investment is £{A}")
    else:
        user_input2 == 'compound'#compound investment calculation
        B = p * math.pow((1 + r), t)
        print("\n")
        print(f"The amount you'll earn on your compound interest is £{B}")

elif user_input == answer2:#bond repayment calculation
     P = float(input("please enter the current value of the house £ "))
     I = float(input("please enter the annual interest rate you will be paying: ")) /100 /12
     N = int(input("please enter how many months you will be repaying the loan over: "))
     R = (I * P)/(1 - (1 + I)**(-N))
     print("\n")
     print(f"The monthly repayments on your home loan will be £{R}")
    
sys.exit()