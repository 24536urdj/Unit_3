###
        how many tables are in the database ? 
        there are 4 tables 
        How many Male inhabitants are Friendly?
        there are 4 male inhabitants that are friendly 

```.py ###
    select count(*) from INHABITANT where gender = "Male" and state = "Friendly"
```
What is the average gold by village?


```.py ###
    select AVG(gold) from INHABITANT group by villageid
    
```
![Screen Shot 2023-03-16 at 21 52 17](https://user-images.githubusercontent.com/112072887/225622601-23c9a32c-5bad-4bf6-a171-86fb28971851.png)
  
         How many items are there that start with the letter “A”
```.py
    select * from ITEM where item like "A%"
```


![Screen Shot 2023-03-16 at 21 57 30](https://user-images.githubusercontent.com/112072887/225623793-05f4e7f6-7abe-4351-9798-dc6ca63f1101.png)
        How many different jobs are there?
```.py
   select  distinct job  from INHABITANT
```
![Screen Shot 2023-03-16 at 22 06 43](https://user-images.githubusercontent.com/112072887/225626103-97b0d8b4-83f6-4fec-8d07-c1fa05db4025.png)
        What are the items owned by the herbalists?
```.py 
   select * from item where owner =4

```
![Screen Shot 2023-03-16 at 22 12 30](https://user-images.githubusercontent.com/112072887/225627513-c4c82a4e-26ad-47f5-8782-05dd569dc4aa.png)






   



