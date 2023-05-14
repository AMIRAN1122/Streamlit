import streamlit as st
import requests

@st.cache_data(show_spinner=False)
def get_page():

    # Set headers
    headers = {
        "X-Frame-Options": "ALLOWALL",
    }

    url = "https://www.google.com/url?sa=t&source=web&rct=j&url=https://bazitahrir.com/&ved=2ahUKEwj6zdrhwfX-AhXvhP0HHTr_DJAQFnoECAsQAQ&usg=AOvVaw1xjgjk7KojxNPocjPQVW1R"

    # Get the page
    response = requests.get(url, headers=headers)
    return response.content 

def main():

    st.set_page_config(page_title="My Streamlit App")

    # Get the page content
    page_content = get_page()

    # Display the page content
    st.components.v1.html(page_content, height=750, width=750)

if __name__ == "__main__":
    main()
