
from directories_dialog import *
from directory import *

class DirectoriesController:

  def __init__(self, router):
    self.router = router

  def create(self, path):
    if Directory.select().where(Directory.path == path).count() == 0:
      Directory.create(path = path)
      self.view.set_directories(self._directories())

  def show(self):
    self.view = DirectoriesDialog(self.router)
    self.view.set_directories(self._directories())
    self.view.ShowModal()
    self.view.Destroy()

  def delete(self, directory):
    directory.delete_instance()
    self.view.set_directories(self._directories())

  def _directories(self):
    return Directory.select().execute()
