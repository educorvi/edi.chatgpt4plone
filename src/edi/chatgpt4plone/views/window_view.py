# -*- coding: utf-8 -*-
from edi.chatgpt4plone import _
from Products.Five.browser import BrowserView
from websockets.sync.client import connect
from edi.chatgpt4plone.browser.controlpanel import IChatGPTConfig
from plone import api as ploneapi

class WindowView(BrowserView):

    def __call__(self):
        return self.index()
