from datetime import datetime
# Program Name: car_efficiency
# Program Description
# This program is to practice converting input value to a number, and print it in a curtain format
# It will ask user to enter gas tank capacity, mileage, and gas price
# Then calculate the cost and maximum running distance with full tank of gas
#
# @Author: Ziwen Li
# @Date:10/10/21
#

name = "CNET-142: Ziwen li"
labName = "Lab 2: Car Mileage"
time = datetime.now()
currenTime = time.strftime("%Y-%m-%d %H:%M:%S")

print(name,"-",labName)
print(currenTime)

capacity = float(input("Enter the capacity of the car's gas tank (in gallons) : "))
miles_per_gallon = int(input("Enter car's miles per gallon : "))
price = float(input("Enter price per gallon : "))
cost = 100 / miles_per_gallon * price
distance = capacity * miles_per_gallon


print('Cost for driving 100 mile is $',format(cost,',.2f'),sep='')

print ('Distance on a tank of gas is' , format(distance,',.2f'),'miles')

print('Your car MPS is',miles_per_gallon)

if miles_per_gallon < 30 :
   print ("It is not fuel efficient car.")
elif 30 <= miles_per_gallon < 40 :
    print("It is average fuel efficient car.")
elif 40 <= miles_per_gallon < 50:
    print("It is fuel efficient car")
else:
    print("It is very fuel efficient car")
