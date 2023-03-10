# Unit_3: project of creating a blog for my client 

![](https://github.com/24536urdj/Unit_3/blob/main/Project_unit_3/dd36613d-aaf4-4c07-acd1-0026086aa5bd.gif)


## Criteria A planning

### Problem definition
My client is mayte Flores (who is currently an IB student ) has expressed  her worries about the accumulation of a great amount of  historical topics  that she became interested in , and  wants to preserve .However the use of a notebook has became   difficult and  disorganized since the needs to buy constantly a new ,notebook while keeping the others, costs her both money and effort , subsequently taking into consideration mayte’s stance toward the privacy policies of many blog websites , and her passion to share these topics with her fellows ;I have decided to create a blog application for my client where she can preserve her privacy and maintain her choice of not sharing some personal data , along with keeping her historical topics organized and easy to find while giving her schoolmates access to them.

### Proposed solution
Considering the client's requirements, an adequate solution includes a low-cost alternative for a notebook  , a more  organized  version of a blog that suits my clients tolerance toward privacy policies ,and an application that allows her to share her work.
For a low-cost notebook , an adequate alternative is a digital blog which is will be created using Python because it is first an easy language and also a free one since it does not require a license. For the blog creation , I will use the KivyMD library to make it since Kivy is perhaps the only framework which is primarily written in pure Python[^2].  , and in order to keep it organized and fulfill the success criteria , I will use sql to associate a database to my app because it's portability makes it a convenient option for users, as they can transfer it from one device to another with no issues. It processes queries quickly. No matter how large data might be, SQL can retrieve it quickly and efficiently.[^3] so that my client will be able to add, withdraw and edit her topics.Finally in order for my client to be able to share her ideas , the blog will have two types of access , one for the owner , and one for the viewer.so that others can observe the topics she wants to publish and also keep those that she  does not want to publish for herself .

### Desing statement

I will design and program a low-cost blog application which will alow the owner to add,withdraw and edit her historical topics in an organized way. This application will also have the ability to share its topics through viewing option. This project is for our client who  needs a low cost blog application that will help her keep her pursue her passion about history easly and effectively . The blog will be created using the software PyCharm and oop programing paradigm that includes the use of python language, taking three weeks to make. All of the findings will be displayed on a 4 min informational video which will also include a discussion of how the code is well organized so that future developers can extend it
if found[^1]. The proposed solution will be evaluated according to criteria A and B.




### Success Criteria 
1. The solution needs to have a login and a registration system
2. The solution needs to have an option of resetting the password but only for my client that will be referred to as owner in the application
3. The solution needs to have an option screen with two buttons one for the owner and one for the viewers, and then depends on the button clicked a certain type of files will be shown.
5. The solution needs to be able to keep  the information about items organized and easily to follow by providing a searching button
6. The solution needs to enable the client to add new historical topic's notes 
7. The solution needs to enable the client to delete unwanted files.

## Criteria B design 
### system diagram
![GUI (1)](https://user-images.githubusercontent.com/112072887/222308800-dbecfa66-055b-4749-8c4b-3e71ed7211c4.png)
### Wireframe diagram for the application 
![Screenflow Diagram Flowchart Whiteboard in Pink Yellow Adjacent Color Blocks Style](https://user-images.githubusercontent.com/112072887/224026850-f4920acd-c68f-4476-97e9-c08dbeab1811.png)

### flow charts  

![Screen Shot 2023-03-09 at 22 12 13](https://user-images.githubusercontent.com/112072887/224033512-e774d401-2d4b-4b97-8590-e7302d936b7a.png)


this flow chart is for connecting python to sqlite database which is preferable to use with this programming language because SQLite is a very easy to use database engine included with Python. SQLite is open source and is a great database for smaller projects, hobby projects, or testing and developmen[^4] ,and also the functions added after the connection such as search , and run_save 
 


![Screen Shot 2023-03-09 at 23 30 04](https://user-images.githubusercontent.com/112072887/224055778-33f8f33e-eb4d-4054-9b7e-b90d61cb5c60.png)
This flow chart is for creating a secure log in function for my client,it uses if function in order to eliminate and mitigate the error of letting someone who does not possess the username or password of log in into the application.

![Screen Shot 2023-03-09 at 23 47 24](https://user-images.githubusercontent.com/112072887/224060498-157e9cc0-e1c9-4ebf-b089-fa9719655dfc.png)
This flow chart shows the creation of add function and save function that were required by client in the success criteria.the add function allows he client to add new topics to the data table ,and the save function serves to commit this action.
### Er diagram
![Screen Shot 2023-03-10 at 5 03 19](https://user-images.githubusercontent.com/112072887/224141550-50d77575-67a5-44da-b0c8-b75cf5abad16.png)

 the ER diagram shows the relationship between new topic table and topic_text table. In the topic table, there are 4 columns including id, topic, date, share , which each column will have the specific data type after the column name. The second table has 2 columns which are id,  and topic_text. This diagram shows also the primary key will be the id.


### UML Diagram 

![Screen Shot 2023-03-10 at 0 08 28](https://user-images.githubusercontent.com/112072887/224066394-4b9855c9-5c31-4660-9d31-47c5ad641b1f.png)
the UML diagram shows all the classes used by the developer  in this project with methods included in every class. There are 2 main parents class which are MDScreen and MDApp from which other class inherite methods and attributes from them. The inheritance is represented by the arrow.



## Test Plan
| Description                 | Type             | Inputs                                                                                                                                              | Outputs                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-----------------------------|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| login system         | Unit test        | 1. Run the python file login_screen.py 2. Click owner button on the homescreen 3. Input information in each textfield following the hint text 4. Click login | If the username is wrong:an error hint_text  in blue will say the username is wrong. If password is wrong :an error hint_text will appear saying the password is wrong don't match: the message will say that password doesn't match. If enterign the right password and username : successfully open DigitalScreen.                                                                                                                                                                                                                          |
|  Add function         | Unit test        | 1. login 2. press close button 3. press file button 4.press the tool bar and click on add new topic 5.input information in each textfield following the hint text 6.press save button 7.go back to database table and check if the new information added are updated and inserted correctly                                                    | all information in topic column need to be in alphabitical order and the new added information need to be there too.                                                                                                                                                                                                                                                                                                                                                        |
| Log out system              | Unit test        | 1. login 2. Press close  button                                                                                                                 | Digital screen 2 will appear 3. press close button 4.app closed                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Delete function               | Unit test        | 1.Press check on one of the id of the row you would like to delete in the TableScreen 2. Press delete                              |  the row is completely deleted                                                                                                                                                                                      |
|check if all thechniques needed are used  | code review t| 1.check login_screen.py for : 1. if everything in  list of techniques is used correctly and efectively | Note: the code must include all thechniques mentioned in criteria c and proposed solution  |
|Save function             | Unit test        | 1.go to NEW MDScreen 2. add all required information 3.press save button                                                      | 1.after presing the button ,it goes to TableSceen 2.the added data is saved in the databaseand in the data table 
                                                                            |                                                                                                                                                                                                                                                       
                                                                                                                                                          | Python Code Review          | Code Review      | Check the login_screen.py and database_library.py file for: 1. Variable names and  Comments                                                  | The variable name and comments need to show to the user  the functionality of the code that should be easy to follow and not too complicated to understand  |                                                                                                                                                                                                                


|    | Planned Action                                        | Planned Outcome                                                                            | Design Cycle   | Time Estimate | Target Completion | Criteria |
|----|-------------------------------------------------------|--------------------------------------------------------------------------------------------|----------------|---------------|-------------------|----------|
| 1  | First meeting with client                             | meeting with mayte flores ,to discuss her deisre for a method to gather hitory topics                                            | Planning       | 7 minutes    |10 february        | A        |
| 2  | Write down success criteria                           | discussing my client success criteria and eliminating the unnecessary ones.                                                | Planning       | 7 minutes    | 13 February          | A        |
| 3  | finalizing the success criteria                              |  Meeting with Mayte to show her the finalized success criteria and get her consent to start | Planning       | 10 minutes        | 16 feb           | A        |
| 4  | Write down the problem definition                              | state a detailed version of the problem and identify  the client                         | Planning       | 40 minutes    | 18 feb         | A        |
| 5  | Write down the proposed solution with justification of tools implied | Reasearch and evaluation of solutions to choose an adequate one                                   | Planning       | 2 hours    | 20 february        | A        |
| 6  | presenting the solution to the client  | getting the consent of my client and agreement on the solution                                                     | Planning       | 15 min      | 19 feb        | A        |
| 7  | Starts working on login  system       | Finish login system,(it doesn't need a database connect to it )                                        | Development    | 1 day         | 23 feb         | C        |
| 8  | Create system diagram                              | system diagram that will be presented to the client                          | Design         | 45 minutes        | 28 feb          | B        |
| 9  | start working on the GUI application interferance of login screen and homescreen                                | first part of the app is ready to be presented                                         | Developement         | 45 min      | 29 feb         | C       |
| 10 | Working on password validation                        | Create a unique username and password for my client that without it no one will be able to access the tools of editing or adding new files               | Development    | 30 min        | 29 feb            | C        |
| 11 | Create sql database to store the topics added | have a table with name .topic ,date and share columns                                                                   | Development    |  15 min      | 8           | C        |
| 12 | Present an mvp of the application to the class (and my client)   | Get client's feedback on the  application design and services available                                    | Planning       |     | 3 march         | A        |
| 13 | Make DataTable and connect it to the sql database along with creating an MDScreen in the kivy file for it                                     | data will be presented in the table in a another MDScreen in an organized way                                                   | developement      | 15 min    | 4 march          | C        |
| 14 | create an MDScreen with all tools available                       | An MDScreen with a Bar of tools such as add is created                                                               | Developement       | 20 minutes    |      4 march     | C       |
| 15 | Create another MDSreen to add new topics                          | MDScreen that allows client to fill the topic ,the date of its creation and if they would like to share it.                  | Development    | 3 hours                 | C        |



### Criteria C development 
## technique used 
- for loop
- creating application interferance with kivymd library 
-  connection to sql database
-  functions such as if function 
-  creating a data table using MDDataTable imported from kivymd 
-  using sql dialogue to insert,search and commit actions
-  using the language of python and sqlite .
-  
## HomeScreen created using kivymd
  ```py
  <HomeScreen>:
    size: 500,500
    FitImage:
        source: "love.png"
    MDCard:

        size_hint: .5, .9
        elevation : 2
        pos_hint:{"center_x":.5,"center_y":.5}

        orientation: "vertical"
        padding: dp(50)
        MDLabel:
            text: "WELCOME TO MIRABEL"
            font_style: "H3"
            size_hint: 1, .2

            pos_hint:{"center_x":.5,"center_y":.5}

        MDBoxLayout:
            size_hint: 1,.1

            MDRaisedButton:
                id: owner
                text: "owner"
                on_press:root.parent.current ="LoginScreen"
                size_hint:.3,1
                md_bg_color:"#e63946"
            MDRaisedButton:
                id:viewer
                text:"viewer"
                size_hint:.3,1
                on_press:root.parent.current ="Screen2"
```
# login screen using  kivymd 
```py
<LoginScreen>:
    size: 500,500
    FitImage:
        source: "love.png"
    MDCard:

        size_hint: .5, .9
        elevation : 2
        pos_hint:{"center_x":.5,"center_y":.5}

        orientation: "vertical"
        padding: dp(50)
        MDLabel:
            text: "Login"
            font_style: "H3"
            size_hint: 1, .2

            pos_hint:{"center_x":.5,"center_y":.5}
        MDTextField:
            id: uname
            hint_text:"Enter your username or email"
            icon_left: "email"
        MDTextField:
            id: password
            hint_text:"Enter your password"

            icon_left: "key"
            password: True
        MDBoxLayout:
            size_hint: 1,.1
            MDRaisedButton:
                id: login
                text: "login"
                on_press: root.try_login()
                size_hint:.3,1
            MDLabel:
                size_hint: .3,1

```
# the python code for login function
```py
class LoginScreen(MDScreen):
    def try_login(self):
        log = self.ids.password.text
        if log == False:
            exit()
        print("User trying to login ")
        uname = self.ids.uname.text
        password = self.ids.password.text
        if uname != "mi":
            self.ids.uname.hint_text= "error username doesn't exist"


        else :
            if uname == "mi" and password != "mo1":
                self.ids.password.hint_text="error password incorrect"

            else:
                if uname == "mi" and password == "mo1":
                    self.parent.current = "DigitalScreen"


    pass

```
# adding the function of deeting and updating the data table using python in pycharm
```py 
 data_table= None
    def update(self):
        db = database_worker("new_file.db")
        query= "SELECT * From wordy order by topic"
        data= db.search(query)
        db.close()
        self.data_table.update_row_data(None,data)
    def delete(self):
        rows_checked = self.data_table.get_row_checks()
        print(rows_checked)
        db = database_worker("new_file.db")
        for r in rows_checked:
            id = r[0]
            query= f"delete from wordy  where id = {id} "
            db.run_save(query)
        db.close()
        self.update()



    def on_pre_enter(self, *args):

        self.data_table= MDDataTable(
            size_hint= (.5,.7),
            pos_hint= {"center_x":.5,"center_y":.5},
            use_pagination= False,
            check= True,
            background_color= "black",
            column_data= [("id",20),("name",30),("date",30),("share",30)]

        )
        self.data_table.bind(on_row_press=self.row_pressed)
        self.data_table.bind(on_check_press=self.check_pressed)

        self.add_widget(self.data_table)
        print("hello")
        self.update()

    def row_pressed(self,table,row):
        print("a row was pressed ",row.text)
        row.md_bg_color="#ffff00"


    def check_pressed(self,table,current_row):
        print("a row was checked ",current_row)


    #before the screen is shown this code runs

    pass
```
# Creating a the Table screen using kivymd library
```py
<TableScreen>:
    size: 500,500
    FitImage:
        source: "love.png"
    MDCard:
        size_hint: .5, .9
        elevation : 2
        pos_hint:{"center_x":.5,"center_y":.5}

        MDBoxLayout:
            orientation: "vertical"
            md_bg_color:"#B4A8BA"



            MDLabel:
                text:""
                size_hint_y:.55
                md_bg_color:"#B4A8BA"

            FloatLayout:

                MDRoundFlatIconButton:
                    id:containere
                    text: "search"


                    on_press: root.parent.current="TableScreen"


            MDRaisedButton:





                text: "Delete"


                on_press: root.delete()


```
# creating a function that saves the inputs entered in the sql database created
```py
class NEW(MDScreen):
    def save(self):
        uname = self.ids.unamee.text
        date = self.ids.date.text
        share = self.ids.share.text

        db = database_worker("new_file.db")

        query = f"INSERT into wordy (topic, date,share) values ('{uname}', '{date}', '{share}')"
        db.run_save(query)

        db.close()
        self.parent.current="TableScreen"

```
# Criteria D functionality



https://user-images.githubusercontent.com/112072887/224200809-06da8cc4-55cb-4342-ae01-996fcf496d82.mov




### Works Cited



[^1]:https://docs.google.com/presentation/d/1k41YyEAyK55seezfsiWFLbTviNKkhPw58PTaGJcqjpo/edit#slide=id.g113dea6e35a_0_9)
[^2]:https://www.pythonguis.com/faq/which-python-gui-library/#:~:text=While%20most%20other%20GUI%20frameworks,is%20the%20way%20to%20go.
[^3]:https://www.businessnewsdaily.com/5804-what-is-sql.html#:~:text=Its%20portability%20makes%20it%20a,retrieve%20it%20quickly%20and%20efficiently.
[^4]:https://www.freecodecamp.org/news/using-sqlite-databases-with-python/#:~:text=SQLite%20is%20a%20very%20easy,projects%2C%20or%20testing%20and%20development.


