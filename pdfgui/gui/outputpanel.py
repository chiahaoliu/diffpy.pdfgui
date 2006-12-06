#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# generated by wxGlade 0.4.1 on Wed Dec  6 14:16:15 2006

import wx
from pdfpanel import PDFPanel

class OutputPanel(wx.Panel,PDFPanel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: OutputPanel.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.sizer_2_staticbox = wx.StaticBox(self, -1, "")
        self.outputLabel = wx.StaticText(self, -1, "PDFfit2 Output")
        self.outputTextCtrl = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade
        self.__customProperties()

    def __set_properties(self):
        # begin wxGlade: OutputPanel.__set_properties
        self.outputLabel.SetFont(wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: OutputPanel.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.StaticBoxSizer(self.sizer_2_staticbox, wx.HORIZONTAL)
        sizer_2.Add(self.outputLabel, 0, wx.ALL|wx.ADJUST_MINSIZE, 5)
        sizer_1.Add(sizer_2, 0, wx.ALL|wx.EXPAND, 5)
        sizer_1.Add(self.outputTextCtrl, 1, wx.ALL|wx.EXPAND|wx.ADJUST_MINSIZE, 5)
        self.SetAutoLayout(True)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        sizer_1.SetSizeHints(self)
        # end wxGlade

    def __customProperties(self):
        """Set the custom properties."""
        # Set the font to monospace
        font = self.outputTextCtrl.GetFont()
        font = wx.Font(font.GetPointSize(), wx.FONTFAMILY_TELETYPE,
                font.GetWeight(), font.GetStyle(), font.GetUnderlined())
        self.outputTextCtrl.SetFont(font)
        return

    def refresh(self):
        pass

# end of class OutputPanel


