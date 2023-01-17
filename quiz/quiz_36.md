###
              class Person :
            def __init__(self,name : str, age:int ):
                self.name = name
                self.age = age
            def get_name(self):
                return self.name
            def get_age(self):
                return self.age
        class Student(Person) :
            def __init__(self,grade,name,age ):
                self.grade = grade
                super().__init__(name= name,age = age)
            def get_grade(self):
                return self.grade
        laila = Student(name ="leila ",age = "16",grade = "G10" )
        print(f"{laila.get_name()}is a student,she is {laila.get_age()},and she is currently a {laila.get_grade()}")

![Screen Shot 2023-01-17 at 13 43 54](https://user-images.githubusercontent.com/112072887/212811802-ea3b6aa9-311a-4184-95fd-dee2904186a6.png)



