# FINE 3300 Assignment 2: Canadian CPI and Inflation Calculator

## Overview

This project was developed using the programming language Python for FINE 3300 Assignment 2. The purpose of this project is to create a Canadian inflation calculator that uses the Consumer Price Index (CPI) to measure changes in the cost of goods and services over time.

The CPI data used in the program is extracted from the Bank of Canada and stored in a CSV file. The program reads this data using the Pandas library and uses it to calculate changes in the purchasing power of money between different years.

The project consists of two Python programs. The first program uses Pandas and Matplotlib to create a graph displaying Canada's CPI and annual percentage change over time. The second program uses a Python class named `InflationCalculator` to calculate the adjusted cost of money, total percentage change, number of years, and average annual inflation rate based on the years entered by the user.

## Project Objectives

The main objectives of this project are to:

- Read monthly CPI data from a CSV file using Pandas.
- Convert the date column into datetime format.
- Calculate the annual percentage change in CPI using `pct_change()`.
- Create a graph displaying CPI and annual percentage change over time.
- Use separate y-axes to display CPI and annual percentage change.
- Include a dotted horizontal line representing the CPI base level of 100.
- Create a Python class named `InflationCalculator`.
- Retrieve CPI values for specific years from the dataset.
- Calculate adjusted costs and percentage changes using CPI values.
- Calculate the number of years and average annual inflation rate.
- Collect user input using Python's `input()` function.
- Display the calculator results with appropriate currency formatting and decimal places.

## Project Files

| File | Description |
|---|---|
| `CPI_Graph.py` | Python program that reads the CPI data and generates the CPI graph. |
| `CPI_Calculator.py` | Python program that implements the Canadian inflation calculator. |
| `STATIC_INFLATIONCALC.csv` | Monthly CPI data provided by the Bank of Canada. |
| `CPI_Graph.png` | Saved graph displaying Canadian CPI and annual percentage change. |
| `README.md` | Project overview, code explanations, CPI graph, commentary, and calculator output. |

---

# Part 1: Canadian CPI Graph

## Reading the CPI Data

I used the Pandas library to read the monthly CPI data from the Bank of Canada CSV file and store it in a DataFrame named `cpi_data`.

The CSV file contains descriptive information before the actual observations, so I used `skiprows=8` to skip the first eight rows and read the data starting from the observation headings.

The `date` column was then converted into datetime format using `pd.to_datetime()`. This allows Python to recognize the dates and extract information such as the year and month.

## Calculating the Annual Percentage Change

To calculate the annual percentage change in CPI, I used the `pct_change()` method with `periods=12`.

Since the dataset contains monthly observations, using 12 periods compares each month's CPI value with the same month from the previous year. The result is then multiplied by 100 to express the change as a percentage.

## Creating the CPI Graph

I used Matplotlib to create a graph displaying Canada's Consumer Price Index and annual percentage change over time.

The CPI is displayed on the left y-axis, while the annual percentage change is displayed on the right y-axis using `twinx()`.

I also included a dotted horizontal line at 100 to represent the CPI base level. Since the dataset uses 2002 as its base year, a CPI value of 100 represents the reference level for that year.

The graph includes a title, axis labels, and a combined legend to identify each line. Finally, I used `plt.savefig()` to save the graph as a PNG file.

## CPI Graph

The following graph displays Canada's Consumer Price Index and annual percentage change over time.

**[INSERT CPI GRAPH IMAGE HERE]**

## CPI Commentary

The graph illustrates the long-term increase in Canada's Consumer Price Index, showing how the overall cost of goods and services has changed over time.

The CPI generally follows an upward trend, indicating that the cost of the typical basket of goods and services has increased over the long term. However, the annual percentage change fluctuates throughout the period, demonstrating that inflation rates vary from year to year.

An important distinction is that the CPI and annual percentage change measure two different things. While the CPI represents the overall price level, the annual percentage change measures how much prices have increased or decreased compared with the same month in the previous year.

---

# Part 2: Canadian Inflation Calculator

## The InflationCalculator Class

I created a class named `InflationCalculator` to organize the functionality of the inflation calculator.

The class uses the CPI data loaded from the Bank of Canada CSV file and contains several methods to retrieve CPI values and perform inflation calculations.

The main methods include `__init__()`, `get_cpi()`, `cost_for_inflation()`, `percentage_for_inflation()`, `number_of_years()`, and `average_annual_inflation()`.

## The __init__ Method

The `__init__()` method initializes the `InflationCalculator` object and stores the CPI DataFrame in the object's `cpi_data` attribute.

This allows the other methods within the class to access the CPI data when performing calculations.

## The get_cpi Method

The `get_cpi()` method retrieves the CPI value for a specific year from the dataset.

Since the dataset contains monthly observations, I used the latest available month to ensure that the calculator compares the same month across different years. The dataset currently ends in September 2026, so the program retrieves September's CPI value for each selected year.

The `.max()` method identifies the latest date in the dataset, while `.month` extracts the month from that date. The program then uses `.loc[]` to find the CPI value matching the selected year and month.

If the CPI value is unavailable, the program raises a `ValueError`.

## The cost_for_inflation Method

The `cost_for_inflation()` method calculates the adjusted cost of an amount based on the CPI values for the original and target years.

The calculation uses the following formula:

**Adjusted Cost = Original Amount × (Target CPI / Original CPI)**

The method also checks whether both years fall within the available dataset, which ranges from 1914 to 2026.

## The percentage_for_inflation Method

The `percentage_for_inflation()` method calculates the total percentage change in the cost of the original amount.

The calculation compares the target CPI with the original CPI to determine the overall percentage increase or decrease in prices.

**Percentage Change = ((Target CPI / Original CPI) - 1) × 100**

## The number_of_years Method

The `number_of_years()` method calculates the number of years between the original year and the target year.

It uses the `abs()` function to return the difference between the two years as a positive number.

## The average_annual_inflation Method

The `average_annual_inflation()` method calculates the average annual inflation rate between the two selected years.

It uses the original and target CPI values to calculate the compound annual rate of change over the selected period.

Unlike the total percentage change, which measures the overall increase in prices, the average annual inflation rate represents the compounded yearly rate over the selected period.

## User Input

After defining the class, I created an object named `a` using the `InflationCalculator` class.

The program displays an introduction and instructions explaining how to use the calculator. Using Python's `input()` function, the user is prompted to enter the amount of money they want to adjust, the original year, and the target year.

These inputs are passed to the appropriate methods within the class to perform the calculations.

The results are displayed using f-strings, with monetary amounts rounded to two decimal places, percentage values displayed to two decimal places, and CPI values displayed to one decimal place.

## Part 2: Program Output

The following output was generated by my Python implementation using an original amount of $100.00 from 1914 and a target year of 2026.

**Input:**

- Original amount: $100.00
- Original year: 1914
- Target year: 2026

**Output:**

```text
Welcome to the Bank of Canada Inflation Calculator!
This calculator uses the Consumer Price Index (CPI) to determine inflation and adjust the value of money over time between 1914 and 2026.

How to use the calculator:
1. Enter the amount of money you want to adjust.
2. Enter the year of the original amount (1914-2026).
3. Enter the year of the target amount (1914-2026).

Amount of money to adjust: $100
What is the year of the original amount (1914-2026)?: 1914
What is the year of the target amount (1914-2026)?: 2026

INFLATION CALCULATOR RESULTS
----------------------------------
Original amount: $100.00
Adjusted amount: $2,833.33
Percent change: 2,733.33%
Number of years: 112
Average annual inflation rate: 3.03%
CPI for first year: (Sep 1914) 6.0
CPI for second year: (Sep 2026) 170.0
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

   `python CPI_Graph.py`

5. The program will generate and display the CPI graph and save it as `CPI_Graph.png`.

## Running the Inflation Calculator

1. Open the project folder in Visual Studio Code.
2. Open the terminal.
3. Run the inflation calculator:

   `python CPI_Calculator.py`

4. Enter the monetary amount, original year, and target year when prompted.
5. The calculator will display the adjusted amount and other inflation results.

Make sure the CSV file is located in the directory expected by the Python programs.

---

# Conclusion

In conclusion, this project demonstrates the implementation of Python concepts learned in FINE 3300 to analyze Canadian inflation using Consumer Price Index data from the Bank of Canada.

The first program uses Pandas to read and analyze monthly CPI observations and Matplotlib to visualize changes in CPI and annual inflation over time. The second program uses an object-oriented approach through the `InflationCalculator` class to retrieve CPI values and calculate the adjusted value of money between different years.

Together, these programs demonstrate how Python can be used to organize financial data, perform calculations, and present meaningful information about changes in purchasing power and the cost of living in Canada.
