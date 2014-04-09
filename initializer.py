
from router import *
import wx
from refresher import *

app = wx.App()
router = Router()

refresher = Refresher(router)
refresher.start()

router.files.show()
app.MainLoop()
