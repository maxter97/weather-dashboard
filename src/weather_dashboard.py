import os
import json
import boto3
import botocore.exceptions 
import requests
from datetime import datetime
from dotenv import load_dotenv
import random

# Load environment variables
load_dotenv()

class WeatherDashboard:
    def __init__(self):
        self.api_key = os.getenv('OPENWEATHER_API_KEY')
        self.bucket_name = os.getenv('AWS_BUCKET_NAME')
        profile_name = os.getenv('AWS_PROFILE', 'default')
        
        try:
            self.session = boto3.Session(profile_name=profile_name)
            print(f"Using AWS profile: {profile_name}")
        except botocore.exceptions.ProfileNotFound as e:
            print(f"Profile not found: {e}")
            raise
        
        self.s3_client = boto3.client('s3')  # Initialize s3_client

    def create_bucket_if_not_exists(self):
        """Create S3 bucket if it doesn't exist"""
        if self.bucket_name:
            try:
                self.s3_client.head_bucket(Bucket=self.bucket_name)
                print(f"Bucket {self.bucket_name} exists")
                return
            except botocore.exceptions.ClientError as e:
                error_code = int(e.response['Error']['Code'])
                if error_code == 404:
                    print(f"Bucket {self.bucket_name} does not exist in AWS")
                    try:
                        self.s3_client.create_bucket(Bucket=self.bucket_name)
                        print(f"Successfully created bucket {self.bucket_name}")
                        self.update_env_file(self.bucket_name)
                        return
                    except Exception as e:
                        print(f"Error creating bucket: {e}")
                        return
                else:
                    print(f"Error checking bucket: {e}")
                    return
        else:
            print("Bucket name not found in .env file")

        try:
            # Generate a unique bucket name
            random_number = random.randint(1000, 9999)
            self.bucket_name = f"weather-dashboard-{random_number}"
            self.s3_client.create_bucket(Bucket=self.bucket_name)
            print(f"Successfully created bucket {self.bucket_name}")
            self.update_env_file(self.bucket_name)
        except Exception as e:
            print(f"Error creating bucket: {e}")

    def update_env_file(self, bucket_name):
        """Update the .env file with the new bucket name"""
        if not os.path.exists('.env'):
            with open('.env', 'w') as file:
                file.write(f'AWS_BUCKET_NAME={bucket_name}\n')
        else:
            with open('.env', 'r') as file:
                lines = file.readlines()
            
            with open('.env', 'w') as file:
                for line in lines:
                    if line.startswith('AWS_BUCKET_NAME='):
                        file.write(f'AWS_BUCKET_NAME={bucket_name}\n')
                    else:
                        file.write(line)

    def fetch_weather(self, city):
        """Fetch 5-day/3-hour forecast data from OpenWeather API"""
        base_url = "http://api.openweathermap.org/data/2.5/forecast"
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "imperial"
        }
        
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None

    def save_to_s3(self, weather_data, city):
        """Save weather data to S3 bucket"""
        if not weather_data:
            return False
            
        timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
        file_name = f"weather-data/{city}-{timestamp}.json"
        
        try:
            weather_data['timestamp'] = timestamp
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=file_name,
                Body=json.dumps(weather_data),
                ContentType='application/json'
            )
            print(f"Successfully saved data for {city} to S3")
            return True
        except Exception as e:
            print(f"Error saving to S3: {e}")
            return False

def main():
    dashboard = WeatherDashboard()
    
    # Create bucket if needed
    dashboard.create_bucket_if_not_exists()
    
    # Prompt user for cities
    cities_input = input("Enter the cities you want to fetch weather data for, separated by commas: ")
    cities = [city.strip() for city in cities_input.split(",")]
    
    for city in cities:
        print(f"\nFetching weather for {city}...")
        weather_data = dashboard.fetch_weather(city)
        if weather_data:
            success = dashboard.save_to_s3(weather_data, city)
            if success:
                print(f"Weather data for {city} saved to S3!")
        else:
            print(f"Failed to fetch weather data for {city}")

if __name__ == "__main__":
    main()