SALARY=int(input("Enter amount of your salary: "))
LOAN=int(input("Enter amount of your Desired Loan: "))

if (SALARY >= 30000.00) and (LOAN <= SALARY*10):
    MONTHS_LOAN=int(input("Enter Desired Months To pay loan: "))
    INTEREST=LOAN * 0.10 
    NEW_LOAN= INTEREST + LOAN
    PAYABLE= NEW_LOAN/MONTHS_LOAN
    ROUNDED_PAYABLE = round(PAYABLE, 2)
    print("Your Loan is: ",ROUNDED_PAYABLE,"/MONTH" )
 
else:
  print("Customer is not eligible for a loan. Reason either low salary or too high loan request.")

    