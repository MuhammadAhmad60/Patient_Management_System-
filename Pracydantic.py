# this is just for practice 

from Pracydantic import BaseModel




class Patient(BaseModel):
    name: str
    age: int


def insert_patient_data(patient: Patient):
    print(Patient.name)
    print(Patient.age)
    print('inserted')


def update_patient_data(patient: Patient):
    print(Patient.name)
    print(Patient.age)
    print('Updated')



patient_info = {'name': 'ALI', 'age': 30}


patient1 = Patient(**patient_info)

update_patient_data(patient1)