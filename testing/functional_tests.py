from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

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
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_table('1: Finish This Assignment You Freak')

        # There's another text box and this time you enter "Stop Being Depressed"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Stop Being Depressed')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The site now shows two mean things you've said about yourself
        self.check_for_row_in_table('1: Finish This Assignment You Freak')
        self.check_for_row_in_table('2: Stop Being Depressed')

if __name__=='__main__':
    unittest.main(warnings='ignore')

browser.quit()