from peewee import *
from core.models.base import BaseModel
from core.models.clients import Client
from core.models.inventory import Material
import datetime

class Invoice(BaseModel):
    client = ForeignKeyField(Client, backref='invoices')
    date = DateField(default=datetime.date.today)
    type = CharField(choices=["sale", "install", "both"])
    delivery_fee_billed = FloatField(default=0.0)
    delivery_cost_actual = FloatField(default=0.0)
    install_fee_billed = FloatField(default=0.0)
    discount_rate = FloatField(default=0.0)
    tax_rate = FloatField(default=0.0)
    subtotal = FloatField(default=0.0)
    tax_amount = FloatField(default=0.0)
    total = FloatField(default=0.0)
    profit_margin = FloatField(default=0.0)
    note = TextField(null=True)
    status = CharField(choices=["draft", "posted", "corrected"], default="draft")
    reference = CharField(null=True)
    corrections_of = ForeignKeyField('self', null=True, backref='corrections')

class InvoiceItem(BaseModel):
    invoice = ForeignKeyField(Invoice, backref='items')
    material = ForeignKeyField(Material, backref='invoice_items')
    pieces = FloatField(default=1.0)
    length_m = FloatField(null=True)
    width_m = FloatField(null=True)
    thickness_mm = FloatField(null=True)
    area_m2 = FloatField(default=0.0)
    buy_price_m2 = FloatField(default=0.0)
    sell_price_m2 = FloatField(default=0.0)



