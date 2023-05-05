import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from PIL import Image
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

if st.button(label="Start"):

#     service = Service(ChromeDriverManager().install())

#     options = webdriver.ChromeOptions()

#     options.add_argument("--headless")

#     options.add_argument("--disable-gpu")

#     # options.add_argument("--no-sandbox")

#     # options.add_argument("--disable-dev-shm-usage")

#     options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36")

#     driver = webdriver.Chrome(service=service, options=options)

#     driver.get("https://snapinsta.app/")
    
#     time.sleep(10)
    
#     driver.save_screenshot("image.png")
    
#     image = Image.open("image.png")
    
#     st.image(image, caption='This is for you')  
    
    chrome_capabilities = webdriver.DesiredCapabilities.CHROME.copy()
    chrome_capabilities['browserless:token'] = 'WR2t4sKXbSX0h'
    chrome_capabilities['goog:chromeOptions'] = {
        'args': [
            '--headless',
            '--no-sandbox'
        ]
    }

    driver = webdriver.Remote(
        command_executor='https://chrome-pyjbqmuda.iran.liara.run/webdriver',
        desired_capabilities=chrome_capabilities,
        browser_profile=None,
        proxy=None,
        keep_alive=False,
        file_detector=None
    )


    driver.get("https://www.digikala.com/")
    
    time.sleep(10)
    
    driver.save_screenshot("image.png")
    
    image = Image.open("image.png")
    
    st.image(image, caption='This is for you')
