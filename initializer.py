
from directories_dialog import *
import wx

app = wx.App()
dialog = DirectoriesDialog()
dialog.ShowModal()
app.MainLoop()
