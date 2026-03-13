import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.mark.django_db
def test_abrir_sistema(live_server):

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    driver.get(live_server.url)

    assert "EPI" in driver.page_source

    driver.quit()