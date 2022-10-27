import sqlite3
import jwt
from datetime import datetime, timedelta

def main():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Clients(
        id INT PRIMARY KEY,
        name_surname TEXT,
        acc_num INT,
        pass TEXT,
        token TEXT)
        """)

    conn.commit()

    clients = cursor.execute("SELECT * FROM Clients")

    if (len(clients.fetchall()) == 0):
        client = [('1', 'John Smith', '07', 'pwd1', ''), ('2', 'James Hunt', '10', 'pwd2', ''), ('3', 'Mike Black', '33', 'pwd3', '')]
        cursor.executemany("INSERT INTO Clients VALUES (?, ?, ?, ?, ?)", client)
        conn.commit()


    provided_acc = input("Enter client account number: ")
    provided_pass = input("Enter client password: ")


    data = cursor.execute("SELECT %s FROM clients where %s=? and %s=?" % ("acc_num", "acc_num", "pass"), (provided_acc, provided_pass))

    if (len(data.fetchall()) == 0):
        print("Client does not exist")
    else:
        key = "secret"
        encoded = jwt.encode({'acc_num': provided_acc, 'exp': datetime.utcnow() + timedelta(seconds=45)}, key, algorithm='HS256')

    cursor.execute("UPDATE Clients SET %s=? WHERE %s=? AND %s=?" % ("token", "acc_num", "pass"), (encoded, provided_acc, provided_pass))

    conn.commit()

    print("Login successful")
    print(encoded)


if __name__ == '__main__':
    main()