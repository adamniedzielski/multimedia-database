
import wx
from controllers.directories_controller import *

class MainWindow(wx.Frame):

  def __init__(self, router):
    wx.Frame.__init__(self, None, -1)
    self._init_ui()
    self.router = router

  def _init_ui(self):
    self._init_menu()

    self.panel = wx.Panel(self)
    vertical_box = wx.BoxSizer(wx.VERTICAL)

    self.panel.SetSizer(vertical_box)
    vertical_box.Fit(self)

    self.SetTitle('Multimedia database')
    self.SetSize((500, 500))
    self.Centre()

  def _init_menu(self):
    menu_bar = wx.MenuBar()
    settings_menu = wx.Menu()
    paths_item = settings_menu.Append(0, 'Search paths', 'Search paths')
    menu_bar.Append(settings_menu, 'Settings')
    self.SetMenuBar(menu_bar)
    self.Bind(wx.EVT_MENU, self._show_directories_dialog, paths_item)

  def _show_directories_dialog(self, event):
    self.router.directories.show()
