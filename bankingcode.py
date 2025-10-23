import pymysql
import random 

def connect_db():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="Poojastar1*",
        database="Python_force"
    )

def generate_unique_number(cursor):
    while True:
        acc_num=random.randint(1000000000,99999999999)
        cursor.execute("select account_number from bank_accounts where account_number=%s",(acc_num,))
        if not cursor.fetchone():
            return acc_num

def create_account():
    name=input("Enter owner_name: ")
    db=connect_db()
    cursor=db.cursor()

    cursor.execute("select * from bank_accounts where owner_name=%s",(name))
    if cursor.fetchone():
        print("Account already exists for this name.")
    else:
        account_number=generate_unique_number(cursor)
        cursor.execute(
            "Insert into bank_accounts(owner_name, account_number, balance) VALUES(%s, %s, %s)",
            (name, account_number, 0)
        )
        db.commit()
        print(f"Account created. Account number: {account_number}")

    cursor.close()
    db.close()

def deposit():
    acc_num=input("Please enter your account number:")
    amount=float(input("enter deposit amount:"))
    db=connect_db()
    cursor=db.cursor()

    cursor.execute("select balance from bank_accounts where account_number=%s",(acc_num))
    result=cursor.fetchone()

    if result:
        new_balance = result[0] + amount
        cursor.execute("update bank_accounts set balance =%s where account_number=%s",(new_balance,acc_num))
        db.commit()
        print(f"Deposited{amount}. Avaiable balance in your account{new_balance}")
    else:
        print("Invalid account_number, Please enter correct account number.")

    cursor.close()
    db.close()

def withdraw():
    acc_num=input("Please enter your account number:")
    amount=float(input("enter withdrawal amount:"))
    db=connect_db()
    cursor=db.cursor()

    cursor.execute("select balance from bank_accounts where account_number=%s",(acc_num))
    result=cursor.fetchone()

    if result:
        if result[0] >= amount:
            new_balance = result[0] - amount
            cursor.execute("update bank_accounts set balance=%s where account_number=%s",(new_balance,acc_num))
            db.commit()
            print(f"withdrawal {amount}. Your current balance is: {new_balance}")
        else:
            print("Insufficient funds.")
    else:
        print("Account number not found, Please enter correct account number")

    cursor.close()
    db.close()

def main():
    while True:
        print("\n----Bank Menu---")
        print("1.Create account")
        print("2.deposit")
        print("3.withdraw")
        print("4.exit")
        choice = input("choose and option= ")

        if choice == '1':
            create_account()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again")

if __name__== "__main__":
    main()
        
        


    
        