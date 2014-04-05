from base_model import *
from directory import *

class File(BaseModel):
  name = CharField()
  artist = CharField(null = True)
  album = CharField(null = True)
  title = CharField(null = True)
  track_number = CharField(null = True)
  duration = CharField(null = True)
  directory = ForeignKeyField(Directory, related_name = 'files')
