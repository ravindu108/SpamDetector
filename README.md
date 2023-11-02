# Introduction
+ This is a FastAPI application that is built on Python which will take in an email as string and classify if it is a spam email.
+ The classification of emails can be done by posting a JSON object with a 'email' attribute to the POST endpoint /classify
+ If the provided email is a spam email, the API will send a JSON response with an attribute of 'isSpam' set to True if it is spam, else it will be False

# Installation
```
pip install -r requirements.txt
python main.py
```

# Usage
+ Visit http://localhost:8000 to access the Swagger endpoint, which can be used to test the API.

# Web Interface Initiation
+ Navigate the directory which has index.html
+ Start the server on a specific port
```
python -m http.server 8080
```

+ Make sure your FastAPI server is running as well. 
