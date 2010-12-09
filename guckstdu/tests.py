from selenium import selenium
import unittest, time, re

class AdminLogin(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://guckstdu.frog32.ch/")
        self.selenium.start()
    
    def test_untitled(self):
        sel = self.selenium
        sel.open("/admin/")
        sel.type("id_username", "guckstdu")
        sel.type("id_password", "test1234")
        sel.click("//input[@value='Anmelden']")
        sel.wait_for_page_to_load("30000")
        try: self.failUnless(sel.is_text_present("Willkommen"))
        except AssertionError, e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
