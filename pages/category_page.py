from .base_page import BasePage


class CategoryPage(BasePage):
    def should_be_category_url(self):
        """Проверяет переход на страницу категории"""
        category_url = "category"
        assert category_url in self.browser.current_url, f"Category link does not contain {category_url}"