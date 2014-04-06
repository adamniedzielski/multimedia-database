
import os.path
import subprocess
from views.main_window import *
from models.file import *

class FilesController:

  def __init__(self, router):
    self.router = router
    self._search_term = ""

  def show(self):
    self.view = MainWindow(self.router)
    self.view.set_files(self._files())
    self.view.Show(True)

  def update_view(self):
    self.view.set_files(self._files())

  def filter(self, search_term):
    self._search_term = search_term
    self.update_view()

  def open(self, name, directory):
    file = os.path.join(directory, name)
    subprocess.call(["xdg-open", file])

  def _files(self):
    query = '%' + self._search_term + '%'
    files = File.select().where(File.name ** query | File.artist ** query | File.title ** query | File.album ** query).execute()
    return files
