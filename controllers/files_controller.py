
from views.main_window import *
from models.file import *

class FilesController:

  def __init__(self, router):
    self.router = router

  def show(self):
    self.view = MainWindow(self.router)
    self.view.set_files(self._files())
    self.view.Show(True)

  def update_view(self):
    self.view.set_files(self._files())

  def _files(self):
    return File.select().execute()
