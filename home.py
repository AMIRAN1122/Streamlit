import streamlit as st
import streamlit.components.v1 as components

st.write("Hello world")

components.html(
    """
    <head>
    <script>
            !function(e,t,n){e.yektanetAnalyticsObject=n,e[n]=e[n]||function(){e[n].q.push(arguments)},e[n].q=e[n].q||[];var a=t.getElementsByTagName("head")[0],r=new Date,c="https://cdn.yektanet.com/superscript/UegHYjU6/native-streamlit.iran.liara.run-31555/yn_pub.js?v="+r.getFullYear().toString()+"0"+r.getMonth()+"0"+r.getDate()+"0"+r.getHours(),s=t.createElement("link");s.rel="preload",s.as="script",s.href=c,a.appendChild(s);var l=t.createElement("script");l.async=!0,l.src=c,a.appendChild(l)}(window,document,"yektanet");
        </script>
    <div id="pos-article-display-82887"></div>
    </head> 
    """,
    height=800
)
