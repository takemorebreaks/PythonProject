from collections import Counter

import pytest

from MyFramework.framework.base_test.BaseTest import BaseTest
from MyFramework.framework.json_reader.JsonReader import JsonReader
from MyFramework.framework.pages.login_page import LoginPage


class TestLogin(BaseTest):
    @pytest.mark.parametrize("user",JsonReader.read_json("data/test_data.json").values())
    def test_login(self, user):
        global last_j
        login_page = LoginPage(self.page)
        login_page.login(user["username"], user["password"])





