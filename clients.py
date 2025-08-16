from peewee import *
from core.models.base import BaseModel

class Client(BaseModel):
    name = CharField()
    phone = CharField(null=True)
    address = TextField(null=True)
    notes = TextField(null=True)



