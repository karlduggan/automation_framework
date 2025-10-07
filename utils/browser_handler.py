from playwright.sync_api import sync_playwright
from configuration.config import get_parameters, load_parameters

class BrowserHandler:
    def __init__(self):
        load_parameters()
        params = get_parameters()
        self.playwright = sync_playwright().start()
        self.browser = getattr(self.playwright, params["browser"]).launch(headless=params["headless"])
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def goto(self, url):
        self.page.goto(url)

    def get_title(self):
        return self.page.title()

    def screenshot(self, path="screenshot.png"):
        self.page.screenshot(path=path)
        
    def get_page_content(self):
        return self.page.content()
    
    def close_browser(self):
        self.context.close()
        self.browser.close()
        self.playwright.stop()

# Example usage:
handler = BrowserHandler()
handler.goto(url=get_parameters()["url"])
print(handler.get_title())
handler.screenshot("example.png")
handler.close_browser()