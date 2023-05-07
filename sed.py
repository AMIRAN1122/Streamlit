import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from PIL import Image
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

html_string = """
<script>
            !function(e,t,n){e.yektanetAnalyticsObject=n,e[n]=e[n]||function(){e[n].q.push(arguments)},e[n].q=e[n].q||[];var a=t.getElementsByTagName("head")[0],r=new Date,c="https://cdn.yektanet.com/superscript/QOqTe3Bm/native-amiran1122-red-red-lkrpex.streamlit.app-31446/yn_pub.js?v="+r.getFullYear().toString()+"0"+r.getMonth()+"0"+r.getDate()+"0"+r.getHours(),s=t.createElement("link");s.rel="preload",s.as="script",s.href=c,a.appendChild(s);var l=t.createElement("script");l.async=!0,l.src=c,a.appendChild(l)}(window,document,"yektanet");
        </script>

<div id="pos-article-display-82621"></div>     
"""

if st.button(label="Start"):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.set_capability('browserless:token', 'SDflkgfhlslktydskhga')

    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")

    driver = webdriver.Remote(
        command_executor='https://s-chrome.iran.liara.run/webdriver',
        options=chrome_options
    )

    driver.get("https://streamlit.iran.liara.run/")
    
    page_source = driver.page_source
    
    st.write("1 2 3 OK")
    
    driver.quit()
    
    st.write(page_source)

    
#     try:
#         with Image.open(image_path) as image:
#             st.image(image, caption='This is for you')

#     except OSError:
#         st.write("مشکل خواندن فایل تصویر")
