import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():
    # Set up the WebDriver (e.g., ChromeDriver)
    driver = webdriver.Chrome()
    yield driver
    # Teardown: Quit the WebDriver after tests
    driver.quit()

def test_home_page(driver):
    # Open the home page URL
    driver.get("https://example.com")
    # Assert that the page title is correct
    assert driver.title == "Example Domain"
