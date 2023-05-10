# import streamlit as st

# st.set_page_config(
#     page_title="Hello",
#     page_icon="👋",
# )

# st.write("# Welcome to Streamlit! 👋")

# st.sidebar.success("Select a demo above.")

# st.markdown(
#     """
#     Streamlit is an open-source app framework built specifically for
#     Machine Learning and Data Science projects.
#     **👈 Select a demo from the sidebar** to see some examples
#     of what Streamlit can do!
#     ### Want to learn more?
#     - Check out [streamlit.io](https://streamlit.io)
#     - Jump into our [documentation](https://docs.streamlit.io)
#     - Ask a question in our [community
#         forums](https://discuss.streamlit.io)
#     ### See more complex demos
#     - Use a neural net to [analyze the Udacity Self-driving Car Image
#         Dataset](https://github.com/streamlit/demo-self-driving)
#     - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
# """
# )


import streamlit as st
import streamlit.components.v1 as components
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import time

st.write("Hello world")

# components.html(
#     """
#     <head>
#     <script>
#             !function(e,t,n){e.yektanetAnalyticsObject=n,e[n]=e[n]||function(){e[n].q.push(arguments)},e[n].q=e[n].q||[];var a=t.getElementsByTagName("head")[0],r=new Date,c="https://cdn.yektanet.com/superscript/UegHYjU6/native-streamlit.iran.liara.run-31555/yn_pub.js?v="+r.getFullYear().toString()+"0"+r.getMonth()+"0"+r.getDate()+"0"+r.getHours(),s=t.createElement("link");s.rel="preload",s.as="script",s.href=c,a.appendChild(s);var l=t.createElement("script");l.async=!0,l.src=c,a.appendChild(l)}(window,document,"yektanet");
#         </script>
#     <div id="pos-article-display-82887"></div>
#     </head> 
#     """,
#     height=625,
#     width=1000,
# )


# if st.button(label="Start"):

#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.set_capability('browserless:token', 'SDflkgfhlslktydskhga')

#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36")

#     driver = webdriver.Remote(
#         command_executor='https://s-chrome.iran.liara.run/webdriver',
#         options=chrome_options
#     )

#     driver.get("https://streamlit.iran.liara.run/")
    
#     WaitFrameElement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div[1]/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/iframe")))

#     FindFrameElement = driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/iframe")

#     driver.switch_to.frame(FindFrameElement)
    
#     st.write(driver.page_source)

#     WaitLinkElement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.yn-item-link")))
    
#     LinkElements = driver.find_elements(By.CSS_SELECTOR, "a.yn-item-link")
                                                    
#     linc = []

#     for link in LinkElements:
#         link = link.get_attribute('href')
#         linc.append(link)

#     st.write(linc[6])

#     driver.quit()

    
#     try:
#         with Image.open(image_path) as image:
#             st.image(image, caption='This is for you')

#     except OSError:
#         st.write("مشکل خواندن فایل تصویر")


