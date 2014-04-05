
from peewee import *

database = SqliteDatabase('audio.db', threadlocals = True)

class BaseModel(Model):
  class Meta:
    database = database
