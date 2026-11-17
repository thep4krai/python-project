# Retail Customer Analyzer – Project Summary

**PS No. 83**

- **Name:** Deepak Kumar Rai
- **Enrollment No:** RU-26-01558

## Introduction
The Retail Customer Analyzer is a menu-driven Python 3 program that reads customer data from a CSV file using the Pandas library. It helps a shop owner quickly understand how much customers spend, who the best customers are, and which city brings the most business.

## Problem Statement
Read `customers.csv` with Pandas. Show the mean, median, highest and lowest spending, list customers who spent at least a limit entered by the user, and show city-wise total and average spending. The data has 5 columns (CustomerID, Name, City, Purchases, TotalSpent) and 8 rows.

## Features
| Feature | What it does |
|---|---|
| Spending statistics | Shows mean, median, highest and lowest TotalSpent along with customer names |
| High-value customers | The user enters a limit; the program lists every customer whose TotalSpent is at least that limit |
| City-wise summary | Groups customers by city and shows total and average spending of each city |
| Error handling | Shows a message for a missing file, text input or a negative amount instead of crashing |

## How It Works
1. The program loads `customers.csv` using Pandas.
2. A menu with four options is shown.
3. The user types 1, 2, 3 or 4.
4. The program prints the result and returns to the menu until the user chooses Exit.

## Concepts Used
Python 3, Pandas (`read_csv`, `mean`, `median`, `idxmax`, `idxmin`), filtering with conditions, grouping with `groupby`, functions, `while` loop, `if/elif/else`, and `try/except` for error handling.

## Test Cases
| Test | Input | Result |
|---|---|---|
| 1. Normal | Spending statistics | Mean 9125.0, Median 7500.0, Highest Chitra (25000), Lowest Deepak (800) |
| 2. Boundary | High-value customers, limit 25000 | 1 customer: C03 \| Chitra \| Raipur \| 25000 |
| 3. Invalid | Limit `abc` and limit `-500` | Invalid amount. Please enter a number. / Amount must be 0 or more. |
| 4. Different valid | City-wise summary | Raipur 43000 (avg 14333.33), Bhilai 15800 (avg 7900.0), Durg 14200 (avg 4733.33) |

## Conclusion
This project helped me learn how to read CSV files with Pandas, filter and group data, and handle errors in a Python program. The Retail Customer Analyzer turns raw customer data into useful information in a few seconds.
