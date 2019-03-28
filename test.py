import allure


class TestDome:
    @allure.step(title="这是001")
    def test_01(self):
        allure.attach("步骤描述", "具体的描述内容", allure.attach_type.TEXT)
        print("这是一个--------01")
        assert True

    @allure.step(title="这是002")
    def test_02(self):
        with open("./page.png", "rb") as f:
            allure.attach("图名", f.read(), allure.attach_type.PNG)
        print("---------------02")
        assert True
