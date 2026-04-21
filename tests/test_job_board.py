import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

BASE_URL = "http://127.0.0.1:5000"

class TestJobBoard:

    def test_homepage_loads(self, driver):
        """Test that job board homepage loads successfully"""
        driver.get(BASE_URL)
        title = driver.find_element(By.XPATH, "//*[@data-test='page-title']")
        assert title.text == "QA Job Board"

    def test_all_jobs_displayed(self, driver):
        """Test that all 5 jobs are displayed on homepage"""
        driver.get(BASE_URL)
        jobs = driver.find_elements(By.XPATH, "//*[@data-test='job-card']")
        assert len(jobs) == 5

    def test_results_count_correct(self, driver):
        """Test that results count shows correct number"""
        driver.get(BASE_URL)
        count = driver.find_element(By.XPATH, "//*[@data-test='results-count']")
        assert "5" in count.text

    def test_search_by_keyword(self, driver):
        """Test that searching by keyword filters results correctly"""
        driver.get(BASE_URL)
        search_input = driver.find_element(By.XPATH, "//*[@data-test='search-input']")
        search_input.send_keys("QA Engineer")
        driver.find_element(By.XPATH, "//*[@data-test='search-button']").click()
        jobs = driver.find_elements(By.XPATH, "//*[@data-test='job-card']")
        assert len(jobs) >= 1

    def test_search_by_location(self, driver):
        """Test that searching by location filters results correctly"""
        driver.get(BASE_URL)
        location_input = driver.find_element(By.XPATH, "//*[@data-test='location-input']")
        location_input.send_keys("Wrocław")
        driver.find_element(By.XPATH, "//*[@data-test='search-button']").click()
        jobs = driver.find_elements(By.XPATH, "//*[@data-test='job-card']")
        assert len(jobs) == 3

    def test_job_detail_page(self, driver):
        """Test that clicking View Details opens job detail page"""
        driver.get(BASE_URL)
        driver.find_element(By.XPATH, "(//*[@data-test='apply-button'])[1]").click()
        assert "Nokia" in driver.page_source

    def test_empty_search_returns_all_jobs(self, driver):
        """Test that empty search returns all jobs"""
        driver.get(BASE_URL + "/search")
        jobs = driver.find_elements(By.XPATH, "//*[@data-test='job-card']")
        assert len(jobs) == 5

    def test_screenshot_saved(self, driver):
        """Test homepage and save screenshot as evidence"""
        driver.get(BASE_URL)
        os.makedirs("reports/screenshots", exist_ok=True)
        driver.save_screenshot("reports/screenshots/homepage.png")
        assert os.path.exists("reports/screenshots/homepage.png")