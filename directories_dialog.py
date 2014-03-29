
import wx

class DirectoriesDialog(wx.Dialog):

  def __init__(self, router):
    wx.Dialog.__init__(self, None, -1)
    self._init_ui()
    self.router = router

  def _init_ui(self):
    self.panel = wx.Panel(self)
    vertical_box = wx.BoxSizer(wx.VERTICAL)
    self.listbox = wx.ListBox(self, size = (200, -1))

    add_button = wx.Button(self, label = "Add directory")
    add_button.Bind(wx.EVT_BUTTON, self._on_add)

    delete_button = wx.Button(self, label = "Delete")
    delete_button.Bind(wx.EVT_BUTTON, self._on_delete)

    vertical_box.Add(self.listbox, 0, wx.TOP | wx.EXPAND, 40)
    vertical_box.Add(add_button, 0)
    vertical_box.Add(delete_button, 0)

    self.panel.SetSizer(vertical_box)
    vertical_box.Fit(self)
    self.SetSize((400, 400))

  def set_directories(self, directories):
    self.listbox.Clear()

    for directory in directories:
      self.listbox.Append(directory.path, directory)

  def _on_add(self, event):
    dialog = wx.DirDialog(self, "Choose a directory:")
    if dialog.ShowModal() == wx.ID_OK:
      self.router.directories.create(dialog.GetPath())
    dialog.Destroy()

  def _on_delete(self, event):
    selection = self.listbox.GetSelection()

    if selection != wx.NOT_FOUND:
      self.router.directories.delete(self.listbox.GetClientData(selection))

