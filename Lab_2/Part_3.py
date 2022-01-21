# Part 3: Student dataclass
# Type in the dataclass code from the slides/video. You would have done this before class.
# Add one more field: gpa, a float.
# Write a main function to create some example Student objects with some example names, college_id and GPA values. 
# Verify you can read the name, college ID and GPA for an example student.  Verify when you print an example student, the GPA is included. 
# Add some comments in your code to compare the dataclass version to the "traditional" version.

#I noticed that using the dataclass version is more straightforward, easier and more readable than
#the traditional way 

from dataclasses import dataclass


@dataclass
class Student:
    name : str
    college_id : str
    gpa : float

    def __str__(self):
        return f'Name: {self.name}, id: {self.college_id}, gpa: {self.gpa}'

def main():
    
    alice = Student('Alice', 'aa1234aa', 3.6)
    bob = Student('Bob', 'bb1234bb', 2.6)
    james = Student('James', 'jj123', 4.0)

    print(alice.name)
    print(bob.college_id)
    print(james.gpa)

    print(alice)
    print(bob)
    print(james)

main()

