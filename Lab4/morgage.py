"""
This program will calculate morgage loan and interest

User can use this program to know monthly payment,total amount payments, and total interest
"""


def morgage ():
    print("\n", "Calculating Mortgage Payment", "\n")
    loanAmount = 1
    while loanAmount > 0:
        loanAmount = float(input('Enther the loan amount, 0 to quit : '))
        if loanAmount == 0:
            print('\n','Existing Mortgage Payment program','\n')
            break;
        interestRate = float(input('Enter the loan interest rate % : '))
        loanTerm = int(input('Enter the loan term (number of years) : '))

        monthlyRate = (interestRate / 100) / 12
        numPayments = loanTerm * 12
        monthlyPayment = loanAmount * monthlyRate * pow((1 + monthlyRate), numPayments) \
                         / (pow((1 + monthlyRate), numPayments) - 1)
        totalPayment = monthlyPayment * (loanTerm * 12)
        interestPaid = totalPayment - loanAmount

        print("For the loan Amonunt of",format(loanAmount,',.2f'),"for",loanTerm,"years with interest rate",\
              interestRate,"%")
        print ("The monthly pamnent is $",format(monthlyPayment,',.2f'))
        print('Total amount paid for this loan is %',format(totalPayment,',.2f'))
        print('Total interest paid for this loan is $',format(interestPaid,",.2f"),'\n')

