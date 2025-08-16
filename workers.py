from peewee import *
from core.models.base import BaseModel
import datetime

class Worker(BaseModel):
    name = CharField()
    phone = CharField(null=True)
    wage_type = CharField(choices=["daily", "monthly", "per_m2"])
    wage_rate = FloatField()
    active_from = DateField(default=datetime.date.today)
    active_to = DateField(null=True)

class Attendance(BaseModel):
    worker = ForeignKeyField(Worker, backref='attendance')
    date = DateField()
    present = BooleanField(default=True)
    note = TextField(null=True)



