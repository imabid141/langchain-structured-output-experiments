from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = 'Abid'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5 , description= 'A decimal value representing the cgpa of the student')

new_student = {'age':30, 'email':'abc@gmail.com'}

student = Student(**new_student)

# Convert into Python dictionary
student_dict = dict(student)
print(student_dict['cgpa'])

# Convert into Json format
student_json = student.model_dump_json()
print(student_json)