
import wx
import wx.grid
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
    self._init_grid()

    play_button = wx.Button(self.panel, label = "Open and play", size = (300, 50))
    play_button.Bind(wx.EVT_BUTTON, self._on_search)

    vertical_box.Add(self._search_row(), 0, wx.ALL | wx.EXPAND, 10)
    vertical_box.Add(play_button, 0, wx.ALL, 10)
    vertical_box.Add(self.grid, 0, wx.ALL | wx.EXPAND, 10)

    self.panel.SetSizer(vertical_box)
    vertical_box.Fit(self)

    self.SetTitle('Multimedia database')
    self.SetSize((1000, 700))
    self.Maximize()
    self.Centre()

  def set_files(self, files):
    files = list(files)

    old_size = self.grid.GetNumberRows()
    new_size = len(files)

    if old_size < new_size:
      self.grid.AppendRows(new_size - old_size)
    elif old_size > new_size:
      self.grid.DeleteRows(new_size, new_size - old_size, True)

    for i in range(len(files)):
      self.grid.SetCellValue(i, 0, files[i].name)
      self.grid.SetCellValue(i, 1, files[i].artist or "")
      self.grid.SetCellValue(i, 2, files[i].album or "")
      self.grid.SetCellValue(i, 3, files[i].title or "")
      self.grid.SetCellValue(i, 4, files[i].track_number or "")
      self.grid.SetCellValue(i, 5, files[i].duration or "")
      self.grid.SetCellValue(i, 6, files[i].directory.path or "")

    self.grid.AutoSize()

  def _init_menu(self):
    menu_bar = wx.MenuBar()
    settings_menu = wx.Menu()
    paths_item = settings_menu.Append(0, 'Search paths', 'Search paths')
    menu_bar.Append(settings_menu, 'Settings')
    self.SetMenuBar(menu_bar)
    self.Bind(wx.EVT_MENU, self._show_directories_dialog, paths_item)

  def _init_grid(self):
    self.grid = wx.grid.Grid(self.panel)
    self.grid.CreateGrid(0, 7)
    self.grid.SetColLabelValue(0, "Name")
    self.grid.SetColLabelValue(1, "Artist")
    self.grid.SetColLabelValue(2, "Album")
    self.grid.SetColLabelValue(3, "Title")
    self.grid.SetColLabelValue(4, "Track number")
    self.grid.SetColLabelValue(5, "Duration")
    self.grid.SetColLabelValue(6, "Directory")
    self.grid.EnableEditing(False)
    self.grid.SetSelectionMode(wx.grid.Grid.wxGridSelectRows)

  def _search_row(self):
    self.search_term = wx.TextCtrl(self.panel, size = (-1, 50))
    self.search_term.Bind(wx.EVT_TEXT, self._on_search)

    return self.search_term

  def _show_directories_dialog(self, event):
    self.router.directories.show()

  def _on_search(self, event):
    self.router.files.filter(self.search_term.GetValue())
