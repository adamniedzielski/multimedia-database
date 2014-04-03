
from views.main_window import *

class FilesController:

  def __init__(self, router):
    self.router = router

  def show(self):
    self.view = MainWindow(self.router)
    self.view.Show(True)
