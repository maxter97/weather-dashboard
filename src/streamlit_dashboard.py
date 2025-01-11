import streamlit as st
import boto3
import json
import os
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

# AWS S3 configuration
s3 = boto3.client('s3')
bucket_name = os.getenv('AWS_BUCKET_NAME')  # Replace with your actual bucket name

def fetch_weather_data_from_s3():
    objects = s3.list_objects_v2(Bucket=bucket_name, Prefix='weather-data/')
    weather_data = []
    for obj in objects.get('Contents', []):
        response = s3.get_object(Bucket=bucket_name, Key=obj['Key'])
        data = json.loads(response['Body'].read())
        weather_data.append(data)
    return weather_data


def convert_to_12_hour_format(timestamp):
    est_time = datetime.strptime(timestamp, '%Y%m%d-%H%M%S')
    return est_time.strftime('%Y-%m-%d %I:%M %p %Z')

def main():
    # Custom CSS
    st.markdown(
        """
        <style>
        .main {
            background-color: #f0f2f6;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Weather Dashboard")
    st.write("Visualize weather data from S3 bucket")

    # Streamlit widgets
    st.sidebar.header("Settings")
    selected_city = st.sidebar.selectbox("Select a city", ["All"] + [data['name'] for data in fetch_weather_data_from_s3()])
    refresh_button = st.sidebar.button("Refresh Data")

    weather_data = fetch_weather_data_from_s3()
    if weather_data:
        for data in weather_data:
            if selected_city == "All" or data['name'] == selected_city:
                est_time = convert_to_12_hour_format(data['timestamp'])
                st.subheader(f"Weather data for {data['name']} at {est_time}")
                st.write(f"Temperature: {data['main']['temp']}°F")
                st.write(f"Feels like: {data['main']['feels_like']}°F")
                st.write(f"Humidity: {data['main']['humidity']}%")
                st.write(f"Conditions: {data['weather'][0]['description']}")
    else:
        st.write("No weather data found in S3 bucket.")

if __name__ == "__main__":
    main()