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

    chrome_options = webdriver.ChromeOptions()
    chrome_options.set_capability('browserless:token', 'CkMUJMQQwq3ZbAGi33rssdfhkdfs')

    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")

    driver = webdriver.Remote(
        command_executor='https://cc-chrome.iran.liara.run/webdriver',
        options=chrome_options
    )

    driver.get("https://www.google.com/")
    
    time.sleep(10)
    
    driver.save_screenshot("image.png")
    
    image = Image.open("image.png")
    
    st.image(image, caption='This is for you')
