from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage:
    URL = "https://pl.indeed.com"

    SEARCH_INPUT = (By.ID, "text-input-what")
    LOCATION_INPUT = (By.ID, "text-input-where")
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit']")
    JOB_LISTINGS = (By.CLASS_NAME, "job_seen_beacon")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self):
        self.driver.get(self.URL)
        try:
            cookie_btn = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(), 'Accept') or contains(text(), 'Akceptuj')]")
            ))
            cookie_btn.click()
        except:
            pass
        return self

    def search_jobs(self, keyword, location="Wrocław"):
        search = self.wait.until(EC.presence_of_element_located(self.SEARCH_INPUT))
        search.clear()
        search.send_keys(keyword)
        loc = self.driver.find_element(*self.LOCATION_INPUT)
        loc.clear()
        loc.send_keys(location)
        self.driver.find_element(*self.SEARCH_BUTTON).click()
        return self

    def get_job_count(self):
        self.wait.until(EC.presence_of_element_located(self.JOB_LISTINGS))
        return len(self.driver.find_elements(*self.JOB_LISTINGS))

    def get_page_title(self):
        return self.driver.title