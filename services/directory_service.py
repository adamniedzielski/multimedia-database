
import os
import os.path
from models.directory import *
from models.file import *

class DirectoryService:

  def __init__(self, router):
    self.router = router

  def add_new_directory(self, path):
    directory = Directory.create(path = path)
    self.refresh_files(directory)

  def delete(self, directory):
    for file in list(directory.files):
      file.delete_instance()
    directory.delete_instance()
    self.router.files.update_view()

  def refresh_files(self, directory):
    self._remove_missing_files(directory)
    self._add_new_files(directory)
    self.router.files.update_view()

  def _remove_missing_files(self, directory):
    for file in list(directory.files):
      if not os.path.isfile(os.path.join(directory.path, file.name)):
        file.delete_instance()

  def _add_new_files(self, directory):
    for entry in os.listdir(directory.path):
      if os.path.isfile(os.path.join(directory.path, entry)):
        File.create(directory = directory, name = entry)
