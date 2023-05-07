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
    chrome_options.set_capability('browserless:token', 'SDflkgfhlslktydskhga')

    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")

    driver = webdriver.Remote(
        command_executor='https://s-chrome.iran.liara.run/webdriver',
        options=chrome_options
    )

    driver.get("https://music-fa.com/download-song/69770/")
    
    page_source = driver.page_source
    
    st.write(page_source)

    
#     try:
#         with Image.open(image_path) as image:
#             st.image(image, caption='This is for you')

#     except OSError:
#         st.write("مشکل خواندن فایل تصویر")
