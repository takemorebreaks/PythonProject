from MyFramework.framework.json_reader.JsonReader import JsonReader


class LoginPage:
    def __init__(self,page):
        self.page=page
        self.locators=JsonReader.read_json("data/locators.json")["LoginPage"]
    def login(self,userName,password):
        self.page.fill(self.locators["username_field"],userName)
        self.page.fill(self.locators["password_field"],password)
        self.page.click(self.locators["login_button"])