# -*- coding: utf-8 -*-
# from plone.app.textfield import RichText
# from plone.autoform import directives
from plone.dexterity.content import Container
from plone.supermodel import model
# from plone.supermodel.directives import fieldset
from zope import schema
from zope.interface import implementer


from edi.chatgpt4plone import _


class IChatGPTWindow(model.Schema):
    """ Marker interface and Dexterity Python Schema for ChatGPTWindow
    """

    sockethost = schema.TextLine(title=_("Host-IP or DNS-Name of sockethost"), default="127.0.0.1", required=True)
    socketport = schema.TextLine(title=_("Portnumber of socketserver"), default="8765", required=True)

    # If you want, you can load a xml model created TTW here
    # and customize it in Python:

    # model.load('chat_g_p_t_window.xml')

    # directives.widget(level=RadioFieldWidget)
    # level = schema.Choice(
    #     title=_(u'Sponsoring Level'),
    #     vocabulary=LevelVocabulary,
    #     required=True
    # )

    # text = RichText(
    #     title=_(u'Text'),
    #     required=False
    # )

    # url = schema.URI(
    #     title=_(u'Link'),
    #     required=False
    # )

    # fieldset('Images', fields=['logo', 'advertisement'])
    # logo = namedfile.NamedBlobImage(
    #     title=_(u'Logo'),
    #     required=False,
    # )

    # advertisement = namedfile.NamedBlobImage(
    #     title=_(u'Advertisement (Gold-sponsors and above)'),
    #     required=False,
    # )

    # directives.read_permission(notes='cmf.ManagePortal')
    # directives.write_permission(notes='cmf.ManagePortal')
    # notes = RichText(
    #     title=_(u'Secret Notes (only for site-admins)'),
    #     required=False
    # )


@implementer(IChatGPTWindow)
class ChatGPTWindow(Container):
    """
    """
