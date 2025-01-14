# Building a Weather Data Collection system and Dashboard
Project 1 for DevOp Challenge #DevOpsAllStarsChallenge
# Overview
This project grabs real-time weather data for multiple citiesv using a weather API. It collects temperature (°F), humidity, and weather conditions. Stores it automatically stores weather data in an AWS S3 bucket. Then is Virtualized into a dashboard with streamlit.

![Screenshot 2025-01-11 100615](https://github.com/user-attachments/assets/042627cf-1900-4968-bd0d-cff2c46f9ce0)

# Prerequisites
1. Familiar with AWS and Python
2. AWS Account: To use S3 and install <a href="https://aws.amazon.com/cli/">AWS CLI</a> 
3. API Key from OpenWeather: Sign up at https://home.openweathermap.org/users/sign_up to obtain a free tier API key.
4. A Code/Text Editor: To edit any code if needed
5. IDE (ex. VS Code)
   
# Instructions

## 1. Clone Repository using the command  
    
```bash
git clone  https://github.com/maxter97/weather-dashboard.git
```
## 2. Move to where the weather-dashboard directory is stored. Then install all dependencies needed for this project using

```bash
pip install -r requirements.txt
```
 
* If the command does not work try to using the <a href="https://docs.python.org/3/library/venv.html">venv</a> command or use the <a href="https://pipx.pypa.io/stable/">pipx<a/> command to creating a virtual environments to install your dependencies. 
      
![Screenshot 2025-01-07 080710](https://github.com/user-attachments/assets/9a512778-d359-4f18-bf55-b5dc8ddba4f1)

## 3. Add your credentials needed to access AWS resources using
```bash
aws Configue
```
* For best practice, create an IAM user with short-term credentials using IAM Identity Center. If done this way make sure to still add credentials to ~/.aws/credentials or use export command to add them. Use this command if done this way.
```bash
aws configure sso
``` 
  
## 4. Create a a .env file and put your OpenWeather API key and bucket name into it (If you do not have a bucket name entered the code will create a new s3 bucket named weather-dashboard- with a random 4 digit number at the end)
    
  ![Screenshot 2025-01-06 133302](https://github.com/user-attachments/assets/63ae31e7-bb49-4bac-adf9-5f7f3c97d26b)
  
## 5. Run (Python command vary depending on version and OS)
   Update: You can now enter the cites you want to collect data on.
```bash
python3 weather_dashboard.py script 
```  

![Screenshot 2025-01-08 221937](https://github.com/user-attachments/assets/0f133c35-0e65-49d0-83d0-01da6a9e24fd)

## 6. Now Your data should be in your newly created S3 Bucket
   
![Screenshot 2025-01-08 222658](https://github.com/user-attachments/assets/62ec7274-279b-4371-845c-2e92a14d30db)
![Screenshot 2025-01-08 222708](https://github.com/user-attachments/assets/c0385480-e5ca-4280-91da-9a98787f6d3c)
![Screenshot 2025-01-08 222715](https://github.com/user-attachments/assets/045f37a7-6386-439e-a306-082bc559dc2c)

# Creating Dashboard
We can create a dashboard that will visualize our data insde the S3 bucket.

## 1. Install the following dependencies
   ```bash
   pip install streamlit
   pip install pytz
   pip install matplotlib
   pip install pylance
   pip install seaborn
   ```
   * They have been added to the requirements.txt file
     
## 2. Create a new Python script to create dashboard and pull data from S3 
   ```bash
   touch streamlit_dashboard.py
   ```
    *The script I used is included in the repository
## 3. Copy this code into the newly created file. Edit to personalize to your preference
```bash
    import streamlit as st
    import boto3
    import json
    
    # AWS S3 configuration
    s3 = boto3.client('s3')
    bucket_name = 'your-bucket-name'  # Replace with your actual bucket name
    
    def fetch_weather_data_from_s3():
        objects = s3.list_objects_v2(Bucket=bucket_name, Prefix='weather-data/')
        weather_data = []
        for obj in objects.get('Contents', []):
            response = s3.get_object(Bucket=bucket_name, Key=obj['Key'])
            data = json.loads(response['Body'].read())
            weather_data.append(data)
        return weather_data
    
    def main():
        st.title("Weather Dashboard")
        st.write("Visualize weather data from S3 bucket")
    
        weather_data = fetch_weather_data_from_s3()
        if weather_data:
            for data in weather_data:
                st.subheader(f"Weather data for {data['name']} at {data['timestamp']}")
                st.write(f"Temperature: {data['main']['temp']}°F")
                st.write(f"Feels like: {data['main']['feels_like']}°F")
                st.write(f"Humidity: {data['main']['humidity']}%")
                st.write(f"Conditions: {data['weather'][0]['description']}")
        else:
            st.write("No weather data found in S3 bucket.")
    
    if __name__ == "__main__":
        main()
```
## 4. Run this command to launch your dashboard
```bash
   streamlit run streamlit_dashboard.py
```
    Once you run it you will get a local URL and a network URL to access your dashboard
   
    ![Screenshot 2025-01-11 081023](https://github.com/user-attachments/assets/31c4ffe0-07ce-4cf5-a6dd-d7a1ba2d3a1e)

## 5. Here is how my dashboard looks with some edits to streamlit_dashboard.py
   
![Screenshot 2025-01-11 080944](https://github.com/user-attachments/assets/37af07ce-bf8c-436f-ba72-73d0c5aa47ab)

# What I have learned 
- Using Python script to featch and transform data
- How to secure key values when running scripts and using AWS
- Using AWS services, IAM user and roles
- Create a user interface and make changes to it with streamlit
- Getting familiar with the AWS CLI


# Future Enhancements
1. Automate and run in a virtul environment
2. Host the dashborad online
3. Input cities in dashboard
  

