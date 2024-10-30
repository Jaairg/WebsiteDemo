import streamlit as st
import requests


background_image_url = "https://images.unsplash.com/photo-1729636364314-877a914f223a?q=80&w=1770&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

# CSS to set the background image
page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url("{background_image_url}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    .top-right-button {{
        position: fixed;
        top: 10px;
        right: 10px;
        z-index: 9999;
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
    }}
    </style>
    """

st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>Student Center Hydroponic System</h1>", unsafe_allow_html=True)

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'username' not in st.session_state:
    st.session_state['username'] = ''

# Dummy user data
users = {"student": "password123", "admin": "password456"}

# Function to handle login
def login(username, password):
    if username in users and users[username] == password:
        st.session_state['logged_in'] = True
        st.session_state['username'] = username
        st.success("Logged in successfully!")
    else:
        st.error("Invalid username or password")

# Function to handle logout
def logout():
    st.session_state['logged_in'] = False
    st.session_state['username'] = ''
    st.success("Logged out successfully!")

# Top-right Login/Logout button
if not st.session_state['logged_in']:
    st.markdown('<button class="top-right-button" onclick="window.location.reload()">Log In</button>', unsafe_allow_html=True)
else:
    st.markdown('<button class="top-right-button" onclick="window.location.reload()">Log Out</button>', unsafe_allow_html=True)

# Display login form in sidebar if not logged in
if not st.session_state['logged_in']:
    with st.sidebar:
        st.subheader("Log In")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Log In"):
            login(username, password)
        st.info("Don't have an account? Contact admin to sign up.")


left_column, center_column, right_column, fourth_column = st.columns([3, 3, 3, 3], gap = "medium")

def get_weather_data():
    # Fetching weather data for Toms River, NJ (latitude: 39.9537, longitude: -74.1979)
    response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=39.9537&longitude=-74.1979&current_weather=true")
    if response.status_code == 200:
        data = response.json()

        if 'current_weather' in data:
            current_temp = data['current_weather']['temperature']  # Current temperature
            current_windspeed = data['current_weather']['windspeed']  # Current wind speed
            return current_temp, current_windspeed,
    else:
        st.error("Could not retrieve data from API.")
        return None, None


with left_column:
    st.subheader("Watering days")
    st.write("Monday 8:00 - 9:00")
    st.write("Wednesday 8:00 - 9:00")
    st.write("Friday 8:00 - 9:00")


with center_column:
    st.subheader("Current plant conditions")
    st.write("Humidity: 30%")
    st.write("Water level: 50%")

with right_column:
    st.subheader("Outside conditions")

    temperature, windspeed = get_weather_data()  # Unpack returned values

    if temperature is not None:
        st.metric("Temperature", f"{temperature} °C")
        st.metric("Wind Speed", f"{windspeed} km/h")

    else:
        st.error("Could not retrieve data.")
with fourth_column:
    add_button = st.button("Add plants")
    add_button = st.button('Gallery')
    add_button = st.button('Contact')
    add_button = st.button('About us')
