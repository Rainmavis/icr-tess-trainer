#Boa:Frame:Frame1

import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAME1] = [wx.NewId() for _init_ctrls in range(1)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        wx.Frame.__init__(self, style=wx.DEFAULT_FRAME_STYLE, name='', parent=prnt, title='Frame1', pos=(480, 245), id=wxID_FRAME1, size=(1280, 653))

    def __init__(self, parent):
        self._init_ctrls(parent)
