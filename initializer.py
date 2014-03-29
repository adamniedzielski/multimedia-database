
from main_window import *
from router import *
import wx

app = wx.App()
MainWindow(Router())
app.MainLoop()
