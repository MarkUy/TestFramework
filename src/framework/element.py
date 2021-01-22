from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class Element(WebElement):

    def __init__(self, driver: WebDriver, config: dict, parent, id_):
        """
        Creates a new Element class instance

        :param WebDriver driver:
        :param config:
        """
        super().__init__(parent, id_)
        self._driver = driver
        self._config = config

    def _find_element(self):
        """

        Find and return the element from the configuration

        :return: the element if it was found
        :rtype: WebElement
        """
        if self._config['by'] == 'name':
            return self._driver.find_element_by_name(self._config['query'])
        else:
            return self._driver.find_element_by_xpath(self._config['query'])

    def click(self):
        """
        Clicks the element
        """
        self._find_element().click()

    @property
    def text(self):
        """

        :return:
        """
        elem = self._find_element()
        return elem.text

    def set_text(self, text):
        elem = self._find_element()
        elem.clear()
        elem.send_keys(text)
        elem.send_keys(Keys.RETURN)
