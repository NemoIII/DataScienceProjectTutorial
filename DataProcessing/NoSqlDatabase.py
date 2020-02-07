# Import the python libraries
from pymongo import MongoClient
from pprint import pprint

# Choose the appropriate client
client = MongoClient()

# Connect to the test db 
db=client.test

# Use the employee collection
employee = db.employee
'''Inserting Data'''
employee_details = {
    'Name': 'Raj Kumar',
    'Address': 'Sears Streer, NZ',
    'Age': '42'
}

# Use the insert method
# result = employee.insert_one(employee_details)

# Updating Data
db.employee.update_one(
        {"Age":'42'},
        {
        "$set": {
            "Name":"Srinidhi",
            "Age":'35',
            "Address":"New Omsk, WC"
        }
        }
    )

# Query for the inserted document.
# Queryresult = employee.find_one({'Age': '42'})

# Queryresult = employee.find_one({'Age':'35'})

# pprint(Queryresult)

# Deleting Data
db.employee.delete_one({'Age': '35'})
Queryresult = employee.find_one({'Age': '35'})
pprint(Queryresult)
