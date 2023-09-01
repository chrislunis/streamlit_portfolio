import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(
    page_title="My Web Page",
    page_icon=":tada:",
    layout="wide"
)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    
# use local class
def local_css(file):
    with open(file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")
# Load Assets
lottie_coding = load_lottieurl("https://lottie.host/3f8f1b43-4fa9-454c-9a45-b890ba3ea52e/Fh7Ed7s0rY.json")
img_projects = Image.open("images/projects.jpg")
# Header Section
with st.container():
    st.subheader("Hi, I am Chris Lunis :wave:")
    st.title("Data Scientist From Mumbai")
    st.write("I am passionate about exploring ways to use Python and integrate it into more efficient and impactful usecase of data for the growth of business settings.")
    st.write("[Learn More about my projects here >](https://github.com/chrislunis)")

# What I do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            - Currently pursuing Master's in Artificial Intellingence from NMIMS University, Mumbai.
            - For the research and dissertation of my Master's, I'm working on the peripheral of recommendation system using AI and how it work underneath the hood.
            - I have completed # number of end to end projects and have gained exposure wile developing them about the real time challenges and also the industry-based techniques applied for deployment production usage.
                 """)
        st.write("[Open for seeking opportunities, please connect with me here ->](https://www.linkedin.com/in/chris-l-23a773136)")
    
    with right_column:
        st_lottie(lottie_coding, height=400, key="coding")


# Projects
with st.container():
    st.write('---')
    st.header('My Work Experience and Projects')
    st.write('##')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_projects)
    with text_column:
        st.subheader("Internship with KubixSquare as Android Application Developer")
        st.write(
        """
        - Worked on the development of android application for the organization using React native and it's framework.
        - During the three months of internship, our team was responsible to complete the registration and dashboard of the application.
        - Helped the organisation, in improving the engagement with clients for more growth of the organisation.
        """
        )

# Contact
with st.container():
    st.write("---")
    st.header("Get in touch with me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/chrislunis19@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()