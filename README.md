# FINE 3300 Assignment 2: Canadian CPI and Inflation Calculator

## Overview
This project was developed using the programming language Python for FINE 3300 Assignment 2. The objective is to create a Canadian inflation calculator using the Consumer Price Index (CPI) to track changes in the cost of goods and services over time and visualize these changes in a graph.

The CPI data used in this project is obtained from the Bank of Canada and stored in a CSV file. The program uses Pandas to read and analyze monthly CPI observations covering January 1914 to September 2026.

The project consists of two Python programs. The first uses Pandas and Matplotlib to generate a graph displaying Canada's CPI and annual percentage change over time. The second uses a Python class named `InflationCalculator` to calculate adjusted costs, total percentage changes, the time difference in years and months, and the average annual inflation rate based on the dates entered by the user.

## Project Objectives

The main objectives of this project are to:

- Read monthly CPI data from a CSV file using Pandas.
- Convert the date column into datetime format.
- Calculate the annual percentage change in CPI using monthly observations.
- Create a graph displaying CPI and annual percentage change over time.
- Use separate y-axes to display CPI and annual percentage change.
- Include a dotted horizontal line representing the CPI base level of 100.
- Create a Python class named `InflationCalculator`.
- Retrieve CPI values for specific months and years from the dataset.
- Calculate adjusted costs and percentage changes using CPI values.
- Calculate the number of years and remaining months between two dates.
- Calculate the average annual inflation rate.
- Collect and validate user input.
- Display calculator results with appropriate currency formatting and decimal places.

## Project Files

| File | Description |
|---|---|
| `CPI_Annual Percentage Change_Graph.py` | Python program that reads the CPI data and generates the CPI and annual percentage change graph. |
| `Inflation_Calculator.py` | Python program that implements the enhanced Canadian inflation calculator. |
| `STATIC_INFLATIONCALC.csv` | Monthly CPI data from January 1914 to September 2026, obtained from the Bank of Canada. |
| `CPI_Annual Percentage Change_Graph.png` | Saved graph displaying Canadian CPI and annual percentage change. |
| `README.md` | Project overview, program explanations, graph commentary, and sample calculator output. |

---

# Part 1: Canadian CPI & Annual Percentage Change Graph

## Reading the CPI Data

I used the Pandas library to read the monthly CPI data from the Bank of Canada CSV file and store it in a DataFrame named `cpi_data`.

The CSV file contains descriptive information before the actual observations, so I used `skiprows=8` to skip the first eight rows and read the data starting from the observation headings.

The `date` column was then converted into datetime format using `pd.to_datetime()`. This allows Python to recognize the dates and extract information such as the year and month.

## Calculating the Annual Percentage Change

To calculate the annual percentage change in CPI, I used the `pct_change()` method with `periods=12`.

Since the dataset contains monthly observations, using 12 periods compares each month's CPI value with the same month from the previous year. The result is then multiplied by 100 to express the change as a percentage.

## Creating the Graph

I used Matplotlib to create a graph displaying Canada's Consumer Price Index and annual percentage change over time.

The CPI is displayed on the left y-axis, while the annual percentage change is displayed on the right y-axis using the `twinx()` method. This allows both measures to be displayed on the same graph with different scales.

I also included a dotted horizontal line at 100 to represent the CPI base level. Since the dataset uses 2002 as its base year, a CPI value of 100 represents the reference level for that year.

The graph includes a title, axis labels, and a combined legend in the bottom-right corner to identify each line. Finally, I used `plt.savefig()` to save the graph as a PNG file.

## CPI & Annual Percentage Change Graph Image

The following graph displays Canada's Consumer Price Index and annual percentage change over time.

<img width="1747" height="995" alt="image" src="https://github.com/user-attachments/assets/ea5b5460-9e2c-44b8-9d24-3ea4ad256a25" />


## Graph Commentary

The graph illustrates the long-term increase in Canada's Consumer Price Index, showing how the overall cost of goods and services has changed between 1914 and 2026.

The Canadian CPI (blue line) shows an overall upward trend, meaning the cost of a typical basket of goods and services has increased over the long term. However, the annual percentage change (orange line) fluctuates throughout the period, demonstrating that inflation rates vary over time.

It is important to note that the CPI and annual percentage change measure two different things. The CPI measures the overall level of prices, while the annual percentage change measures how prices have changed compared with the same month in the previous year.

---

# Part 2: Canadian Inflation Calculator

## The InflationCalculator Class

I created a class named `InflationCalculator` to organize the several functions of the inflation calculator.

The class uses CPI data loaded from the Bank of Canada CSV file and includes methods to retrieve CPI values and perform inflation calculations.

The main methods include `__init__()`, `get_cpi()`, `cost_for_inflation()`, `percentage_for_inflation()`, `number_of_years()`, and `average_annual_inflation()`.

## The __init__ Method

The `__init__()` method initializes the `InflationCalculator` object and stores the CPI DataFrame in the object's `cpi_data` attribute.

This allows the other methods within the class to access the CPI data when performing calculations.

## The get_cpi Method

The `get_cpi()` method retrieves the CPI value for a specific month and year from the dataset.

Since the dataset contains monthly observations, the method extracts the month and year from the date the user enters. It then uses `.loc[]` to find the CPI value that matches both the selected month and year.

If CPI data is unavailable for the selected date, the program raises a `ValueError`.

## The cost_for_inflation Method

The `cost_for_inflation()` method calculates the adjusted cost of an amount based on the CPI values for the original and target dates.

The calculation uses the following formula:

**Adjusted Cost = Original Amount × (Target CPI / Original CPI)**

The method retrieves the CPI values for both selected dates using the `get_cpi()` method before calculating the adjusted cost.

## The percentage_for_inflation Method

The `percentage_for_inflation()` method calculates the total percentage change in the cost of the original amount.

The calculation uses the following formula:

**Percentage Change = ((Adjusted Cost - Original Amount) / Original Amount) × 100**

## The number_of_years Method

The `number_of_years()` method calculates the total time difference between the original and target dates.

Since the calculator uses monthly CPI observations, the method calculates the total difference in months and converts it into years and remaining months.

For example, a difference of 112 years and 8 months is displayed in the output rather than rounding to 113 years.

## The average_annual_inflation Method

The `average_annual_inflation()` method calculates the average annual inflation rate between the two selected dates.

It uses the original and target CPI values to calculate the compound annual rate of change over the selected period.

The time difference is converted to decimal years to account for both complete years and remaining months.

The average annual inflation rate is the compounded annual change over the selected time period. This differs from the total percentage change, which is the overall change in prices.

## User Input and Validation

After defining the class, I created an object named `a` using the `InflationCalculator` class.

The program displays an introduction and instructions explaining how to use the calculator. Using Python's `input()` function, the user is prompted to enter:

1. The amount of money they want to adjust in Canadian dollars (CAD).
2. The original date in Month Year format (e.g., December 1914).
3. The target date in Month Year format (e.g., October 2020).

The amount entered by the user is converted to a float using `float()`. The program also checks that the amount is greater than zero and raises a `ValueError` if an invalid amount is entered.

The dates are converted into datetime format using `pd.to_datetime()`. A `ValueError` is raised if the dates are not entered in the required format.

The program then uses the selected dates to retrieve the corresponding CPI values and perform the inflation calculations.

The results are displayed using f-strings, with monetary amounts rounded to two decimal places, percentage values displayed to two decimal places, and CPI values displayed to one decimal place.

## Part 2: Program Output

The following output was generated by my Python implementation using an original amount of $100.00 CAD, an original date of January 1914, and a target date of September 2026.

**Input:**

- Original amount: $100.00 CAD
- Original date: January 1914
- Target date: September 2026

**Output:**

```text
Welcome to the Bank of Canada Inflation Calculator!
This calculator uses the Consumer Price Index (CPI) to calculate inflation and adjust the value of money between January 1914 and September 2026.

How to use the calculator:
1. Enter the amount of money you want to adjust.
2. Enter the original date (e.g., December 1914).
3. Enter the target date (e.g., October 2020).

Amount of money to adjust (CAD): $100
Enter the original date (Month Year): January 1914
Enter the target date (Month Year): September 2026

ENHANCED INFLATION CALCULATOR RESULTS
--------------------------------------------------

Original amount (CAD): $100.00
Adjusted amount (CAD): $2,833.33
Percent change: 2,733.33%
Number of years and months: 112 years and 8 months
Average annual inflation rate: 3.01%
CPI for first period: (January 1914) 6.0
CPI for second period: (September 2026) 170.0
```

---

# How to Run the Programs

## Requirements

To run the programs, you need:

- Python installed on your computer.
- The Python files and the Bank of Canada CPI CSV file.
- The Pandas library.
- The Matplotlib library.
- A Python development environment, such as Visual Studio Code.

Install the required libraries using:

`pip install pandas matplotlib`

## Running the CPI Graph Program

1. Download or clone this repository.
2. Open the project folder in Visual Studio Code.
3. Open the terminal.
4. Run the CPI graph program:

   `python "CPI_Annual Percentage Change_Graph.py"`

5. The program will generate and display the CPI graph and save it as a PNG file.

## Running the Inflation Calculator

1. Open the project folder in Visual Studio Code.
2. Open the terminal.
3. Run the inflation calculator:

   `python Inflation_Calculator.py`

4. Enter the monetary amount, original date, and target date when prompted.
5. The calculator will display the adjusted amount and other inflation results.

Make sure the CSV file is located in the same directory as the Python programs, or update the file path in the code accordingly.

---

# Conclusion

In conclusion, this project utilizes the Python concepts learned in FINE 3300 to analyze Canadian inflation using the Consumer Price Index data from the Bank of Canada.

The first program uses Pandas to read and analyze monthly CPI observations and uses Matplotlib to visualize the changes in CPI and annual percentage change over time. The second program uses an object-oriented approach with the `InflationCalculator` class to retrieve CPI values for specific months and years and calculate the adjusted value of money between dates.

Together, these programs show how Python can be used to organize financial data, perform calculations, and present meaningful information about changes in purchasing power and the cost of living in Canada.
