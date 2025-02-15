# Banking Management System

## 📋 Overview
The **Banking Management System** is a Python-based desktop application built using **Tkinter** for the GUI, **Pandas** for data handling, and **MySQL** for database management. This system allows banks to efficiently manage their customers, accounts, branches, employees, transactions, and loans.

## 🚀 Features
- **Customer Management:** Add, view, search, update, and delete customer records.
- **Branch Management:** Manage details of bank branches.
- **Account Management:** Handle account creation, viewing, updating, and deletion.
- **Employee Management:** Track employee information, roles, and salaries.
- **Transaction Management:** Record, search, and manage transactions.
- **Loan Management:** Add, update, view, and delete loan details.

## 🛠️ Technologies Used
- **Python** (with Tkinter for GUI)
- **Pandas** (for data display and manipulation)
- **MySQL** (for database storage)
- **pymysql** (for Python-MySQL connectivity)

## 💻 Prerequisites
- **Python 3.x** installed
- **MySQL Server** installed
- **MySQL Workbench** (optional, for managing databases visually)
- Required Python libraries:
  ```bash
  pip install pymysql pandas
  ```

## 🗂️ Database Setup
1. Open MySQL Workbench or any MySQL client.
2. Create a database named `BankingSystem`:
   ```sql
   CREATE DATABASE BankingSystem;
   USE BankingSystem;
   ```
3. Run the following SQL commands to create the necessary tables:
   ```sql
   CREATE TABLE Customer (
       CustomerID INT PRIMARY KEY,
       Name VARCHAR(100),
       Phone VARCHAR(15),
       Email VARCHAR(100),
       Address VARCHAR(255),
       DateOfBirth DATE
   );

   CREATE TABLE Branch (
       BranchID INT PRIMARY KEY,
       BranchName VARCHAR(100),
       Address VARCHAR(255),
       Phone VARCHAR(15)
   );

   CREATE TABLE Account (
       AccountID INT PRIMARY KEY,
       CustomerID INT,
       BranchID INT,
       AccountType VARCHAR(50),
       Balance DECIMAL(15, 2),
       OpeningDate DATE,
       FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
       FOREIGN KEY (BranchID) REFERENCES Branch(BranchID)
   );

   CREATE TABLE Employee (
       EmployeeID INT PRIMARY KEY,
       BranchID INT,
       Name VARCHAR(100),
       Role VARCHAR(50),
       Salary DECIMAL(10, 2),
       HireDate DATE,
       FOREIGN KEY (BranchID) REFERENCES Branch(BranchID)
   );

   CREATE TABLE Transaction (
       TransactionID INT PRIMARY KEY,
       AccountID INT,
       TransactionType VARCHAR(50),
       Amount DECIMAL(15, 2),
       TransactionDate DATE,
       FOREIGN KEY (AccountID) REFERENCES Account(AccountID)
   );

   CREATE TABLE Loan (
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
   ```

## ⚙️ Configuration
- In the Python code, ensure the database connection parameters match your MySQL credentials:
  ```python
  def connect_db():
      return pymysql.connect(host="localhost", user="root", passwd="your_password", database="BankingSystem")
  ```

## 📥 Installation & Running the Application
1. **Clone the repository or download the files:**
   ```bash
   git clone https://github.com/anamay1857/BankingManagementSystem.git
   cd BankingManagementSystem
   ```
2. **Install dependencies:**
   ```bash
   pip install pymysql pandas
   ```
3. **Run the application:**
   ```bash
   python3 main-GUI.py
   ```

## 🗒️ How It Works
- Upon launching, the **Main Menu** provides options for managing Customers, Branches, Accounts, Employees, Transactions, and Loans.
- Each section allows you to perform CRUD (Create, Read, Update, Delete) operations.
- Data is dynamically fetched from the MySQL database and displayed using Tkinter Treeview.

## 📊 Sample Use Cases
- **Add a New Customer:** Go to the Customer Menu → Add Customer → Fill details → Save.
- **Search Transaction:** Go to the Transaction Menu → Search Transaction → Enter Transaction ID → View details.
- **Manage Loans:** Loan Menu → Add/Search/Update/Delete Loan.

## 🤝 Contributing
Feel free to fork the project and submit pull requests for improvements or bug fixes.

## ⚠️ Troubleshooting
- **MySQL Connection Error:** Check if MySQL Server is running and credentials are correct.
- **Module Not Found:** Ensure `pymysql` and `pandas` are installed.

## 📧 Contact
For any queries, contact: [Anamay Prasad] - [anamayprasad1@gmail.com]  

---

**Enjoy managing your banking system efficiently! 🚀**

