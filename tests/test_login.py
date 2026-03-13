from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_abrir_sistema():

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    driver.get("http://127.0.0.1:8000/")

    assert "EPI" in driver.page_source

    driver.quit()