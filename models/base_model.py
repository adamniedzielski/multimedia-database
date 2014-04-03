
from peewee import *

database = SqliteDatabase('audio.db')

class BaseModel(Model):
  class Meta:
    database = database
