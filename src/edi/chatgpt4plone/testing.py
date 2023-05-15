# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import edi.chatgpt4plone


class EdiChatgpt4PloneLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=edi.chatgpt4plone)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'edi.chatgpt4plone:default')


EDI_CHATGPT4PLONE_FIXTURE = EdiChatgpt4PloneLayer()


EDI_CHATGPT4PLONE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EDI_CHATGPT4PLONE_FIXTURE,),
    name='EdiChatgpt4PloneLayer:IntegrationTesting',
)


EDI_CHATGPT4PLONE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EDI_CHATGPT4PLONE_FIXTURE,),
    name='EdiChatgpt4PloneLayer:FunctionalTesting',
)


EDI_CHATGPT4PLONE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        EDI_CHATGPT4PLONE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='EdiChatgpt4PloneLayer:AcceptanceTesting',
)
