from mongoengine import *



"""
Use DynamicDocument instead Document because a document in companies collection has a many field and if use Document class you need specify each field
"""


class Company(DynamicDocument):
    name = StringField(required=True)
    number_of_employees = IntField(required=True)
    description = StringField()

    meta = {
        #Collection name
        'collection':'companies'
    }
