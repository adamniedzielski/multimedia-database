
import wx

class DirectoriesDialog(wx.Dialog):

  def __init__(self):
    wx.Dialog.__init__(self, None, -1)
    self._init_ui()

  def _init_ui(self):
    self.panel = wx.Panel(self)
    vertical_box = wx.BoxSizer(wx.VERTICAL)
    social_label = wx.StaticText(self.panel, label = "Sign In using your account with")
    vertical_box.Add(social_label, 0, wx.TOP | wx.EXPAND, 40)
    self.panel.SetSizer(vertical_box)
    vertical_box.Fit(self)

