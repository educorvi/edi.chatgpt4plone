from plone.autoform import directives
from plone import schema
from zope.interface import Interface
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from zope.interface import Invalid
from zope.interface import invariant
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.restapi.controlpanels import RegistryConfigletPanel
from zope.component import adapter
from plone.z3cform import layout
from z3c.form import form

from edi.chatgpt4plone import _

data_sources = SimpleVocabulary(
    [SimpleTerm(value=u'catalog', title=_(u'Portal Catalog')),
     SimpleTerm(value=u'elastic', title=_(u'Elastic Search'))])

models = SimpleVocabulary(
    [SimpleTerm(value=u'gpt-3.5-turbo', title=_(u'GPT 3.5-Turbo')),
     SimpleTerm(value=u'gpt-4', title=_(u'GPT 4'))])

class IChatGPTConfig(Interface):

    datasource = schema.Choice(title=_("Data Source"),
            description=_("The source of own data the ChatGPT should query."),
            vocabulary=data_sources,
            default='catalog',
            required=True)

    sourceurl = schema.URI(title=_("URL of Data Source"),
            description=_("Complete URL of Data Source if source its not Portal Catalog"),
            default="http://127.0.0.1:9200",
            required=False)

    index = schema.TextLine(title=_("Name of Index if source its not Portal Catalog"),
            required=False)

    resultcount = schema.Int(title=_("These number of searchresults should be used for generating the answer. Please remember:\
            the costs increase with the amount of results."),
            default=10,
            required=True)

    temperatur = schema.Int(title=_("A marker for creativity while generating answers. 0 means: create your answer from results only"),
            default=0,
            required=True)

    openai_apikey = schema.TextLine(title=_("OpenAI API Key"),
            required=True)

    summarize_model = schema.Choice(title=_("Model for the summary of own text data"),
            default='gpt-3.5-turbo',
            vocabulary=models,
            required=True)

    chat_model = schema.Choice(title=_("Model for answering questions with ChatGPT"),
            default='gpt-3.5-turbo',
            vocabulary=models,
            required=True)

    sockethost = schema.TextLine(title=_("URI of websocket server"),
            description=_("Host and portnumber will be connected from clients browser, take care about network connection and firewall entries"),
            default='ws://entwicklung.educorvi.de',
            required=True)

    socketport = schema.Int(title=_("Port of websocket server"),
            default=8765,
            required=True)


    @invariant
    def source_invariant(data):
        if data.datasource != 'catalog':
            if not sourceurl or not index:
                raise Invalid(_(u'For choosen data source you must enter Complete URL and Name of Index.'))


class ChatGPTPanelForm(RegistryEditForm):
    form.extends(RegistryEditForm)
    schema = IChatGPTConfig

ChatGPTControlPanelView = layout.wrap_form(ChatGPTPanelForm, ControlPanelFormWrapper)
ChatGPTControlPanelView.label = u"ChatGPT for Plone Settings"
