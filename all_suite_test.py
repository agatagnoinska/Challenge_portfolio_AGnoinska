import unittest

from unittest.loader import makeSuite

from test_cases.SCOUT_01_login_to_the_system import TestLogInToSystem
from test_cases.SCOUT_02_login_to_the_system_negative import TestLogInToSystemWrong
from test_cases.SCOUT_03_change_language_loginpage import TestChangeLanguageLoginPage
from test_cases.SCOUT_04_add_player import TestAddingPlayer
from test_cases.SCOUT_05_clear_add_a_player_form import TestClearButton
from test_cases.framework import Test
from test_cases.title_of_add_a_player_page import TitleOfAddPlayerPage


def full_suite():
   test_suite = unittest.TestSuite()
   test_suite.addTest(makeSuite(TestLogInToSystem))
   test_suite.addTest(makeSuite(TestLogInToSystemWrong))
   test_suite.addTest(makeSuite(TestChangeLanguageLoginPage))
   test_suite.addTest(makeSuite(TestAddingPlayer))
   test_suite.addTest(makeSuite(TestClearButton))
   test_suite.addTest(makeSuite(TitleOfAddPlayerPage))
   return test_suite

if __name__ == '__main__':
   runner = unittest.TextTestRunner(verbosity=2)
   runner.run(full_suite())