```.py 
import sqlite3

from kivymd.app import MDApp
from secure_password import encrypt_password

class database_worker:
    def __init__(self, name):
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()

    def search(self, query):
        result = self.cursor.execute(query).fetchall()
        return result

    def run_save(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()


class quiz047(MDApp):


    def build(self):
        return


    def update(self):
        base = self.root.ids.base.text
        hash = ""
        if base != "":
            total = int(base)
            hash+= f"base{total}"

            ids = ["inhabitant", "income_tax", "pension", "health"]

            # TextField = self.root.ids.inhabitant.text , self.root.ids.income_tax.text,self.root.ids.pension.text,
            for cat in ["inhabitant", "income_tax", "pension", "health"]:

                value = self.root.ids[cat].text
                if value != "":
                    new_value= f"{int(value)*int(base)//100 }JPY"
                    total -= int(value)*int(base)//100
                    hash  += f"id_of_textField{value}"
                else :
                    new_value = "JPY"
                    hash+= f"id_of_textField{0}"

                self.root.ids[cat+"_label"].text = new_value
        hash+= f"total{total}"
        self.root.ids.salary_label.text = f"{total}JPY"
        import hashlib
        hash_object = hashlib.sha224(b"hash")
        hex_dig = hash_object.hexdigest()
        print(hex_dig)


    def save(self):
        #repeat the algorithm in update but create variables to save the amount of each item:
        #base = int(base)
        #inhabitant = amount in JPY to remove from base for inhabitant tax
        #income_tax = amount in JPY to remove from base for income tax
        #pension = amount in JPY to remove from base for pension tax
        #health = amount in JPY to remove from base for health tax
        #total = total net salary
        #hahs = hash of the calcualtions in the format
        #inhabitant4,income_tax3,pension2,health1,total1103  (here the numbers next to the category are percentages)

        # query = f"""INSERT into payments
        # --here complete the code
        #
        # """
        # db = database_worker("payments.db")
        # db.run_save(query)
        # db.close()
        self.root.ids.hash.text = f"Payment saved"

    def clear(self):
        for label in ["base", "inhabitant","income_tax","pension","health"]:
            self.root.ids[label].text = ""
            self.root.ids[label+"_label"].text = " JPY"

        self.root.ids["salary_label"].text = " JPY"
        self.root.ids.hash.text = "----"


test = quiz047()
# create = """CREATE TABLE if not exists payments(
#
#
# --- Complete here the table
#
#
#     )"""
# db = database_worker("payments.db")
# db.run_save(create)
# db.close()
test.run()
```
