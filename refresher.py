
from models.directory import *
from services.directory_service import *
from database import *

import threading
import time
import wx
from wx.lib.pubsub import Publisher

class Refresher(threading.Thread):

  def __init__(self, router):
    threading.Thread.__init__(self)
    self.setDaemon(True)
    self.router = router

  def run(self):
    while True:
      time.sleep(5)
      print "checking..."
      
      Database.access.acquire()
      refreshed = 0
      for directory in list(Directory.select().execute()):
        refreshed += DirectoryService(self.router).refresh_files(directory)

      if refreshed > 0:
        wx.CallAfter(Publisher().sendMessage, "refresh")

      Database.access.release()


