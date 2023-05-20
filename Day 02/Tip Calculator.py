#DAY 2 PROJECT : TIP CALCULATOR (SUMITH SAI KORABOINA)

print('Welcome to the tip calculator')
tot_bill=(input("What was the total bill: "))
tip_percent=(input('What percentage tip would you like to give? 10 or 12 or 15 ? '))
split=(input('How many people would like to split the bill? '))
Individual_bill=float(float(tot_bill)/int(split)) * ((float(tip_percent)/100)+1)
bill_to_pay=(round(Individual_bill,2))
#bill_to_pay={":.2f".format(Individual_bill)}
print(f"Bill to be paid by every individual is ${bill_to_pay}")