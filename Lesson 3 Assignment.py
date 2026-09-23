investment_amount = int(input("Enter an investment amount (Greater than 0 and less than 50,000): "))

while investment_amount <= 0 or investment_amount >= 50000:
    print("Invalid amount. Investment must be greater than 0 and less than 50,000.")
    investment_amount = int(input("Please enter a valid investment amount: "))

interest_rate = int(input("Enter an interest rate (Greater than 0 and less than 15): "))

while interest_rate <= 0 or interest_rate >= 15:
    print("Invalid rate. Interest rate must be greater than 0 and less than 15.")
    interest_rate = int(input("Please enter a valid interest rate: "))

duration_years = int(input("Enter the investment duration in years (Greater than 0): "))

while duration_years <= 0:
    print("Invalid duration. Duration must be greater than 0.")
    duration_years = int(input("Please enter a valid investment duration in years: "))

total_months = duration_years * 12
monthly_interest_rate = (interest_rate / 12) / 100

future_total = 0.0

print("\n--- Yearly Progress Report ---")

for current_month in range(1, total_months + 1):
    future_total += investment_amount
    
    monthly_interest = round(future_total * monthly_interest_rate, 2)
    future_total += monthly_interest

    if current_month % 12 == 0:
        current_year = current_month // 12
        print("Year " + str(current_year) + ": $" + str(round(future_total, 2)))

print("\n--- Investment Summary ---")
print("Years Calculated: " + str(duration_years))
print("Yearly Interest Rate: " + str(interest_rate) + "%")
print("Monthly Investment Amount: $" + str(round(float(investment_amount), 2)))
print("Total Portfolio Value: $" + str(round(future_total, 2)))

print("Completed by Lincoln Reeves.")

keep_open = input("Graggle ")
