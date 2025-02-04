import pymysql
import pandas as pd
import tkinter as tk
from tkinter import messagebox, ttk

# Database connection
def connect_db():
    return pymysql.connect(host="localhost", user="root", passwd="password", database="BankingSystem")

# SQL Queries to create tables if not exist
def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    # Customer Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Customer (
        CustomerID INT PRIMARY KEY,
        Name VARCHAR(100),
        Phone VARCHAR(15),
        Email VARCHAR(100),
        Address VARCHAR(255),
        DateOfBirth DATE
    );
    """)

    # Branch Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Branch (
        BranchID INT PRIMARY KEY,
        BranchName VARCHAR(100),
        Address VARCHAR(255),
        Phone VARCHAR(15)
    );
    """)

    # Account Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Account (
        AccountID INT PRIMARY KEY,
        CustomerID INT,
        BranchID INT,
        AccountType VARCHAR(50),
        Balance DECIMAL(15, 2),
        OpeningDate DATE,
        FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
        FOREIGN KEY (BranchID) REFERENCES Branch(BranchID)
    );
    """)

    # Employee Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Employee (
        EmployeeID INT PRIMARY KEY,
        BranchID INT,
        Name VARCHAR(100),
        Role VARCHAR(50),
        Salary DECIMAL(10, 2),
        HireDate DATE,
        FOREIGN KEY (BranchID) REFERENCES Branch(BranchID)
    );
    """)

    # Transaction Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Transaction (
        TransactionID INT PRIMARY KEY,
        AccountID INT,
        TransactionType VARCHAR(50),
        Amount DECIMAL(15, 2),
        TransactionDate DATE,
        FOREIGN KEY (AccountID) REFERENCES Account(AccountID)
    );
    """)

    # Loan Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Loan (
        LoanID INT PRIMARY KEY,
        CustomerID INT,
        AccountID INT,
        LoanAmount DECIMAL(15, 2),
        InterestRate DECIMAL(5, 2),
        StartDate DATE,
        EndDate DATE,
        FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
        FOREIGN KEY (AccountID) REFERENCES Account(AccountID)
    );
    """)

    conn.commit()
    conn.close()

# Main Application Class
class BankingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Banking Management System")
        self.root.geometry("800x600")

        # Create tables in the database
        create_tables()

        # Main Menu
        self.main_menu()

    def main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Welcome to Banking Management System", font=("Arial", 16)).pack(pady=20)

        tk.Button(self.root, text="Customer", command=self.customer_menu, width=20).pack(pady=10)
        tk.Button(self.root, text="Branch", command=self.branch_menu, width=20).pack(pady=10)
        tk.Button(self.root, text="Account", command=self.account_menu, width=20).pack(pady=10)
        tk.Button(self.root, text="Employee", command=self.employee_menu, width=20).pack(pady=10)
        tk.Button(self.root, text="Transactions", command=self.transaction_menu, width=20).pack(pady=10)
        tk.Button(self.root, text="Loan", command=self.loan_menu, width=20).pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit, width=20).pack(pady=10)

    # Customer Menu
    def customer_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Button(self.root, text="Show Customers", command=self.show_customers, width=20).pack(pady=10)
        tk.Button(self.root, text="Add Customer", command=self.add_customer, width=20).pack(pady=10)
        tk.Button(self.root, text="Search Customer", command=self.search_customer, width=20).pack(pady=10)
        tk.Button(self.root, text="Delete Customer", command=self.delete_customer, width=20).pack(pady=10)
        tk.Button(self.root, text="Update Customer", command=self.update_customer, width=20).pack(pady=10)
        tk.Button(self.root, text="Back to Main Menu", command=self.main_menu, width=20).pack(pady=10)

    def show_customers(self):
        conn = connect_db()
        df = pd.read_sql("SELECT * FROM Customer", conn)
        conn.close()
        self.display_dataframe(df)

    def add_customer(self):
        self.data_entry_window("Add Customer", ["CustomerID", "Name", "Phone", "Email", "Address", "DateOfBirth"], self.save_customer)

    def save_customer(self, data):
        conn = connect_db()
        cursor = conn.cursor()
        query = "INSERT INTO Customer (CustomerID, Name, Phone, Email, Address, DateOfBirth) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, data)
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Customer added successfully")

    def search_customer(self):
        self.search_window("Search Customer", "CustomerID", self.show_customer_result)

    def show_customer_result(self, customer_id):
        conn = connect_db()
        df = pd.read_sql(f"SELECT * FROM Customer WHERE CustomerID = {customer_id}", conn)
        conn.close()
        self.display_dataframe(df)

    def delete_customer(self):
        self.search_window("Delete Customer", "CustomerID", self.delete_customer_record)

    def delete_customer_record(self, customer_id):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM Customer WHERE CustomerID = {customer_id}")
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Customer deleted successfully")

    def update_customer(self):
        self.search_window("Update Customer", "CustomerID", self.update_customer_record)

    def update_customer_record(self, customer_id):
        conn = connect_db()
        df = pd.read_sql(f"SELECT * FROM Customer WHERE CustomerID = {customer_id}", conn)
        conn.close()
        if not df.empty:
            self.data_entry_window("Update Customer", ["Name", "Phone", "Email", "Address", "DateOfBirth"], lambda data: self.save_customer_update(customer_id, data), df.iloc[0].tolist()[1:])
        else:
            messagebox.showinfo("Error", "Customer not found")

    def save_customer_update(self, customer_id, data):
        conn = connect_db()
        cursor = conn.cursor()
        query = "UPDATE Customer SET Name = %s, Phone = %s, Email = %s, Address = %s, DateOfBirth = %s WHERE CustomerID = %s"
        cursor.execute(query, data + [customer_id])
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Customer updated successfully")

    # Branch Menu
    def branch_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Button(self.root, text="Show Branches", command=self.show_branches, width=20).pack(pady=10)
        tk.Button(self.root, text="Add Branch", command=self.add_branch, width=20).pack(pady=10)
        tk.Button(self.root, text="Search Branch", command=self.search_branch, width=20).pack(pady=10)
        tk.Button(self.root, text="Delete Branch", command=self.delete_branch, width=20).pack(pady=10)
        tk.Button(self.root, text="Update Branch", command=self.update_branch, width=20).pack(pady=10)
        tk.Button(self.root, text="Back to Main Menu", command=self.main_menu, width=20).pack(pady=10)

    def show_branches(self):
        conn = connect_db()
        df = pd.read_sql("SELECT * FROM Branch", conn)
        conn.close()
        self.display_dataframe(df)

    def add_branch(self):
        self.data_entry_window("Add Branch", ["BranchID", "BranchName", "Address", "Phone"], self.save_branch)

    def save_branch(self, data):
        conn = connect_db()
        cursor = conn.cursor()
        query = "INSERT INTO Branch (BranchID, BranchName, Address, Phone) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, data)
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Branch added successfully")

    def search_branch(self):
        self.search_window("Search Branch", "BranchID", self.show_branch_result)

    def show_branch_result(self, branch_id):
        conn = connect_db()
        df = pd.read_sql(f"SELECT * FROM Branch WHERE BranchID = {branch_id}", conn)
        conn.close()
        self.display_dataframe(df)

    def delete_branch(self):
        self.search_window("Delete Branch", "BranchID", self.delete_branch_record)

    def delete_branch_record(self, branch_id):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM Branch WHERE BranchID = {branch_id}")
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Branch deleted successfully")

    def update_branch(self):
        self.search_window("Update Branch", "BranchID", self.update_branch_record)

    def update_branch_record(self, branch_id):
        conn = connect_db()
        df = pd.read_sql(f"SELECT * FROM Branch WHERE BranchID = {branch_id}", conn)
        conn.close()
        if not df.empty:
            self.data_entry_window("Update Branch", ["BranchName", "Address", "Phone"], lambda data: self.save_branch_update(branch_id, data), df.iloc[0].tolist()[1:])
        else:
            messagebox.showinfo("Error", "Branch not found")

    def save_branch_update(self, branch_id, data):
        conn = connect_db()
        cursor = conn.cursor()
        query = "UPDATE Branch SET BranchName = %s, Address = %s, Phone = %s WHERE BranchID = %s"
        cursor.execute(query, data + [branch_id])
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Branch updated successfully")

    # Account Menu
    def account_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Button(self.root, text="Show Accounts", command=self.show_accounts, width=20).pack(pady=10)
        tk.Button(self.root, text="Add Account", command=self.add_account, width=20).pack(pady=10)
        tk.Button(self.root, text="Search Account", command=self.search_account, width=20).pack(pady=10)
        tk.Button(self.root, text="Delete Account", command=self.delete_account, width=20).pack(pady=10)
        tk.Button(self.root, text="Update Account", command=self.update_account, width=20).pack(pady=10)
        tk.Button(self.root, text="Back to Main Menu", command=self.main_menu, width=20).pack(pady=10)

    def show_accounts(self):
        conn = connect_db()
        df = pd.read_sql("SELECT * FROM Account", conn)
        conn.close()
        self.display_dataframe(df)

    def add_account(self):
        self.data_entry_window("Add Account", ["AccountID", "CustomerID", "BranchID", "AccountType", "Balance", "OpeningDate"], self.save_account)

    def save_account(self, data):
        conn = connect_db()
        cursor = conn.cursor()
        query = "INSERT INTO Account (AccountID, CustomerID, BranchID, AccountType, Balance, OpeningDate) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, data)
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Account added successfully")

    def search_account(self):
        self.search_window("Search Account", "AccountID", self.show_account_result)

    def show_account_result(self, account_id):
        conn = connect_db()
        df = pd.read_sql(f"SELECT * FROM Account WHERE AccountID = {account_id}", conn)
        conn.close()
        self.display_dataframe(df)

    def delete_account(self):
        self.search_window("Delete Account", "AccountID", self.delete_account_record)

    def delete_account_record(self, account_id):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM Account WHERE AccountID = {account_id}")
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Account deleted successfully")

    def update_account(self):
        self.search_window("Update Account", "AccountID", self.update_account_record)

    def update_account_record(self, account_id):
        conn = connect_db()
        df = pd.read_sql(f"SELECT * FROM Account WHERE AccountID = {account_id}", conn)
        conn.close()
        if not df.empty:
            self.data_entry_window("Update Account", ["CustomerID", "BranchID", "AccountType", "Balance", "OpeningDate"], lambda data: self.save_account_update(account_id, data), df.iloc[0].tolist()[1:])
        else:
            messagebox.showinfo("Error", "Account not found")

    def save_account_update(self, account_id, data):
        conn = connect_db()
        cursor = conn.cursor()
        query = "UPDATE Account SET CustomerID = %s, BranchID = %s, AccountType = %s, Balance = %s, OpeningDate = %s WHERE AccountID = %s"
        cursor.execute(query, data + [account_id])
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Account updated successfully")

    # Employee Menu
    def employee_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Button(self.root, text="Show Employees", command=self.show_employees, width=20).pack(pady=10)
        tk.Button(self.root, text="Add Employee", command=self.add_employee, width=20).pack(pady=10)
        tk.Button(self.root, text="Search Employee", command=self.search_employee, width=20).pack(pady=10)
        tk.Button(self.root, text="Delete Employee", command=self.delete_employee, width=20).pack(pady=10)
        tk.Button(self.root, text="Update Employee", command=self.update_employee, width=20).pack(pady=10)
        tk.Button(self.root, text="Back to Main Menu", command=self.main_menu, width=20).pack(pady=10)

    def show_employees(self):
        conn = connect_db()
        df = pd.read_sql("SELECT * FROM Employee", conn)
        conn.close()
        self.display_dataframe(df)

    def add_employee(self):
        self.data_entry_window("Add Employee", ["EmployeeID", "BranchID", "Name", "Role", "Salary", "HireDate"], self.save_employee)

    def save_employee(self, data):
        conn = connect_db()
        cursor = conn.cursor()
        query = "INSERT INTO Employee (EmployeeID, BranchID, Name, Role, Salary, HireDate) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, data)
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Employee added successfully")

    def search_employee(self):
        self.search_window("Search Employee", "EmployeeID", self.show_employee_result)

    def show_employee_result(self, employee_id):
        conn = connect_db()
        df = pd.read_sql(f"SELECT * FROM Employee WHERE EmployeeID = {employee_id}", conn)
        conn.close()
        self.display_dataframe(df)

    def delete_employee(self):
        self.search_window("Delete Employee", "EmployeeID", self.delete_employee_record)

    def delete_employee_record(self, employee_id):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM Employee WHERE EmployeeID = {employee_id}")
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Employee deleted successfully")

    def update_employee(self):
        self.search_window("Update Employee", "EmployeeID", self.update_employee_record)

    def update_employee_record(self, employee_id):
        conn = connect_db()
        df = pd.read_sql(f"SELECT * FROM Employee WHERE EmployeeID = {employee_id}", conn)
        conn.close()
        if not df.empty:
            self.data_entry_window("Update Employee", ["BranchID", "Name", "Role", "Salary", "HireDate"], lambda data: self.save_employee_update(employee_id, data), df.iloc[0].tolist()[1:])
        else:
            messagebox.showinfo("Error", "Employee not found")

    def save_employee_update(self, employee_id, data):
        conn = connect_db()
        cursor = conn.cursor()
        query = "UPDATE Employee SET BranchID = %s, Name = %s, Role = %s, Salary = %s, HireDate = %s WHERE EmployeeID = %s"
        cursor.execute(query, data + [employee_id])
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Employee updated successfully")

    # Transaction Menu
    def transaction_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Button(self.root, text="Show Transactions", command=self.show_transactions, width=20).pack(pady=10)
        tk.Button(self.root, text="Add Transaction", command=self.add_transaction, width=20).pack(pady=10)
        tk.Button(self.root, text="Search Transaction", command=self.search_transaction, width=20).pack(pady=10)
        tk.Button(self.root, text="Back to Main Menu", command=self.main_menu, width=20).pack(pady=10)

    def show_transactions(self):
        conn = connect_db()
        df = pd.read_sql("SELECT * FROM Transaction", conn)
        conn.close()
        self.display_dataframe(df)

    def add_transaction(self):
        self.data_entry_window("Add Transaction", ["TransactionID", "AccountID", "TransactionType", "Amount", "TransactionDate"], self.save_transaction)

    def save_transaction(self, data):
        conn = connect_db()
        cursor = conn.cursor()
        query = "INSERT INTO Transaction (TransactionID, AccountID, TransactionType, Amount, TransactionDate) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, data)
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Transaction added successfully")

    def search_transaction(self):
        self.search_window("Search Transaction", "TransactionID", self.show_transaction_result)

    def show_transaction_result(self, transaction_id):
        conn = connect_db()
        df = pd.read_sql(f"SELECT * FROM Transaction WHERE TransactionID = {transaction_id}", conn)
        conn.close()
        self.display_dataframe(df)
        # Loan Menu
    def loan_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Button(self.root, text="Show Loans", command=self.show_loans, width=20).pack(pady=10)
        tk.Button(self.root, text="Add Loan", command=self.add_loan, width=20).pack(pady=10)
        tk.Button(self.root, text="Search Loan", command=self.search_loan, width=20).pack(pady=10)
        tk.Button(self.root, text="Delete Loan", command=self.delete_loan, width=20).pack(pady=10)
        tk.Button(self.root, text="Update Loan", command=self.update_loan, width=20).pack(pady=10)
        tk.Button(self.root, text="Back to Main Menu", command=self.main_menu, width=20).pack(pady=10)

    def show_loans(self):
        conn = connect_db()
        df = pd.read_sql("SELECT * FROM Loan", conn)
        conn.close()
        self.display_dataframe(df)

    def add_loan(self):
        self.data_entry_window("Add Loan", ["LoanID", "AccountID", "LoanAmount", "InterestRate", "LoanTerm", "StartDate", "EndDate"], self.save_loan)

    def save_loan(self, data):
        conn = connect_db()
        cursor = conn.cursor()
        query = "INSERT INTO Loan (LoanID, AccountID, LoanAmount, InterestRate, LoanTerm, StartDate, EndDate) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, data)
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Loan added successfully")

    def search_loan(self):
        self.search_window("Search Loan", "LoanID", self.show_loan_result)

    def show_loan_result(self, loan_id):
        conn = connect_db()
        df = pd.read_sql(f"SELECT * FROM Loan WHERE LoanID = {loan_id}", conn)
        conn.close()
        self.display_dataframe(df)

    def delete_loan(self):
        self.search_window("Delete Loan", "LoanID", self.delete_loan_record)

    def delete_loan_record(self, loan_id):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM Loan WHERE LoanID = {loan_id}")
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Loan deleted successfully")

    def update_loan(self):
        self.search_window("Update Loan", "LoanID", self.update_loan_record)

    def update_loan_record(self, loan_id):
        conn = connect_db()
        df = pd.read_sql(f"SELECT * FROM Loan WHERE LoanID = {loan_id}", conn)
        conn.close()
        if not df.empty:
            self.data_entry_window("Update Loan", ["AccountID", "LoanAmount", "InterestRate", "LoanTerm", "StartDate", "EndDate"], lambda data: self.save_loan_update(loan_id, data), df.iloc[0].tolist()[1:])
        else:
            messagebox.showinfo("Error", "Loan not found")

    def save_loan_update(self, loan_id, data):
        conn = connect_db()
        cursor = conn.cursor()
        query = "UPDATE Loan SET AccountID = %s, LoanAmount = %s, InterestRate = %s, LoanTerm = %s, StartDate = %s, EndDate = %s WHERE LoanID = %s"
        cursor.execute(query, data + [loan_id])
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Loan updated successfully")
    

    # Helper Methods
    def display_dataframe(self, df):
        # Show the dataframe in a new window
        for widget in self.root.winfo_children():
            widget.destroy()

        tree = ttk.Treeview(self.root, columns=list(df.columns), show="headings")
        tree.pack(fill=tk.BOTH, expand=True)
        
        for col in df.columns:
            tree.heading(col, text=col)
        
        for row in df.values.tolist():
            tree.insert("", tk.END, values=row)
        
        tk.Button(self.root, text="Back to Main Menu", command=self.main_menu, width=20).pack(pady=10)

    def search_window(self, title, search_key, callback):
        search_window = tk.Toplevel(self.root)
        search_window.title(title)
        search_window.geometry("300x200")

        tk.Label(search_window, text=f"Enter {search_key}:").pack(pady=10)
        search_entry = tk.Entry(search_window)
        search_entry.pack(pady=5)

        def on_search():
            value = search_entry.get()
            if value:
                callback(value)
                search_window.destroy()
            else:
                messagebox.showwarning("Input Error", f"Please enter {search_key}")
        
        tk.Button(search_window, text="Search", command=on_search).pack(pady=10)
        tk.Button(search_window, text="Cancel", command=search_window.destroy).pack(pady=5)

    def data_entry_window(self, title, fields, save_callback, default_values=[]):
        entry_window = tk.Toplevel(self.root)
        entry_window.title(title)
        entry_window.geometry("300x300")

        entries = {}
        for i, field in enumerate(fields):
            tk.Label(entry_window, text=field).pack(pady=5)
            entry = tk.Entry(entry_window)
            entry.insert(0, default_values[i] if i < len(default_values) else "")
            entry.pack(pady=5)
            entries[field] = entry

        def on_save():
            data = [entries[field].get() for field in fields]
            if all(data):
                save_callback(data)
                entry_window.destroy()
            else:
                messagebox.showwarning("Input Error", "Please fill all fields")

        tk.Button(entry_window, text="Save", command=on_save).pack(pady=10)
        tk.Button(entry_window, text="Cancel", command=entry_window.destroy).pack(pady=5)

# Running the app
if __name__ == "__main__":
    root = tk.Tk()
    app = BankingApp(root)
    root.mainloop()
