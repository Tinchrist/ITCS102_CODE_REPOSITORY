#inputs
age = int(input("AGE"))
monthly_revenue = float(input("REVENUE ---> "))
credit_score = int(input("CREDIT SCORE --> "))
years_in_business = float(input("years IN BUSINESS ---> "))
has_defaults = bool(input("FILE FOR BANKRUPTCY ---> "))
collateral_name = input("COLLATERAL NAME? ---> ")
c_value = float(input("COLLATERAL VALUE ---> "))

#baseline age >=21 , yrs >= 2.0 , False in defaults
max_loan = 0
base_fee = 0

if age >= 21 and years_in_business >= 2.0 and has_defaults == False:
    print("BASELINE PASSED")
    if credit_score >= 720:  # tier1
        max_loan = monthly_revenue * 3
        print("MAXIMUM LOANABLE AMOUNT IS SET TO", max_loan)
        print("HIGH CREDIT SCORE")
        if monthly_revenue >= 50000:
            print("REVENUE HIGHER THAN 50K ")
            base_fee = max_loan * 0.015
            print("BASE FEE RATE IS SET TO", base_fee)
        else:
            print("REVENUE LOWER THAN 50K")
            base_fee = max_loan * 0.025
            print("BASE FEE RATE IS SET TO", base_fee)

        #collateral
        if c_value >= max_loan:
            print("Collateral",collateral_name, "with a value of",c_value, "is ACCEPTED")
        else:
            print("Rejected: INsufficient collateral value for",collateral_name)

        #supercharge
        surge_fee_rate = max_loan * base_fee
        if max_loan % 50000 !=
            print("Additional CHarge added")
            base fee += 250
            print("Updated base fee is",base_fee)
    elif credit_score >= 620 and credit_score < 720: #tier2
        print("Credit Score within range of 620 to 720")
        max_loan = monthly_revenue * 1.5
        print("Maximum loan for this credit score is", max_loan)
        if years_in_business >= 5:
            print("Base fee rate is set to ",base_fee)
        else:
            print("Business year more than 5 years")
            base_fee = max_loan * 0.02
            print("Base fee ratye is set to ",base_fee)

    elif credit_score <620 and credit_score >= 1: #tier 3
        print("Credit Score too low")
    else:
        print("INVALID")
else:
    print("BASELINE FAILED")
