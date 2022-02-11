from peewee import *

db = SqliteDatabase('Lab_5/records.sqlite')

class Records(Model):
    name = CharField()
    country = CharField()
    number_of_catches = IntegerField()

    class Meta():
        database = db

    def __str__(self):
        return f'ID: {self.id} Name: {self.name}, Country: {self.country}, Number of Catches: {self.number_of_catches}'

db.connect()
db.create_tables([Records])


