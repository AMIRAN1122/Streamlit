import streamlit as st
import streamlit.components.v1 as components
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import WebDriverException
import random
import time

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")

if st.button(label="Start"):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.set_capability('browserless:token', 'SDflkgfhlslktydskhga')

    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36")

    driver = webdriver.Remote(
        command_executor='https://s-chrome.iran.liara.run/webdriver',
        options=chrome_options
    )

    driver.get("https://streamlit.iran.liara.run/")
    
    try:
        WaitFrameElement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div[1]/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/iframe")))
        
        FindFrameElement = driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/div/div/div/section/div[1]/div[1]/div/div[2]/iframe")

        driver.switch_to.frame(FindFrameElement)

        st.write(driver.page_source)
        
    except NoSuchElementException:
        driver.quit()
        
    except TimeoutException:
        driver.quit()
        
    except ElementNotInteractableException:
        driver.quit()
       
    except WebDriverException:
        driver.quit()
        
    try:
        WaitLinkElement = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.yn-item-link")))

        LinkElements = driver.find_elements(By.CSS_SELECTOR, "a.yn-item-link")
        
    except NoSuchElementException:
        driver.quit()
        
    except TimeoutException:
        driver.quit()
        
    except ElementNotInteractableException:
        driver.quit()
       
    except WebDriverException:
        driver.quit()
        
    AdLinc = []

    for link in LinkElements:
        link = link.get_attribute('href')
        AdLinc.append(link)

    AdIndexList = [6, 7, 8, 9, 10, 11]
    
    AdIndex = random.choice(AdIndexList)
    
    st.write(AdIndex)
    
    st.write(AdLinc[AdIndex])

    driver.quit()