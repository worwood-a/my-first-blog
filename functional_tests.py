from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

'''
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

        # You Type "Unfinished assignment" because you haven't finished the assignment yet
        inputbox.send_keys('Unfinished assignment')

        # You hit enter and the site updates to berate you for not having finished the assignment yet
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_table('1: Unfinished assignment')

        # There's another text box and this time you enter "second thing"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('second thing')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The site now shows two things you've said 
        self.check_for_row_in_table('1: Unfinished assignment')
        self.check_for_row_in_table('2: second thing')
'''

class CVEditorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
    
    def check_for_post_in_div(self, div_name, row_title, row_content):
        posts = self.browser.find_elements_by_name(div_name)
        self.assertIn(row_title, [post.find_element_by_tag_name('h3').text for post in posts])
        self.assertIn(row_content, [post.find_element_by_tag_name('p').text for post in posts])

    def test_can_access_cv_page(self):
        # Open the page on the blog page
        self.browser.get('http://127.0.0.1:8000')

        # Check the page title
        self.assertIn('CS Assignment', self.browser.title)

        # Check the header for the page links
        header_texts = self.browser.find_elements_by_tag_name('h1')
        self.assertIn('Blog | CV Page', [text.text for text in header_texts])

        # Click on the CV Page button
        page_link = self.browser.find_element_by_link_text('CV Page')
        page_link.click()

        # Check we're now on the CV Page
        headings = self.browser.find_elements_by_tag_name('h2')
        self.assertIn('Adam Worwood', [heading.text for heading in headings])
    
    def test_can_add_new_education(self):
        # Open the page on the blog page and navigate to the CV Page
        self.browser.get('http://127.0.0.1:8000')
        self.browser.find_element_by_link_text('CV Page').click()

        # Check for the "Add New Education" link and click on it
        education_link = self.browser.find_element_by_link_text('Add New Education')
        education_link.click()

        # Check for the input boxes
        name_box = self.browser.find_element_by_id('id_name')
        start_year_box = self.browser.find_element_by_id('id_start_year')
        end_year_box = self.browser.find_element_by_id('id_end_year')
        description_box = self.browser.find_element_by_id('id_description')

        # Enter some information
        name_box.send_keys('Test School')
        start_year_box.send_keys('2007')
        end_year_box.send_keys('2008')
        description_box.send_keys('Test Description')

        # Find the Save button
        save_button = self.browser.find_element_by_name('save_button')
        save_button.click()

        # Find new post
        self.check_for_post_in_div('education', 'Test School: 2007 - 2008', 'Test Description')

    def test_can_add_new_technical_skill(self):
        # Open the page on the blog page and navigate to the CV Page
        self.browser.get('http://127.0.0.1:8000')
        self.browser.find_element_by_link_text('CV Page').click()

        # Check for the "Add New Technical Skill" link and click on it
        technical_link = self.browser.find_element_by_link_text('Add New Technical Skill')
        technical_link.click()

        # Check for the input boxes
        title_box = self.browser.find_element_by_id('id_title')
        content_box = self.browser.find_element_by_id('id_content')

        # Enter some information
        title_box.send_keys('Test Tech Skill')
        content_box.send_keys('Test Content')

        # Find the Save button
        save_button = self.browser.find_element_by_name('save_button')
        save_button.click()

        # Find new post
        self.check_for_post_in_div('technical', 'Test Tech Skill', 'Test Content')

    def test_can_add_new_work_experience(self):
        # Open the page on the blog page and navigate to the CV Page
        self.browser.get('http://127.0.0.1:8000')
        self.browser.find_element_by_link_text('CV Page').click()

        # Check for the 'Add New Work Experience' link and click on it
        work_link = self.browser.find_element_by_link_text('Add New Work Experience')
        work_link.click()

        # Check for the input boxes
        title_box = self.browser.find_element_by_id('id_title')
        start_year_box = self.browser.find_element_by_id('id_start_year')
        end_year_box = self.browser.find_element_by_id('id_end_year')
        description_box = self.browser.find_element_by_id('id_description')

        # Enter some information
        title_box.send_keys('Test Work Experience')
        start_year_box.send_keys('1950')
        end_year_box.send_keys('1955')
        description_box.send_keys('Test Description')

        # Find the Save button
        save_button = self.browser.find_element_by_name('save_button')
        save_button.click()

        # Find new post
        self.check_for_post_in_div('work', 'Test Work Experience: 1950 - 1955', 'Test Description')

    def test_can_add_new_interest_or_skill(self):
        # Open the page on the blog page and navigate to the CV Page
        self.browser.get('http://127.0.0.1:8000')
        self.browser.find_element_by_link_text('CV Page').click()

        # Check for the 'Add New Interest Or Skill' link and click on it
        interest_link = self.browser.find_element_by_link_text('Add New Interest or Skill')
        interest_link.click()

        # Check for the input boxes
        name_box = self.browser.find_element_by_id('id_name')
        content_box = self.browser.find_element_by_id('id_content')

        # Enter some information
        name_box.send_keys('Test Interest')
        content_box.send_keys('Test Content')

        # Find the Save button
        save_button = self.browser.find_element_by_name('save_button')
        save_button.click()

        #Find new post
        self.check_for_post_in_div('other', 'Test Interest', 'Test Content')

    def clear_input_box(self, input_box):
        text_length = len(input_box.get_attribute('value'))
        for i in range(0, text_length+1):
            input_box.send_keys(Keys.BACKSPACE)
            input_box.send_keys(Keys.DELETE)

    def test_cannot_enter_invalid_start_end_years(self):
        # Open the blog page and navigate to the education form
        self.browser.get('http://127.0.0.1:8000')
        self.browser.find_element_by_link_text('CV Page').click()
        self.browser.find_element_by_link_text('Add New Education').click()

        # Find the input boxes and the save button
        name_box = self.browser.find_element_by_id('id_name')
        start_year_box = self.browser.find_element_by_id('id_start_year')
        end_year_box = self.browser.find_element_by_id('id_end_year')
        description_box = self.browser.find_element_by_id('id_description')
        save_button = self.browser.find_element_by_name('save_button')

        # Enter information, with the start year being < 1900, then attempt to save
        name_box.send_keys('Invalid Education')
        start_year_box.send_keys('1899')
        end_year_box.send_keys('2000')
        description_box.send_keys('This should not be here')
        save_button.click()

        # Verify we're on the same page by looking for the save button (if we're on the cv page this will throw an error)
        save_button = self.browser.find_element_by_name('save_button')

        # Adjust the current data in the start_year box
        start_year_box = self.browser.find_element_by_id('id_start_year')
        self.clear_input_box(start_year_box)

        # Enter new start year higher than the current year and attempt to save
        start_year_box.send_keys('2021')
        save_button.click()

        # Verify we're on the same page by looking for the save button
        save_button = self.browser.find_element_by_name('save_button')

        # Adjust the current start year to be valid but the end year to be before 1900
        start_year_box = self.browser.find_element_by_id('id_start_year')
        end_year_box = self.browser.find_element_by_id('id_end_year')
        self.clear_input_box(start_year_box)
        self.clear_input_box(end_year_box)
        start_year_box.send_keys('2000')
        end_year_box.send_keys('1899')
        save_button.click()

        # Verify we're on the same page
        save_button = self.browser.find_element_by_name('save_button')

        # Make end year higher than current year
        end_year_box = self.browser.find_element_by_id('id_end_year')
        self.clear_input_box(end_year_box)
        end_year_box.send_keys('2021')
        save_button.click()

        # Verify we're on the same page
        save_button = self.browser.find_element_by_name('save_button')

        # Adjust the end year so it is lower than the start year
        end_year_box = self.browser.find_element_by_id('id_end_year')
        self.clear_input_box(end_year_box)
        end_year_box.send_keys('1950')
        save_button.click()

        # Verify we're on the same page
        save_button = self.browser.find_element_by_name('save_button')
        
    def test_can_edit_existing_post(self):
        # Open blog page and navigate to CV Page
        response = self.browser.get('http://127.0.0.1:8000')
        self.browser.find_element_by_link_text('CV Page').click()

        # Add new Education
        self.browser.find_element_by_link_text('Add New Education').click()
        self.browser.find_element_by_id('id_name').send_keys('Unedited Test')
        self.browser.find_element_by_id('id_start_year').send_keys('1901')
        self.browser.find_element_by_id('id_end_year').send_keys('1902')
        self.browser.find_element_by_id('id_description').send_keys('This has not been edited')
        self.browser.find_element_by_name('save_button').click()

        # Find the new post
        e_posts = self.browser.find_elements_by_name('education')
        i = 0
        while (i < len(e_posts)):
            post = e_posts[i]
            post_title = post.find_element_by_tag_name('h3').text
            post_content = post.find_element_by_tag_name('p').text
            if (post_title == 'Unedited Test: 1901 - 1902' and post_content == 'This has not been edited'):
                break
            else:
                i += 1

        # Fail if we couldn't find the new post, otherwise find its edit button
        if (i >= len(e_posts)):
            self.fail('Did not find the new post')
        
        edit_button = e_posts[i].find_element_by_link_text('Edit')
        edit_button.click()

        # Check the form retains the information
        name_box = self.browser.find_element_by_id('id_name')
        start_year_box = self.browser.find_element_by_id('id_start_year')
        end_year_box = self.browser.find_element_by_id('id_end_year')
        description_box = self.browser.find_element_by_id('id_description')
        self.assertEqual(name_box.get_attribute('value'), 'Unedited Test')
        self.assertEqual(start_year_box.get_attribute('value'), '1901')
        self.assertEqual(end_year_box.get_attribute('value'), '1902')
        self.assertEqual(description_box.get_attribute('value'), 'This has not been edited')

        # Edit the information
        self.clear_input_box(name_box)
        self.clear_input_box(start_year_box)
        self.clear_input_box(end_year_box)
        self.clear_input_box(description_box)
        name_box.send_keys('Edited Test')
        start_year_box.send_keys('2001')
        end_year_box.send_keys('2002')
        description_box.send_keys('This has been edited')
        self.browser.find_element_by_name('save_button').click()

        e_posts = self.browser.find_elements_by_name('education')
        # Check the post has been edited
        self.assertEqual(e_posts[i].find_element_by_tag_name('h3').text, 'Edited Test: 2001 - 2002')
        self.assertEqual(e_posts[i].find_element_by_tag_name('p').text, 'This has been edited')

if __name__=='__main__':
    unittest.main(warnings='ignore')

browser.quit()