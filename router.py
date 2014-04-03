
from controllers.directories_controller import *
from controllers.files_controller import *

class Router:

  def __init__(self):
    self.directories = DirectoriesController(self)
    self.files = FilesController(self)
