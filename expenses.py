from peewee import *
from core.models.base import BaseModel
import datetime

class Expense(BaseModel):
    type = CharField()
    amount = FloatField()
    date = DateField(default=datetime.date.today)
    note = TextField(null=True)



