how many tables are in the database ? 
there are 4 tables 
How many Male inhabitants are Friendly?
there are 4 male inhabitants that are friendly 

```.py ###
    select count(*) from INHABITANT where gender = "Male" and state = "Friendly"
```
What is the average gold by village?
![Screen Shot 2023-03-16 at 21 52 17](https://user-images.githubusercontent.com/112072887/225622601-23c9a32c-5bad-4bf6-a171-86fb28971851.png)


```.py ###
    select AVG(gold) from INHABITANT group by villageid
```

  
    
  
