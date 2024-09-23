import os

EXPENSE_FILE = "expenses.txt" #declaring a file for storing the expenses

def add_expenses(): #function to add expenses
    date = input("Enter the date (DD-MM-YYYY): ")
    category =  input("Enter the category (e.g Food, Travel, Entertainment) :  ") 
    description = input("Enter the description: ")
    amount = float(input("Enter the amount: "))

    expense = f"{date}, {category}, {description}, {amount}\n"

    with open(EXPENSE_FILE, 'a') as file:
        file.write(expense)


    print("Expense added successfully")


def view_expense(): #function to view all the expenses

    if not os.path.exists(EXPENSE_FILE):
        print("No expenses found")
        return

    
    with open(EXPENSE_FILE, 'r') as file:
        print(f"Date          |Category         |Description          |Amount")
        print("-" *65)

        for line in file:
            date,  category, description, amount = line.strip().split(",")
            print(f"{date}    |{category:10}       |{description:15}      |Rs.{amount} ")



def view_expenses_by_category(): #function to view the specific expense based on category

    if not os.path.exists(EXPENSE_FILE):
        print("No expenses found")
        return

    category_filter= input("Enter the category to filter by : ").lower()
    total = 0.0

    with open(EXPENSE_FILE, 'r') as file:
        print(f"Date          |Category         |Description          |Amount")
        print("-" *65)

        for line in file:
            date, category, description, amount = [field.strip() for field in line.split(",")]  #field.strip() inside a list comprehension to remove any extra spaces around the fields.
            category = category.lower()
            if(category.lower() == category_filter):
                print(f"{date}    |{category:10}       |{description:15}      |Rs.{amount} ")
                total+= float(amount) #storing the total expenses of that category


    print(f"\nTotal spent on {category_filter.capitalize()}: Rs.{total}")


def delete_expense(): #function to delete a record based on description
    if not os.path.exists(EXPENSE_FILE):
        print("No expenses found.")
        return

    search_term = input("Enter the description of the expense to delete: ").lower()
    expenses = []

    with open(EXPENSE_FILE, 'r') as file:
        expenses = file.readlines()

    updated_expenses = []
    deleted = False

    for line in expenses:
        date, category, description, amount = [field.strip() for field in line.split(",")]
        if search_term in description.lower():
            print(f"Deleting expense: {date} | {category} | {description} | Rs.{amount}")
            deleted = True
        else:
            updated_expenses.append(line)

    if deleted:
        with open(EXPENSE_FILE, 'w') as file:
            file.writelines(updated_expenses)
        print("Expense deleted successfully.")
    else:
        print("No matching description found.")




def main(): #defining a menu driven program for the ease of users
    while True:
        print("\n","*"*20,"Personal Expense Tracker","*"*20,"\n")
        print("1. Add Expense")
        print("2. View all expenses")
        print("3. View expense by category")
        print("4. Delete expense by description")
        print("5. Exit")

        choice = input("Choose an option(1-5): ")

        if choice == "1":
            add_expenses()
        elif choice == "2":
            view_expense()
        elif choice == "3":
            view_expenses_by_category()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            print("Exiting the Expense Tracker..Have a great day!!!")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 4")
            
            
        
main()
    
            














        

    
        
