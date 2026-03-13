from selenium import webdriver
import time

def test_abrir_sistema():

    driver = webdriver.Chrome()

    try:
        driver.get("http://127.0.0.1:8000/")
        time.sleep(3)

        assert "EPI" in driver.page_source

    finally:
        driver.quit()