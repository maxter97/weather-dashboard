# Building a Weather Data Collection system using AWS S3 and OpenWeather API
Project 1 for DevOp Challenge #DevOpsAllStarsChallenge
# Overview
This project grabs real-time weather data for multiple cities. It displays temperature (°F), humidity, and weather conditions. Then it automatically stores weather data in an AWS S3 bucket.

![Screenshot 2025-01-07 053208](https://github.com/user-attachments/assets/2dcc45dc-5888-4f44-9e31-9e186902d5b2)

# Prerequisites
1. Familiar with AWS and Python
2. AWS Account: To use S3 and install <a href="https://aws.amazon.com/cli/">AWS CLI</a> 
3. API Key from OpenWeather: Sign up at https://home.openweathermap.org/users/sign_up to obtain a free tier API key.
4. A Code/Text Editor: To edit any code if needed
5. IDE (ex. VS Code)
# Instructions

1. Clone Repository using the command  
    
```bash
git clone  https://github.com/maxter97/weather-dashboard.git
```
2. Move to where the weather-dashboard directory is stored. Then install all dependencies needed for this project using

```bash
pip install -r requirements.txt
```
 
* If the command does not work try to using the <a href="https://docs.python.org/3/library/venv.html">venv</a> command or use the <a href="https://pipx.pypa.io/stable/">pipx<a/> command to creating a virtual environments to install your dependencies. 
      
![Screenshot 2025-01-07 080710](https://github.com/user-attachments/assets/9a512778-d359-4f18-bf55-b5dc8ddba4f1)

3. Add your credentials needed to access AWS resources using
```bash
aws Configue
```
* For best practice, create an IAM user with short-term credentials using IAM Identity Center. If done this way make sure to still add credentials to ~/.aws/credentials or use export command to add them. Use this command if done this way.
```bash
aws configure sso
``` 
  
4. Create a a .env file and put your OpenWeather API key and bucket name into it (If you do not have a bucket name entered the code will create a new s3 bucket named weather-dashboard- with a random 4 digit number at the end)
    
  ![Screenshot 2025-01-06 133302](https://github.com/user-attachments/assets/63ae31e7-bb49-4bac-adf9-5f7f3c97d26b)
  
5. Run (Python command vary depending on version and OS)
   Update: You can now enter the cites you want to collect data on.
```bash
python3 weather_dashboard.py script 
```  

![Screenshot 2025-01-08 221937](https://github.com/user-attachments/assets/0f133c35-0e65-49d0-83d0-01da6a9e24fd)

6. Now Your data should be in your newly created S3 Bucket
   
![Screenshot 2025-01-08 222658](https://github.com/user-attachments/assets/62ec7274-279b-4371-845c-2e92a14d30db)
![Screenshot 2025-01-08 222708](https://github.com/user-attachments/assets/c0385480-e5ca-4280-91da-9a98787f6d3c)
![Screenshot 2025-01-08 222715](https://github.com/user-attachments/assets/045f37a7-6386-439e-a306-082bc559dc2c)


# Future Enhancements
1. Input different cite
2. Be able to create a weather dashboard with data
3. Automate and run in a virtul environment
  

