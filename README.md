<h1>Building a Weather Data Collection system using AWS S3 and OpenWeather API</h1>
Project 1 for DevOp Challenge #DevOpsAllStarsChallenge
<h2>Overview</h2>
<p>This project grabs real-time weather data for multiple cities. It displays temperature (°F), humidity, and weather conditions. Then it automatically stores weather data in an AWS S3 bucket.</p>

![Screenshot 2025-01-07 053208](https://github.com/user-attachments/assets/2dcc45dc-5888-4f44-9e31-9e186902d5b2)
<br/>
<h2>Prerequisites</h2> 
<ul>
  <li>AWS Account: To use S3 and install <a href="https://aws.amazon.com/cli/">AWS CLI</a></li>
  <li>API Key from OpenWeather: Sign up at https://home.openweathermap.org/users/sign_up to obtain a free tier API key.</li>
  <li>Cli/Termial: To use Python and any needed dependencies</li>
  <li>A Code/Text Editor: To edit any code if needed</li>
</ul>

<br/>
<h2>Instructions</h2>
<ol>
  <li>Clone Repository using the command <b>git clone</b> https://github.com/maxter97/weather-dashboard.git</li>
  <li>Move to weather-dashboard directory using <b>Cd</b> and run the command <b>pip install -r requirements.txt</b> to install all dependencies needed for this project.
  <p>* If the command does not work try to using the <a href="https://docs.python.org/3/library/venv.html">venv</a> command or use the <a href="https://pipx.pypa.io/stable/">pipx<a/> command to creating a virtual environments to install your dependencies. </p>
      
![Screenshot 2025-01-07 080710](https://github.com/user-attachments/assets/9a512778-d359-4f18-bf55-b5dc8ddba4f1)
  <li>Use command <b>aws Configue</b> and add your credentials needed to access AWS resources
  <p>* For best practice, create an IAM user with short-term credentials using IAM Identity Center and use command <b>aws configure sso</b>. (If yoh have done this way make sure to still add credentials to ~/.aws/credentials or use export command to add them). </p></li>
  <li>Put API key in a .env file <p>(Code has been updated to name the bucket weather-dashboard-{random_number} so no need to add bucket name unless you want your bucket a specific name)</p></li>
    
  ![Screenshot 2025-01-06 133302](https://github.com/user-attachments/assets/63ae31e7-bb49-4bac-adf9-5f7f3c97d26b)
  <li>Run weather_dashboard.py script using python </li>
   
  ![Screenshot 2025-01-07 073716](https://github.com/user-attachments/assets/7c2dc2d5-3d34-4c79-b451-1ecf885f8e5a)
  <li>Now Your data should be in your newly created S3 Bucket</li>

</ol>

![Screenshot 2025-01-06 152752](https://github.com/user-attachments/assets/8a017f43-4e4f-4ae2-99f6-24cef9308fb3)
![Screenshot 2025-01-06 152802](https://github.com/user-attachments/assets/f7b727bf-0a41-448b-9310-368d6268314e)
![Screenshot 2025-01-06 152814](https://github.com/user-attachments/assets/0621dffc-dc42-4d73-b13d-2399beb5e6d7)

<h2>Future Enhancements</h2>
<ul>
  <li>Input different cites</li>
  <li>Set up CI/CD pipeline</li>
  <li>Automate and run in a virtul environment</li>
  
</ul>
