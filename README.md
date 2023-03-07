# Unit_3: project of creating a blog for my client 

![](https://github.com/24536urdj/Unit_3/blob/main/Project_unit_3/dd36613d-aaf4-4c07-acd1-0026086aa5bd.gif)
## Criteria A

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

## Criteria B
### system diagram
![GUI (1)](https://user-images.githubusercontent.com/112072887/222308800-dbecfa66-055b-4749-8c4b-3e71ed7211c4.png)


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


### Works Cited
[^1]:https://docs.google.com/presentation/d/1k41YyEAyK55seezfsiWFLbTviNKkhPw58PTaGJcqjpo/edit#slide=id.g113dea6e35a_0_9)
[^2]:https://www.pythonguis.com/faq/which-python-gui-library/#:~:text=While%20most%20other%20GUI%20frameworks,is%20the%20way%20to%20go.
[^3]:https://www.businessnewsdaily.com/5804-what-is-sql.html#:~:text=Its%20portability%20makes%20it%20a,retrieve%20it%20quickly%20and%20efficiently.


