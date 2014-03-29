
from directory import *

Directory.create(path = "test")
for directory in Directory.select():
  print directory.id
