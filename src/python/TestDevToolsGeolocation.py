from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pytest

class TestDevToolsGeolocation:
    def setup_method(self, method):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()

    def teardown_method(self, method):
        self.driver.quit()

    # use https://my-location.org/