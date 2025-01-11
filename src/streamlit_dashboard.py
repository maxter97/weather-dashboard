import streamlit as st
import boto3
import json
import os
from dotenv import load_dotenv
from datetime import datetime
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
    est_time = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
    return est_time.strftime('%Y-%m-%d %I:%M %p')

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
    weather_data = fetch_weather_data_from_s3()
    cities = ["All"] + [data['city']['name'] for data in weather_data]
    selected_city = st.sidebar.selectbox("Select a city", cities)
    refresh_button = st.sidebar.button("Refresh Data")

    if weather_data:
        for data in weather_data:
            if selected_city == "All" or data['city']['name'] == selected_city:
                st.subheader(f"5-Day/3-Hour Forecast for {data['city']['name']}")
                forecast_data = data['list']
                df = pd.DataFrame({
                    'Date': [forecast['dt_txt'].split(' ')[0] for forecast in forecast_data],
                    'Time': [convert_to_12_hour_format(forecast['dt_txt']) for forecast in forecast_data],
                    'Temperature (°F)': [forecast['main']['temp'] for forecast in forecast_data],
                    'Feels Like (°F)': [forecast['main']['feels_like'] for forecast in forecast_data],
                    'Humidity (%)': [forecast['main']['humidity'] for forecast in forecast_data],
                    'Conditions': [forecast['weather'][0]['description'] for forecast in forecast_data]
                })

                grouped = df.groupby('Date')

                for date, group in grouped:
                    st.write(f"### {date}")
                    heatmap_data = group.pivot(index='Time', columns='Conditions', values='Temperature (°F)')
                    plt.figure(figsize=(10, 6))
                    sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap="coolwarm")
                    st.pyplot(plt)
                    st.write("Detailed Forecast")
                    st.dataframe(group[['Time', 'Temperature (°F)', 'Feels Like (°F)', 'Humidity (%)', 'Conditions']])
    else:
        st.write("No weather data found in S3 bucket.")

if __name__ == "__main__":
    main()