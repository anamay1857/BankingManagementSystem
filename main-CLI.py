import pymysql
import matplotlib.pyplot as plt
import pandas as pd

#FOR CUSTOMER
def Customer():
    print("\n1. Show Customers \n2. Add Customer \n3. Search Customer \n4. Delete Customer \n5. Update Customer Data")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        ShowCustomers()
    elif choice == 2:
        AddCustomer()
    elif choice ==3:
        SearchCustomer()    
    elif choice == 4:
        DelCustomer()
    elif choice == 5:
        UpdateCustomerData()
    else:
        print('INVALID INPUT')    

def ShowCustomers():
    d1=pymysql.connect(host="localhost",user="root",passwd="password",database="BankingSystem")
    #c1=d1.cursor()
    quer="select * from Customer;"
    df=pd.read_sql(quer,d1)
    print(df)

def AddCustomer():    
    d1=pymysql.connect(host="localhost",user="root",passwd="password",database="BankingSystem")
    c1=d1.cursor()
    CustomerID = int(input("CustomerID: "))
    Name = input("Name: ")
    Phone = int(input("Phone: "))
    Email = input("Email: ")
    Address = input("Address: ")
    DateOfBirth = input("Date Of Birth yyyy-mm-dd: ")

    val = (CustomerID, Name, Phone, Email, Address, DateOfBirth)

    quer="INSERT INTO Customer(CustomerID, Name, Phone, Email, Address, DateOfBirth) VALUES (%s, %s, %s, %s, %s, %s);" 
    print(c1.execute(quer,val))
    d1.commit()
    print("Record Added")

def SearchCustomer():
    d1=pymysql.connect(user="root",host="localhost",passwd="password",database="BankingSystem")
    #c1=d1.cursor() 
    x=int(input("CustomerID: "))
    quer="select * from Customer where CustomerID=" + str(x)
    df=pd.read_sql(quer,d1)
    if df.size!=0:
        print(df)
    else:
        print("CustomerID ", x, "isn't present")

def DelCustomer():
    d1=pymysql.connect(host="localhost",user="root",passwd="password",database="BankingSystem")
    c1=d1.cursor()   
    x=int(input("\nEnter the CustomerID: "))
    quer="delete from Customer where CustomerID=%d;" %x
    rowcount=c1.execute(quer)
    if rowcount>0:
        d1.commit()
        print("Record Deleted")
    else:
        print("NO RECORD FOUND")

def SearchCustomer():
    d1=pymysql.connect(host="localhost",user="root",passwd="password",database="BankingSystem")
    c1=d1.cursor()
    x=int(input("CustomerID: "))
    quer="select * from Customer where CustomerID=" + str(x)
    df=pd.read_sql(quer,d1)
    if df.size!=0:
        print(df)
    else:
        print("CustomerID ", x, "isn't present")

def UpdateCustomerData():
    d1=pymysql.connect(host="localhost",user="root",passwd="password",database="BankingSystem")
    c1=d1.cursor()
    x=int(input("\nCustomerID: "))
    quer="select * from Customer where CustomerID=" + str(x)
    c1.execute(quer)
    if c1.rowcount>0:
        #row=list(c1.fetchone())
        df=pd.read_sql(quer,d1)
        print(df)
        print("\n1. Name of Customer \n2. Phone\n3. Email \n4. Address \n5. Date of Birth")
        cr=int(input("Enter the no: "))

        #Name of customer
        if cr==1:
            y=input("\nEnter the new name of customer: ")
            quer="update Customer set name='%s' where CustomerID=%d" %(y,x)
            c1.execute(quer)
            d1.commit()
            print("Record Updated")
        #Phone             
        elif cr==2:
            y=input("Enter the new Phone number: ")
            quer="update Customer set phone='%s' where CustomerID=%d" %(y,x)
            c1.execute(quer)
            d1.commit()
            print("Record Updated") 
        #Email               
        elif cr==3:
            y=input("Enter the new email: ")
            quer="update Customer set email='%s' where CustomerID=%d" %(y,x)
            c1.execute(quer)
            d1.commit()
            print("Record Updated")
        #Address    
        elif cr==4:
            y=input("Enter the new address: ")
            quer="update Customer set address='%s' where CustomerID=%d" %(y,x)
            c1.execute(quer)
            d1.commit()
            print("Record Updated")   
        #DOB  
        elif cr==5:
            y=input("Enter the new date of birth yyyy-mm-dd: ")
            quer="update Customer set dateofbirth='%s' where CustomerID=%d" %(y,x)
            c1.execute(quer)
            d1.commit()
            print("Record Updated")
 
    elif c1.rowcount==0 or c1!=[1,2,3,4,5,6,7,8]:
        print("NO RECORD FOUND TO CHANGE")

# FOR BRANCH
def Branch():
    print("\n1. Show Branches \n2. Add Branch \n3. Delete Branch \n4. Update Branch")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        ShowBranches()
    elif choice == 2:
        AddBranch()
    elif choice ==3:
        SearchBranch()    
    elif choice ==4:
        DelBranch()    
    elif choice == 5:
        UpdateBranch()
    else:
        print('INVALID INPUT')

def ShowBranches():
    d1=pymysql.connect(host="localhost",user="root",passwd="password",database="BankingSystem")
    #c1=d1.cursor()
    quer="select * from Branch;"
    df=pd.read_sql(quer,d1)
    print(df)

def AddBranch():
    d1=pymysql.connect(host="localhost",user="root",passwd="password",database="BankingSystem")
    c1=d1.cursor()
    BranchID = int(input("BranchID: "))
    BranchName = input("BranchName: ")
    Address = (input("Address: "))
    Phone = int(input("Phone: "))

    if not (BranchID):
        print("Error: BranchID does not exist. Please enter a valid BranchID.")
        return
    
    val = (BranchID, BranchName, Address, Phone)

    quer="INSERT INTO Branch(BranchID, BranchName, Address, Phone) VALUES (%s, %s, %s, %s);" 
    print(c1.execute(quer,val))
    d1.commit()
    print("Record Added")

def SearchBranch():
    d1=pymysql.connect(host="localhost",user="root",passwd="password",database="BankingSystem")
    c1=d1.cursor()
    x=int(input("BranchID: "))
    quer="select * from Branch where BranchID=" + str(x)
    df=pd.read_sql(quer,d1)
    if df.size!=0:
        print(df)
    else:
        print("BranchID ", x, "isn't present")

def DelBranch():
    d1=pymysql.connect(host="localhost",user="root",passwd="password",database="BankingSystem")
    c1=d1.cursor()   
    x=int(input("\nEnter the BranchID: "))
    quer="delete from Branch where BranchID=%d;" %x
    rowcount=c1.execute(quer)
    if rowcount>0:
        d1.commit()
        print("Record Deleted")
    else:
        print("NO RECORD FOUND")       

def UpdateBranch():
    d1=pymysql.connect(host="localhost",user="root",passwd="password",database="BankingSystem")
    c1=d1.cursor()
    x=int(input("\BranchID: "))
    quer="select * from Branch where BranchID=" + str(x)
    c1.execute(quer)
    if c1.rowcount>0:
        #row=list(c1.fetchone())
        df=pd.read_sql(quer,d1)
        print(df)
        print("\n1. BranchID \n2. BranchName \n3. Address \n5. Phone")
        cr=int(input("Enter the no: "))

        #BranchID
        if cr==1:
            y=input("\nEnter the new BranchID: ")
            quer="update Branch set name='%s' where BranchID=%d" %(y,x)
            c1.execute(quer)
            d1.commit()
            print("Record Updated")
        #BranchName            
        elif cr==2:
            y=input("Enter the new BranchName: ")
            quer="update Branch set BranchName='%s' where BranchID=%d" %(y,x)
            c1.execute(quer)
            d1.commit()
            print("Record Updated") 
        #Address               
        elif cr==3:
            y=input("Enter the new Address: ")
            quer="update Branch set Address='%s' where BranchID=%d" %(y,x)
            c1.execute(quer)
            d1.commit()
            print("Record Updated")
        #Phone    
        elif cr==4:
            y=input("Enter the new Phone: ")
            quer="update Branch set Phone='%s' where BranchID=%d" %(y,x)
            c1.execute(quer)
            d1.commit()
            print("Record Updated")   
    
    elif c1.rowcount==0 or c1!=[1,2,3,4,5,6,7,8]:
        print("NO RECORD FOUND TO CHANGE")




# FOR ACCOUNT
def Account():
    print("\n1. Show Accounts \n2. Add Account \n3. Delete Account \n4. Update Account")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        ShowAccounts()
    elif choice == 2:
        AddAccount()
    elif choice ==3:
        SearchAccount()    
    elif choice == 4:
        DelAccount()
    elif choice == 5:
        UpdateAccountData()
    else:
        print('INVALID INPUT')  

def ShowAccounts():
    d1=pymysql.connect(host="localhost",user="root",passwd="password",database="BankingSystem")
    #c1=d1.cursor()
    quer="select * from Account;"
    df=pd.read_sql(quer,d1)
    print(df)

def AddAccount():
    d1=pymysql.connect(host="localhost",user="root",passwd="password",database="BankingSystem")
    c1=d1.cursor()
    AccountID = int(input("\nAccountID: "))
    CustomerID = input("CustomerID: ")
    BranchID = int(input("BranchID: "))
    AccountType = input("Account Type: ")
    Balance = input("Balance: ")
    OpeningDate = input("Opening Datye yyyy-mm-dd: ")

    val = (AccountID, CustomerID, BranchID, AccountType, Balance, OpeningDate)

    quer="INSERT INTO Account(AccountID, CustomerID, BranchID, AccountType, Balance, OpeningDate) VALUES (%s, %s, %s, %s, %s, %s);" 
    print(c1.execute(quer,val))
    d1.commit()
    print("Record Added")

def SearchAccount():
    d1=pymysql.connect(host="localhost",user="root",passwd="password",database="BankingSystem")
    c1=d1.cursor()
    x=int(input("AccountID: "))
    quer="select * from Account where AccountID=" + str(x)
    df=pd.read_sql(quer,d1)
    if df.size!=0:
        print(df)
    else:
        print("AccountID ", x, "isn't present")

def DelAccount():
    d1=pymysql.connect(host="localhost",user="root",passwd="password",database="BankingSystem")
    c1=d1.cursor()   
    x=int(input("\nEnter the AccountID: "))
    quer="delete from Account where AccountID=%d;" %x
    rowcount=c1.execute(quer)
    if rowcount>0:
        d1.commit()
        print("Record Deleted")
    else:
        print("NO RECORD FOUND") 

def UpdateAccountData():
    d1=pymysql.connect(host="localhost",user="root",passwd="password",database="BankingSystem")
    c1=d1.cursor()
    x=int(input("AccountID: "))
    quer="select * from Account where AccountID=" + str(x)
    c1.execute(quer)
    if c1.rowcount>0:
        #row=list(c1.fetchone())
        df=pd.read_sql(quer,d1)
        print(df)
        print("\n1. AccountID \n2. CustomerID \n3. BranchID \n5. Account Type \n6. Balance \n.7 Opening Date")
        cr=int(input("Enter the no: "))

        #BranchID
        if cr==1:
            y=input("\nEnter the new AccountID: ")
            quer="update Account set AccountID='%s' where AccountID=%d" %(y,x)
            c1.execute(quer)
            d1.commit()
            print("Record Updated")
        #BranchName            
        elif cr==2:
            y=input("Enter the new BranchName: ")
            quer="update Branch set BranchName='%s' where BranchID=%d" %(y,x)
            c1.execute(quer)
            d1.commit()
            print("Record Updated") 
        #Address               
        elif cr==3:
            y=input("Enter the new Address: ")
            quer="update Branch set Address='%s' where BranchID=%d" %(y,x)
            c1.execute(quer)
            d1.commit()
            print("Record Updated")
        #Phone    
        elif cr==4:
            y=input("Enter the new Phone: ")
            quer="update Branch set Phone='%s' where BranchID=%d" %(y,x)
            c1.execute(quer)
            d1.commit()
            print("Record Updated")   
    
    elif c1.rowcount==0 or c1!=[1,2,3,4,5,6,7,8]:
        print("NO RECORD FOUND TO CHANGE")

# FOR EMPLOYEE
def Employee():
    print("\n1. Show Employees \n2. Add Employee \n3. Search Employee \n4. Delete Employee \n5. Update Employee")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        ShowEmployees()
    elif choice == 2:
        AddEmployee()
    elif choice == 3:
        SearchEmployee()
    elif choice == 4:
        DelEmployee()
    elif choice == 5:
        UpdateEmployee()
    else:
        print('INVALID INPUT')

def ShowEmployees():
    d1 = pymysql.connect(host="localhost", user="root", passwd="password", database="BankingSystem")
    quer = "SELECT * FROM Employee;"
    df = pd.read_sql(quer, d1)
    print(df)

def AddEmployee():
    d1 = pymysql.connect(host="localhost", user="root", passwd="password", database="BankingSystem")
    c1 = d1.cursor()
    EmployeeID = int(input("EmployeeID: "))
    BranchID = int(input("BranchID: "))
    Name = input("Name: ")
    Role = input("Role: ")
    Salary = float(input("Salary: "))
    HireDate = input("HireDate (yyyy-mm-dd): ")

    val = (EmployeeID, BranchID, Name, Role, Salary, HireDate)
    quer = "INSERT INTO Employee(EmployeeID, BranchID, Name, Role, Salary, HireDate) VALUES (%s, %s, %s, %s, %s, %s);"
    c1.execute(quer, val)
    d1.commit()
    print("Record Added")

def SearchEmployee():
    d1 = pymysql.connect(host="localhost", user="root", passwd="password", database="BankingSystem")
    x = int(input("EmployeeID: "))
    quer = "SELECT * FROM Employee WHERE EmployeeID=" + str(x)
    df = pd.read_sql(quer, d1)
    if df.size != 0:
        print(df)
    else:
        print("EmployeeID", x, "isn't present")

def DelEmployee():
    d1 = pymysql.connect(host="localhost", user="root", passwd="password", database="BankingSystem")
    c1 = d1.cursor()
    x = int(input("Enter the EmployeeID: "))
    quer = "DELETE FROM Employee WHERE EmployeeID=%d;" % x
    rowcount = c1.execute(quer)
    if rowcount > 0:
        d1.commit()
        print("Record Deleted")
    else:
        print("NO RECORD FOUND")

def UpdateEmployee():
    d1 = pymysql.connect(host="localhost", user="root", passwd="password", database="BankingSystem")
    c1 = d1.cursor()
    x = int(input("EmployeeID: "))
    quer = "SELECT * FROM Employee WHERE EmployeeID=" + str(x)
    c1.execute(quer)
    if c1.rowcount > 0:
        df = pd.read_sql(quer, d1)
        print(df)
        print("\n1. Name \n2. Role \n3. Salary \n4. HireDate")
        cr = int(input("Enter the no: "))

        if cr == 1:
            y = input("Enter the new Name: ")
            quer = "UPDATE Employee SET Name='%s' WHERE EmployeeID=%d" % (y, x)
        elif cr == 2:
            y = input("Enter the new Role: ")
            quer = "UPDATE Employee SET Role='%s' WHERE EmployeeID=%d" % (y, x)
        elif cr == 3:
            y = float(input("Enter the new Salary: "))
            quer = "UPDATE Employee SET Salary=%f WHERE EmployeeID=%d" % (y, x)
        elif cr == 4:
            y = input("Enter the new HireDate (yyyy-mm-dd): ")
            quer = "UPDATE Employee SET HireDate='%s' WHERE EmployeeID=%d" % (y, x)
        else:
            print("INVALID CHOICE")
            return

        c1.execute(quer)
        d1.commit()
        print("Record Updated")
    else:
        print("NO RECORD FOUND TO CHANGE")


# FOR TRANSACTION
def Transaction():
    print("\n1. Show Transactions \n2. Add Transaction \n3. Search Transaction \n4. Delete Transaction")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        ShowTransactions()
    elif choice == 2:
        AddTransaction()
    elif choice == 3:
        SearchTransaction()
    elif choice == 4:
        DelTransaction()
    else:
        print('INVALID INPUT')

def ShowTransactions():
    d1 = pymysql.connect(host="localhost", user="root", passwd="password", database="BankingSystem")
    quer = "SELECT * FROM Transaction;"
    df = pd.read_sql(quer, d1)
    print(df)

def AddTransaction():
    d1 = pymysql.connect(host="localhost", user="root", passwd="password", database="BankingSystem")
    c1 = d1.cursor()
    TransactionID = int(input("TransactionID: "))
    AccountID = int(input("AccountID: "))
    TransactionType = input("TransactionType (Deposit/Withdraw): ")
    Amount = float(input("Amount: "))
    TransactionDate = input("TransactionDate (yyyy-mm-dd): ")

    val = (TransactionID, AccountID, TransactionType, Amount, TransactionDate)
    quer = "INSERT INTO Transaction(TransactionID, AccountID, TransactionType, Amount, TransactionDate) VALUES (%s, %s, %s, %s, %s);"
    c1.execute(quer, val)
    d1.commit()
    print("Record Added")

def SearchTransaction():
    d1 = pymysql.connect(host="localhost", user="root", passwd="password", database="BankingSystem")
    x = int(input("TransactionID: "))
    quer = "SELECT * FROM Transaction WHERE TransactionID=" + str(x)
    df = pd.read_sql(quer, d1)
    if df.size != 0:
        print(df)
    else:
        print("TransactionID", x, "isn't present")

def DelTransaction():
    d1 = pymysql.connect(host="localhost", user="root", passwd="password", database="BankingSystem")
    c1 = d1.cursor()
    x = int(input("Enter the TransactionID: "))
    quer = "DELETE FROM Transaction WHERE TransactionID=%d;" % x
    rowcount = c1.execute(quer)
    if rowcount > 0:
        d1.commit()
        print("Record Deleted")
    else:
        print("NO RECORD FOUND")

# FOR LOAN
def Loan():
    print("\n1. Show Loans \n2. Add Loan \n3. Search Loan \n4. Delete Loan")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        ShowLoans()
    elif choice == 2:
        AddLoan()
    elif choice == 3:
        SearchLoan()
    elif choice == 4:
        DelLoan()
    else:
        print('INVALID INPUT')

def ShowLoans():
    d1 = pymysql.connect(host="localhost", user="root", passwd="password", database="BankingSystem")
    quer = "SELECT * FROM Loan;"
    df = pd.read_sql(quer, d1)
    print(df)

def AddLoan():
    d1 = pymysql.connect(host="localhost", user="root", passwd="password", database="BankingSystem")
    c1 = d1.cursor()
    LoanID = int(input("LoanID: "))
    CustomerID = int(input("CustomerID: "))
    AccountID = int(input("AccountID: "))
    LoanAmount = float(input("LoanAmount: "))
    InterestRate = float(input("InterestRate: "))
    StartDate = input("StartDate (yyyy-mm-dd): ")
    EndDate = input("EndDate (yyyy-mm-dd): ")

    val = (LoanID, CustomerID, AccountID, LoanAmount, InterestRate, StartDate, EndDate)
    quer = "INSERT INTO Loan(LoanID, CustomerID, AccountID, LoanAmount, InterestRate, StartDate, EndDate) VALUES (%s, %s, %s, %s, %s, %s, %s);"
    c1.execute(quer, val)
    d1.commit()
    print("Record Added")

def SearchLoan():
    d1 = pymysql.connect(host="localhost", user="root", passwd="password", database="BankingSystem")
    x = int(input("LoanID: "))
    quer = "SELECT * FROM Loan WHERE LoanID=" + str(x)
    df = pd.read_sql(quer, d1)
    if df.size != 0:
        print(df)
    else:
        print("LoanID", x, "isn't present")

def DelLoan():
    d1 = pymysql.connect(host="localhost", user="root", passwd="password", database="BankingSystem")
    c1 = d1.cursor()
    x = int(input("Enter the LoanID: "))
    quer = "DELETE FROM Loan WHERE LoanID=%d;" % x
    rowcount = c1.execute(quer)
    if rowcount > 0:
        d1.commit()
        print("Record Deleted")
    else:
        print("NO RECORD FOUND")



print("========================================== \nWelcome to Banking Management System \n==========================================")
print("1. Customer \n2. Branch \n3. Account \n4. Employee \n5. Transactions \n6. Loan \n6. Exit")
x=int(input("Enter the no. "))

if x==1:
    Customer()
elif x==2:
    Branch()
elif x==3:
    Account()
elif x==4:
    Employee()
elif x==5:
    Transaction()
elif x==6:
    Loan()
elif x==7:
    print("Exiting the system. Goodbye!")
    exit()
else:
    print("Invalid choice")


'''SQL QUERIES TO BE ENTERED FIRST IN MYSQL
CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(100),
    Phone VARCHAR(15),
    Email VARCHAR(100),
    Address VARCHAR(255),
    DateOfBirth DATE
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

CREATE TABLE Branch (
    BranchID INT PRIMARY KEY,
    BranchName VARCHAR(100),
    Address VARCHAR(255),
    Phone VARCHAR(15)
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
'''