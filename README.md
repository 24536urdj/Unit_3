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
| 1  | First meeting with client                             | meeting with mayte flores ,to discuss what app she would like me to develop                                             | Planning       | 7 minutes    |10 february        | A        |
| 2  | Write down success criteria                           | discussing my client success criteria and eliminating the unnecessary ones.                                                | Planning       | 7 minutes    | 13 February          | A        |
| 3  | finalizing the success criteria                              |  Meeting with Mayte to show her the finalized success criteria and get her consent to start | Planning       | 10 minutes        | 16 feb           | A        |
| 4  | Write down the problem definition                              | state a detailed version of the problem and identify  the client                         | Planning       | 30 minutes    | 14 March          | A        |
| 5  | Meet with client to  present the success criteria     | Present success criteria to client to get the approval                                     | Planning       | 30 minutes    | 19 March          | A        |
| 6  | Research and write rationale for proposed solution    | Finish rationale for proposed solution                                                     | Planning       | 2 hours       | 20 March          | A        |
| 7  | Starts working on login and registration system       | Finish login and registration system with database                                         | Development    | 1 day         | 23 March          | C        |
| 8  | Create wireframe diagram                              | Wireframe diagram is ready to present to client as the first MVP                           | Design         | 1 hour        | 24 March          | B        |
| 9  | Create system diagram                                 | System diagram is done with details written on it                                          | Design         | 2 hours       | 25 March          | B        |
| 10 | Working on password encryption                        | Using sha256 to encrypt password and check password in login and registration              | Development    | 1 hour        | 2 April           | C        |
| 11 | Create welcome screen following the wireframe diagram | Have welcome screen ready                                                                  | Development    | 2 hours       | 8 April           | C        |
| 12 | Present the wireframe and application to the client   | Get client's feedback on the wireframe and application                                     | Planning       | 30 minutes    | 9 April           | A        |
| 13 | Make ER diagram                                       | ER diagram is created for both tables                                                      | Planning       | 40 minutes    | 9 April           | B        |
| 14 | Update record of task                                 | Record of task is up to date                                                               | Planning       | 20 minutes    | 10 April          | B        |
| 15 | Create table to show diary                            | Table is created and can show every diary belongs to that specific user                    | Development    | 3 hours       | 14 April          | C        |
| 16 | Make new diary screen                                 | Allow user to create new diary in the application and can check their diary in the table   

### Works Cited
[^1]:https://docs.google.com/presentation/d/1k41YyEAyK55seezfsiWFLbTviNKkhPw58PTaGJcqjpo/edit#slide=id.g113dea6e35a_0_9)
[^2]:https://www.pythonguis.com/faq/which-python-gui-library/#:~:text=While%20most%20other%20GUI%20frameworks,is%20the%20way%20to%20go.
[^3]:https://www.businessnewsdaily.com/5804-what-is-sql.html#:~:text=Its%20portability%20makes%20it%20a,retrieve%20it%20quickly%20and%20efficiently.


