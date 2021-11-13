import printFirst
import simple_interest
import morgage

# Program Name:  Menu Function
# Program Description
# This program will ask user to chose one of the option, interest calculation or morgage calculation
# by enter the number of the selection.
#
# @Author: Ziwen Li
# @Date:10/24/21
#

def main():
    printIfo= printFirst.print_first("Ziwen li", "4","Menu Function")
    print(printIfo)

    msg = "\n"+ "------------------" + "\n"
    msg = msg + "1  Calculate Simople Interest"+"\n"
    msg = msg + "2  Calculate Mortgage Payment"+"\n"
    msg = msg + "99 Quite the Program"+"\n"
    msg = msg +  "------------------"

    done = False
    while not done:
        print(msg)
        num = int(input("Select one of the command number above: "))
        if num == 99:
            break;
        elif num == 1:
            simple_interest.simpleInterest()
        elif num == 2:
            morgage.morgage()
        else :
            print("Error: Command not recognized")

if  __name__ == '__main__':
    main()