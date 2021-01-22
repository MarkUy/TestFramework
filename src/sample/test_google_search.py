import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from framework.page import Page


class MyTestCase(unittest.TestCase):
    def test_something(self):
        driver = webdriver.Chrome()
        driver.get("http://www.python.org")
        assert "Python" in driver.title
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        driver.close()

    def test_something_else(self):
        page = Page("page.json")
        page.open()
        assert "Python" in page.driver.title
        elem = page.element('search')
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in page.driver.page_source
        page.close()


if __name__ == '__main__':
    unittest.main()
