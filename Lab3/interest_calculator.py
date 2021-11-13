from datetime import datetime
# Program Name:  interest_calculator
# Program Description
# This program will continuously ask user for inputs to calculate the interest earned until the
# user enters number 0 (zero) in principle.
# Once the user enters any number less or equal to 0 in principle, the program will exist.
#
# @Author: Ziwen Li
# @Date:10/17/21
#

name = "CNET-142: Ziwen li"
labName = "Lab 3: Interest Rate"
time = datetime.now()
currenTime = time.strftime("%Y-%m-%d %H:%M:%S")

print(name,"-",labName)
print(currenTime)

p = 1

while p > 0:
    p = float(input('Enther the starting principal, 0 ti quit : '))
    r = float(input('Enter the annual interst rate : '))
    n = float(input('How many times per year is the interest compounded? '))
    t = float(input('For how many years will the account earn interest? '))
    total= p*(1+float(r/100)/n)**(n*t)
    interest = total - p
    print('At the end of ' , t , ' years you will have $' , format(total,',.2f') ,
    "with interest earned $",format(interest,',.2f'))
    print('')





