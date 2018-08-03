from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=5, poll=1):
        feature_by = feature[0]
        feature_value = feature[1]

        web_driver_wait = WebDriverWait(self.driver, timeout, poll)
        return web_driver_wait.until(lambda x: x.find_element(feature_by, feature_value))

    def find_elements(self, feature, timeout=5, poll=1):
        feature_by = feature[0]
        feature_value = feature[1]

        web_driver_wait = WebDriverWait(self.driver, timeout, poll)
        return web_driver_wait.until(lambda x: x.find_elements(feature_by, feature_value))

    def click(self, feature):
        self.find_element(feature).click()

    def input(self, feature, text):
        self.find_element(feature).send_keys(text)

    def scroll_page_one_time(self, dir="down"):
        """
        滑动一次一半屏幕的距离
        :return:
        """

        screen_width = self.driver.get_window_size()["width"]
        screen_height = self.driver.get_window_size()["height"]

        left = {"x": screen_width * 0.25, "y": screen_height * 0.5}
        right = {"x": screen_width * 0.75, "y": screen_height * 0.5}
        up = {"x": screen_width * 0.5, "y": screen_height * 0.25}
        down = {"x": screen_width * 0.5, "y": screen_height * 0.75}

        if dir == "down":
            self.driver.swipe(down["x"], down["y"], up["x"], up["y"], 2000)
        elif dir == "up":
            self.driver.swipe(up["x"], up["y"], down["x"], down["y"], 2000)
        elif dir == "right":
            self.driver.swipe(right["x"], right["y"], left["x"], left["y"], 2000)
        elif dir == "left":
            self.driver.swipe(left["x"], left["y"], right["x"], right["y"], 2000)
        else:
            raise Exception("请传入正确的参数 left/right/up/down")
