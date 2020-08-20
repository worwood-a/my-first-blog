from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Open the web page
        self.browser.get('http://127.0.0.1:8000')

        # Header is "CS Assignment"
        self.assertIn('CS Assignment', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('CS Assignment', header_text)

        # Input Box Appears
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a To-Do Item')

        # You Type "Finish This Assignment You Freak" because you haven't finished the assignment yet
        inputbox.send_keys('Finish This Assignment You Freak')

        # You hit enter and the site updates to berate you for not having finished the assignment yet
        inputbox.send_keys(Key.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Finish This Assignment You Freak' for row in rows))

        # There's another text box and this time you enter "Stop Being Depressed"
        self.fail("Finish the test!")

if __name__=='__main__':
    unittest.main(warnings='ignore')

browser.quit()