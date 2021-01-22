import json

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class Page(object):

    def __init__(self, config_path: str):
        """
        Create a new Page class instance

        :param str config_path: path to the configuration
        """
        with open(config_path) as f:
            self._config = json.load(f)
        self._path = config_path
        self._url = self._config['url']
        self.driver = self._find_driver(self._config['driver'])

    def _find_driver(self, driver: str):
        """
        WebDriver factory.

        :param str driver: Name of the Selenium WebDriver
        :return: Selenium WebDriver
        :rtype: WebDriver
        """
        if isinstance(driver, str):
            d = driver.lower()
            if d == 'chrome':
                return webdriver.Chrome()
            elif d == 'firefox':
                return webdriver.Firefox()
            elif d == 'edge':
                return webdriver.Edge()
            else:
                raise NotImplemented('Unknown Web Driver %s' % driver)
        else:
            raise NotImplemented('Unknown Web Driver %s' % driver)

    def element(self, key: str) -> WebElement:
        """
        WebElement factory.

        :param str key: element key from config
        :return: the element if it was found
        :rtype: WebElement
        """
        if key not in self._config['elements']:
            raise KeyError('Unknown element %s' % key)
        # return Element(self._driver, self._config['elements'][key])
        config = self._config['elements'][key]
        if config['by'] == 'name':
            return self.driver.find_element_by_name(config['query'])
        else:
            return self.driver.find_element_by_xpath(config['query'])

    def open(self):
        """
        Loads the web page of the url in the current browser session.
        """
        self.driver.get(self._url)

    def close(self):
        """
        Closes the current window.
        """
        self.driver.close()
