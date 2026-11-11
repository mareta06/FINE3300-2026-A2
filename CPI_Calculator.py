import pandas as pd

#Skip the descriptive rows and read the data into a pandas DataFrame
cpi_data = pd.read_csv("STATIC_INFLATIONCALC.csv", skiprows=8)
#Convert date column into datetime format
cpi_data['date'] = pd.to_datetime(cpi_data['date'])


#Inflation Calculator Class
class InflationCalculator:
    
    def __init__(self):
        self.cpi_data = cpi_data
    
    #Method to retrieve CPI for a specific year
    def get_cpi(self, year):
        #Find the latest month available in the dataset
        latest_month = self.cpi_data['date'].max().month

        #Find CPI for that month and year existing in dataset
        cpi_value = self.cpi_data.loc[
            (self.cpi_data['date'].dt.year == year) & # Select rows matching the user's chosen year
            (self.cpi_data['date'].dt.month == latest_month),'STATIC_INFLATIONCALC'] 
        #Raise error if CPI data is not available for the specified year
        if cpi_value.empty:
            raise ValueError("CPI data is not available for this year.")
        #Return the latest CPI value for the specified year
        return cpi_value.iloc[0]


    #Method to calculate the adjusted cost based on inflation
    def cost_for_inflation(self, amount, original_year, target_year):
        if 1914 <= original_year <= 2026 and 1914 <= target_year <= 2026:
            original_cpi = self.get_cpi(original_year)
            target_cpi = self.get_cpi(target_year)
            return amount * (target_cpi / original_cpi)
        else:
            raise ValueError("Invalid year. Please enter a year between 1914 and 2026.")


    #Method to calculate the percentage change in inflation
    def percentage_for_inflation(self, amount, original_year, target_year):
        return ((self.cost_for_inflation(amount, original_year, target_year) - amount) / amount) * 100

    #Method to calculate the number of years
    def number_of_years(self, original_year, target_year):
        return abs(target_year - original_year)

    #Method to calculate the average annual inflation rate
    def average_annual_inflation(self, original_year, target_year):
        original_cpi = self.get_cpi(original_year)
        target_cpi = self.get_cpi(target_year)
        years = abs(target_year - original_year)
        if years == 0:
            return 0
        return ((target_cpi / original_cpi) ** (1 / years) - 1) * 100



#User Interface for the Inflation Calculator
print("Welcome to the Bank of Canada Inflation Calculator!")
print("This calculator uses the Consumer Price Index (CPI) to determine inflation and adjust the value of money over time between 1914 and 2026.")

print()

print("How to use the calculator:")
print("1. Enter the amount of money you want to adjust.")
print("2. Enter the year of the original amount (1914-2026).")
print("3. Enter the year of the target amount (1914-2026).")

print()


##User Inputs
amount = float(input("Amount of money to adjust: $"))
original_year = int(input("What is the year of the original amount (1914-2026)?: "))
target_year = int(input("What is the year of the target amount (1914-2026)?: "))


#Create an instance of the InflationCalculator class
a = InflationCalculator()


#Perform the calculations
adjusted_cost = a.cost_for_inflation(amount, original_year, target_year)
percentage_change = a.percentage_for_inflation(amount, original_year, target_year)
years = a.number_of_years(original_year, target_year)
average_rate = a.average_annual_inflation(original_year, target_year)
first_cpi = a.get_cpi(original_year)
second_cpi = a.get_cpi(target_year)


#Display the Results
print()
print("INFLATION CALCULATOR RESULTS")
print("----------------------------------")

print(f"Original amount: ${amount:,.2f}")
print(f"Adjusted amount: ${adjusted_cost:,.2f}")
print(f"Percent change: {percentage_change:,.2f}%")
print(f"Number of years: {years}")
print(f"Average annual inflation rate: {average_rate:.2f}%")
print(f"CPI for first year: (Sep {original_year}) {first_cpi:.1f}")
print(f"CPI for second year: (Sep {target_year}) {second_cpi:.1f}")


