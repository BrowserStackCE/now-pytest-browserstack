import pytest
import os

def openTestPage(selenium):

    # 1. Navigate to the website
    web_endpoint = os.environ.get("CX_TEST_URL", "https://bstackdemo.com/")
    
    selenium.get(web_endpoint)

    # 2. Use universal functions to get page data (no locators)
    page_title = selenium.title
    current_url = selenium.current_url
    page_source = selenium.page_source

    # 3. Log the captured data to BrowserStack using 'annotate'
    # This will appear in the "Text Logs" section of your Automate session
    log_data = f"Page Title: {page_title} | Current URL: {current_url}"
    selenium.execute_script(
        'browserstack_executor: {"action": "annotate", "arguments": {"data": "' + log_data + '", "level": "info"}}'
    )

    # 4. Perform simple, locator-free assertions
    assert len(page_source) > 100  # Checks that the page has content
