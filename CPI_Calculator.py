import pandas as pd

#Skip the descriptive rows and read the data into a pandas DataFrame
cpi_data = pd.read_csv("STATIC_INFLATIONCALC.csv", skiprows=8)

#Convert date column into datetime format
cpi_data['date'] = pd.to_datetime(cpi_data['date'])


#Inflation Calculator Class
class InflationCalculator:

    def __init__(self):
        self.cpi_data = cpi_data

    #Method to retrieve CPI for a specific month and year
    def get_cpi(self, date):

        #Extract the month and year from the date
        month = date.month
        year = date.year

        #Find CPI for the selected month and year in the dataset
        cpi_value = self.cpi_data.loc[
            (self.cpi_data['date'].dt.year == year) &  #Select the rows where the year matches the year entered by the user
            (self.cpi_data['date'].dt.month == month),'STATIC_INFLATIONCALC'] #Ensure the month matches the month entered by the user

        #Raise an error if CPI data is not available for the specified date
        if cpi_value.empty:
            raise ValueError("CPI data is not available for this date.")
        #Return the CPI value
        return cpi_value.iloc[0]

    #Method to calculate the adjusted cost based on inflation
    def cost_for_inflation(self, amount, original_date, target_date):
        #Retrieve CPI values for both dates
        original_cpi = self.get_cpi(original_date)
        target_cpi = self.get_cpi(target_date)
        #Calculate the adjusted cost
        return amount * (target_cpi / original_cpi)

    #Method to calculate the percentage change in inflation
    def percentage_for_inflation(self, amount, original_date, target_date):
        adjusted_cost = self.cost_for_inflation(amount, original_date, target_date)
        return ((adjusted_cost - amount) / amount) * 100

    #Method to calculate the number of years and months in difference
    def number_of_years(self, original_date, target_date):
        #Calculate the total difference in months
        months = abs((target_date.year - original_date.year) * 12 + (target_date.month - original_date.month))
        #Convert total months into years and remaining months
        years = months // 12
        remaining_months = months % 12
        return years, remaining_months

   #Method to calculate the average annual inflation rate
    def average_annual_inflation(self, original_date, target_date):
        original_cpi = self.get_cpi(original_date)
        target_cpi = self.get_cpi(target_date)
        #Calculate the difference in years and months
        years, months = self.number_of_years(original_date, target_date)
        #Convert the difference into decimal years
        total_years = years + (months / 12)
        if total_years == 0:
            return 0
        return ((target_cpi / original_cpi) ** (1 / total_years) - 1) * 100

#User Interface for the Inflation Calculator
print("Welcome to the Bank of Canada Inflation Calculator!")
print("This calculator uses the Consumer Price Index (CPI) to determine inflation and adjust the value of money over time betweenvJanuary 1914- September 2026.")

print()

print("How to use the calculator:")
print("1. Enter the amount of money you want to adjust.")
print("2. Enter the original date (e.g., December 1914).")
print("3. Enter the target date (e.g., October 2020).")

print()


#User Input for amount and validate it
try:
    amount = float(input("Amount of money to adjust (CAD): $"))
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
except ValueError:
    raise ValueError("Please enter a valid positive numerical amount.")

#User Input for dates 
original_input = input("Enter the original date (Month Year): ")
target_input = input("Enter the target date (Month Year): ")

#Convert user inputs into datetime format and validate it
try:
    original_date = pd.to_datetime(original_input, format="%B %Y")
    target_date = pd.to_datetime(target_input, format="%B %Y")
except ValueError:
    raise ValueError("Invalid date format. Please use Month Year (e.g., December 1914).")

#Create an instance of the InflationCalculator class
a = InflationCalculator()

#Perform the calculations
adjusted_cost = a.cost_for_inflation(amount, original_date, target_date)
percentage_change = a.percentage_for_inflation(amount, original_date, target_date)
years, months = a.number_of_years(original_date, target_date)
average_rate = a.average_annual_inflation(original_date, target_date)
first_cpi = a.get_cpi(original_date)
second_cpi = a.get_cpi(target_date)

#Display the Results
print()
print("ENHANCED INFLATION CALCULATOR RESULTS")
print(50 * "-")

print(f"Original amount (CAD): ${amount:,.2f}")
print(f"Adjusted amount (CAD): ${adjusted_cost:,.2f}")
print(f"Percent change: {percentage_change:,.2f}%")
print(f"Number of years and months: {years} years and {months} months")
print(f"Average annual inflation rate: {average_rate:.2f}%")
print(f"CPI for first period: ({original_date.strftime('%B %Y')}) {first_cpi:.1f}")
print(f"CPI for second period: ({target_date.strftime('%B %Y')}) {second_cpi:.1f}")