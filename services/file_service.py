
import os.path
import eyed3
from models.file import *

class FileService:

  def add_new_file(self, directory, name):
    audiofile = eyed3.load(os.path.join(directory.path, name))
    File.create(directory = directory,
                name = name,
                artist = audiofile.tag.artist,
                album = audiofile.tag.album,
                title = audiofile.tag.title,
                track_number = audiofile.tag.track_num[0],
                duration = self._format_duration(audiofile.info.time_secs)
                )

  def _format_duration(self, seconds):
    if seconds:
      return str(seconds / 60) + ":" + str(seconds % 60).zfill(2)
    else:
      return seconds 

