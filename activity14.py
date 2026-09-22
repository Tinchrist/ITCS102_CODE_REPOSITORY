age = int(input("Enter your age    >   "))
is_employed = input("Are you currently employed (True / False) ")
credit_score = int(input("Enter your current credit score ---->     "))
annual_income = float(input("How much is your annual income ---->  "))
has_collateral = input("Do you have any collateral (True / False)) ---> ")

base_interest_rate = 0.0

if age >= 21 and is_employed:
    print("Applicant pass baseline requirement")
    if credit_score >= 750: #tier1
        print("You have high credit score")
        if annual_income >= 10000 and has_collateral:
            base_interest_rate = 4.5
            print("You meet the income and collateral requirements")
        else:
            base_interest_rate = 5.0
            print("You have a high credit score; your interest rate is", base_interest_rate)
    elif credit_score >= 650: # tier 2
        base_interest_rate = 6.5
        print("Your interest rate is", base_interest_rate)
    else:
        base_interest_rate = 8.0
        print("Your interest rate is", base_interest_rate)
else:
    print("Applicant does not meet the baseline requirements")