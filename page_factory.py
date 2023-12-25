from abc import ABC

class Component(ABC):
    def __init__(self, locator):
        self.locator = locator

    def fill_input(self, **kwargs):
        self.locator.click()
        self.locator.send_keys(**kwargs)
