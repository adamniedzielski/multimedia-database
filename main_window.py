
import wx
from directories_controller import *

class MainWindow(wx.Frame):

  def __init__(self, router):
    wx.Frame.__init__(self, None, -1)
    self._init_ui()
    self.router = router

  def _init_ui(self):
    self.panel = wx.Panel(self)
    vertical_box = wx.BoxSizer(wx.VERTICAL)

    button = wx.Button(self.panel, label = "Directories dialog")
    button.Bind(wx.EVT_BUTTON, self._show_directories_dialog)

    vertical_box.Add(button, 0, wx.TOP | wx.EXPAND, 40)
    self.panel.SetSizer(vertical_box)
    vertical_box.Fit(self)

    self.SetTitle('Multimedia database')
    self.SetSize((500, 500))
    self.Centre()
    self.Show(True)

  def _show_directories_dialog(self, event):
    self.router.directories.show()
