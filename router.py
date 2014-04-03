
from directories_controller import *
from files_controller import *

class Router:

  def __init__(self):
    self.directories = DirectoriesController(self)
    self.files = FilesController(self)
