from base_model import *
from directory import *

class File(BaseModel):
  name = CharField()
  directory = ForeignKeyField(Directory, related_name = 'files')
