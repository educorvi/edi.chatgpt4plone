# -*- coding: utf-8 -*-
from edi.chatgpt4plone.content.chat_g_p_t_window import IChatGPTWindow  # NOQA E501
from edi.chatgpt4plone.testing import EDI_CHATGPT4PLONE_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class ChatGPTWindowIntegrationTest(unittest.TestCase):

    layer = EDI_CHATGPT4PLONE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_chat_g_p_t_window_schema(self):
        fti = queryUtility(IDexterityFTI, name='ChatGPT Window')
        schema = fti.lookupSchema()
        self.assertEqual(IChatGPTWindow, schema)

    def test_ct_chat_g_p_t_window_fti(self):
        fti = queryUtility(IDexterityFTI, name='ChatGPT Window')
        self.assertTrue(fti)

    def test_ct_chat_g_p_t_window_factory(self):
        fti = queryUtility(IDexterityFTI, name='ChatGPT Window')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IChatGPTWindow.providedBy(obj),
            u'IChatGPTWindow not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_chat_g_p_t_window_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='ChatGPT Window',
            id='chat_g_p_t_window',
        )

        self.assertTrue(
            IChatGPTWindow.providedBy(obj),
            u'IChatGPTWindow not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('chat_g_p_t_window', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('chat_g_p_t_window', parent.objectIds())

    def test_ct_chat_g_p_t_window_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='ChatGPT Window')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_chat_g_p_t_window_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='ChatGPT Window')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'chat_g_p_t_window_id',
            title='ChatGPT Window container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
