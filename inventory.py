from peewee import *
from core.models.base import BaseModel

class Material(BaseModel):
    name = CharField(unique=True)
    type = CharField()
    length_m = FloatField(null=True)
    width_m = FloatField(null=True)
    thickness_mm = FloatField(null=True)
    buy_price_m2 = FloatField()
    sell_price_m2 = FloatField()
    qty_unit = CharField(choices=["slab", "m2"])
    qty_value = FloatField()
    supplier = CharField(null=True)
    low_stock_threshold = FloatField(default=0)

class StockMove(BaseModel):
    material = ForeignKeyField(Material, backref='stock_moves')
    qty_change_m2 = FloatField()
    note = TextField(null=True)
    source = CharField(choices=["purchase", "invoice", "adjustment"])
    attachment_path = CharField(null=True)



