from playwright.sync_api import Page
import allure

class TestCases:
    def __init__(self, page: Page):
        self.page = page

    @allure.step
    def check_test_exists(self, test_name: str):
        return self.page.query_selector(f'css=tr >> text="{test_name}"') is not None

    @allure.step
    def delete_test_by_name(self, test_name: str):
        # self.page.locator(f'*css=tr >> text=\"{test_name}\"')
        self.page.get_by_role("row").filter(has_text=test_name).get_by_role('button', name="Delete").last.click()
        self.page.wait_for_timeout(300)

    @allure.step
    # table columns are hidden in the mobile device. Return True if all are hidden
    def check_columns_hidden(self):
        description = self.page.is_hidden('.thDes')
        author = self.page.is_hidden('.thAuthor')
        executor = self.page.is_hidden('.thLast')
        return description and author and executor
