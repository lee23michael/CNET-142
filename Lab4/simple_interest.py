'''
This function will calculate the annual interst by asking user curtain input

Users will know the total amount  and interes after curtain years, and t
'''



def simpleInterest():
        print("\n","Calculating Simple Interest","\n")

        p = 1
        while p > 0 :
                p = float(input('Enther the starting principal, 0 to quit : '))
                if p == 0:
                        print('\n','Existing Simple Interest program','\n')
                        break;
                r = float(input('Enter the annual interst rate : '))
                n = float(input('How many times per year is the interest compounded? '))
                t = float(input('For how many years will the account earn interest? '))

                total = p * (1 + float(r / 100) / n) ** (n * t)
                interest = total - p

                print('At the end of ', t, ' years you will have $', format(total, ',.2f'),
                      "with interest earned $", format(interest, ',.2f'))
