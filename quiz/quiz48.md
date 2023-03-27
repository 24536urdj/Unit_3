```.py 
import sqlite3
from secure_password import check_password

connection = sqlite3.connect("bitcoin_exchange.db")
cursor = connection.cursor()
query = "SELECT * FROM ledger"
result = cursor.execute(query).fetchall()
connection.close()

for y in result:
    unhashed = f"id {y[0]},sender_id {y[1]},receiver_id {y[2]},amount {y[3]}"
    if check_password(user_password=unhashed, hashed_password=y[4])==True:
        print(f"Tx(id={y[0]})Signature matches")
    else:
        print(f"Tx(id={y[0]})Error signature")
```
![Screen Shot 2023-03-27 at 19 24 53](https://user-images.githubusercontent.com/112072887/227915510-773b4a1e-ae66-4de7-9a7c-764680623d02.png)
