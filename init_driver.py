from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class InitDriver(object):

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, xpath, timer=100):
        """ Функция ожидания элемента на странице.
            Если элемент найден функция возвращает его.
            Если нет, то возвращается False
        :param xpath: Обязательный параметр, элемент в формате xpath,
                        который ищется на странице
        :param timer: Время, по истечении которого, в случае, если элемент не найден,
                        функция переходит в Except
        """
        self.wait_for_progress_gif_and_ajax()
        try:
            element = WebDriverWait(self.driver, timer). \
                until(ec.element_to_be_clickable((By.XPATH, xpath)))
            return element
        except StaleElementReferenceException:
            print("except StaleElementReferenceException:")
            self.driver.quit()
            return False
            # time.sleep(3)
            # el = WebDriverWait(self.driver, timer).\
            #     until(ec.element_to_be_clickable((By.XPATH, xpath)))
            # return el

    def wait_for_progress_gif_and_ajax(self, timer_for_progress_gif=120, timer_for_ajax=60):
        """ Функция ожидания, пока progress gif и ajax исчезнут со страницы.
            В кейсах, где progress gif и/или ajax
            могут загружаться дольше установленного по умолчанию времени,
            можно передавать время ожидания явно при вызове функции."""
        progress_gif = "//div[@class='progress-gif']"
        ajax = "'div.async-load-placeholder',display='block'"
        # ajax = "//div[@class='async-load-placeholder']"
        try:
            WebDriverWait(self.driver, timer_for_progress_gif).\
                until_not(ec.presence_of_element_located((By.XPATH, progress_gif)))

            WebDriverWait(self.driver, timer_for_ajax).\
                until_not(ec.presence_of_element_located((By.CSS_SELECTOR, ajax)))
            # print("LOADER & AJAX")
            return
        except StaleElementReferenceException:
            print("LOADER EXCEPT")
            return False

    def element_is_not_present(self, xpath, timer=30):
        WebDriverWait(self.driver, timer).until_not(ec.presence_of_element_located((By.XPATH, xpath)))
