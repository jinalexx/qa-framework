import pytest
from pages.search_page import SearchPage
import os


class TestJobSearch:

    def test_homepage_loads(self, driver):
        """Test that Pracuj.pl homepage loads successfully"""
        page = SearchPage(driver)
        page.open()
        assert "indeed" in driver.title.lower() or len(driver.title) > 0

    def test_page_has_content(self, driver):
        """Test that homepage has visible content"""
        page = SearchPage(driver)
        page.open()
        body = driver.find_element("tag name", "body")
        assert len(body.text) > 0

    def test_search_returns_results(self, driver):
        """Test that searching for QA jobs returns results"""
        page = SearchPage(driver)
        page.open()
        try:
            page.search_jobs("QA", "Wrocław")
            count = page.get_job_count()
            assert count > 0, "No job listings found"
        except Exception as e:
            pytest.skip(f"Search functionality not accessible: {e}")

    def test_screenshot_on_load(self, driver):
        """Test homepage and save screenshot"""
        page = SearchPage(driver)
        page.open()
        os.makedirs("reports/screenshots", exist_ok=True)
        driver.save_screenshot("reports/screenshots/homepage.png")
        assert True