# Project: Retail Customer Analyzer (PS No. 83)
# Language: Python 3
# Concepts: Pandas, Filtering, Grouping, Statistics

import pandas as pd


def load_data():
    # try to read the csv file, if file is missing show a message
    try:
        data = pd.read_csv("customers.csv")
        return data
    except FileNotFoundError:
        print("Error: customers.csv file not found.")
        print("Please keep customers.csv in the same folder as this program.")
        return None


def show_statistics(data):
    # calculate mean, median, highest and lowest of TotalSpent
    mean_spend = data["TotalSpent"].mean()
    median_spend = data["TotalSpent"].median()

    # idxmax() gives the row number of the highest value
    # idxmin() gives the row number of the lowest value
    highest_row = data["TotalSpent"].idxmax()
    lowest_row = data["TotalSpent"].idxmin()

    highest_name = data.loc[highest_row, "Name"]
    highest_amount = data.loc[highest_row, "TotalSpent"]
    lowest_name = data.loc[lowest_row, "Name"]
    lowest_amount = data.loc[lowest_row, "TotalSpent"]

    print("\n--- Spending Statistics ---")
    print("Mean spend: Rs.", round(mean_spend, 2))
    print("Median spend: Rs.", round(median_spend, 2))
    print("Highest:", highest_name, "(Rs.", highest_amount, ")")
    print("Lowest:", lowest_name, "(Rs.", lowest_amount, ")")


def show_high_value_customers(data):
    # ask the user for a limit
    limit_text = input("Enter the limit amount: ")

    # check if the user entered a number
    try:
        limit = float(limit_text)
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    # negative amount is not allowed
    if limit < 0:
        print("Amount must be 0 or more.")
        return

    # filter customers whose TotalSpent is greater than or equal to limit
    high_customers = data[data["TotalSpent"] >= limit]

    print("\nHigh-value customers (TotalSpent >=", limit_text + "):", len(high_customers))

    # go through each filtered row and print it
    for index, row in high_customers.iterrows():
        print(row["CustomerID"], "|", row["Name"], "|", row["City"], "| Rs.", row["TotalSpent"])


def show_city_summary(data):
    # group the data by city, then find total and average of TotalSpent
    city_data = data.groupby("City")["TotalSpent"].agg(["sum", "mean"])

    # show the city with the highest total first
    city_data = city_data.sort_values("sum", ascending=False)

    print("\n--- City-wise Summary ---")
    for city, row in city_data.iterrows():
        print(city, ": Total Rs.", round(row["sum"], 2), "| Average Rs.", round(row["mean"], 2))


def main():
    data = load_data()

    # if file was not found, stop the program
    if data is None:
        return

    # menu keeps running until user chooses exit
    while True:
        print("\n===== Retail Customer Analyzer =====")
        print("1. Spending statistics")
        print("2. High-value customers")
        print("3. City-wise summary")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_statistics(data)
        elif choice == "2":
            show_high_value_customers(data)
        elif choice == "3":
            show_city_summary(data)
        elif choice == "4":
            print("Thank you! Program closed.")
            break
        else:
            print("Wrong choice. Please enter a number from 1 to 4.")


main()