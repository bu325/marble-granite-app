from peewee import *
import datetime

db = SqliteDatabase("marble_granite.db")

class BaseModel(Model):
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)
    version = IntegerField(default=1)
    is_deleted = BooleanField(default=False)

    class Meta:
        database = db

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        if self.id:  # Only increment version if updating existing record
            self.version += 1
        super(BaseModel, self).save(*args, **kwargs)



