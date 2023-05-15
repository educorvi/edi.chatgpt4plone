# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s edi.chatgpt4plone -t test_chat_g_p_t_window.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src edi.chatgpt4plone.testing.EDI_CHATGPT4PLONE_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/edi/chatgpt4plone/tests/robot/test_chat_g_p_t_window.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a ChatGPT Window
  Given a logged-in site administrator
    and an add ChatGPT Window form
   When I type 'My ChatGPT Window' into the title field
    and I submit the form
   Then a ChatGPT Window with the title 'My ChatGPT Window' has been created

Scenario: As a site administrator I can view a ChatGPT Window
  Given a logged-in site administrator
    and a ChatGPT Window 'My ChatGPT Window'
   When I go to the ChatGPT Window view
   Then I can see the ChatGPT Window title 'My ChatGPT Window'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add ChatGPT Window form
  Go To  ${PLONE_URL}/++add++ChatGPT Window

a ChatGPT Window 'My ChatGPT Window'
  Create content  type=ChatGPT Window  id=my-chat_g_p_t_window  title=My ChatGPT Window

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the ChatGPT Window view
  Go To  ${PLONE_URL}/my-chat_g_p_t_window
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a ChatGPT Window with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the ChatGPT Window title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
