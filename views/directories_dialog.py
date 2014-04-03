
import wx

class DirectoriesDialog(wx.Dialog):

  def __init__(self, router):
    wx.Dialog.__init__(self, None, -1)
    self._init_ui()
    self.router = router

  def _init_ui(self):
    self.panel = wx.Panel(self)
    main_box = wx.BoxSizer(wx.HORIZONTAL)
    self.listbox = wx.ListBox(self, size = (600, 250))

    main_box.Add(self.listbox, 0, wx.ALL | wx.EXPAND, 10)
    main_box.Add(self._buttons_sizer(), 0, wx.ALL | wx.EXPAND, 10)

    self.panel.SetSizer(main_box)
    main_box.Fit(self)

    self.SetTitle("Search paths")
    self.SetSize((800, 270))

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

  def _buttons_sizer(self):
    vertical_box = wx.BoxSizer(wx.VERTICAL)

    add_button = wx.Button(self, label = "Add directory")
    add_button.Bind(wx.EVT_BUTTON, self._on_add)

    delete_button = wx.Button(self, label = "Delete")
    delete_button.Bind(wx.EVT_BUTTON, self._on_delete)

    vertical_box.Add(add_button, 0, wx.ALL | wx.EXPAND, 2)
    vertical_box.Add(delete_button, 0, wx.ALL | wx.EXPAND, 2)

    return vertical_box
