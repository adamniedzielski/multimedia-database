
import os
import os.path
from models.directory import *
from file_service import *
from database import *

class DirectoryService:

  def __init__(self, router):
    self.router = router

  def add_new_directory(self, path):
    directory = Directory.create(path = path)
    self.refresh_files(directory)
    self.router.files.update_view()

  def delete(self, directory):
    Database.access.acquire()

    for file in list(directory.files):
      file.delete_instance()
    directory.delete_instance()
    self.router.files.update_view()

    Database.access.release()

  def refresh_files(self, directory):
    refreshed = self._remove_missing_files(directory)
    refreshed += self._add_new_files(directory)
    return refreshed

  def _remove_missing_files(self, directory):
    removed = 0
    for file in list(directory.files):
      if not os.path.isfile(os.path.join(directory.path, file.name)):
        removed += 1
        file.delete_instance()
    return removed

  def _add_new_files(self, directory):
    files = []

    for entry in os.listdir(directory.path):
      if os.path.isfile(os.path.join(directory.path, entry)) and self._is_mp3(entry):
        files.append(entry)

    new_files = set(files) - set(map(lambda file: file.name, directory.files))
    
    for file in new_files:
      FileService().add_new_file(directory, file)
    
    return len(new_files)

  def _is_mp3(self, name):
    return name.endswith(".mp3")
