from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, DevSecOps Interview!"

# PRACTICE TIP: UNCOMMENT THE LINE BELOW to test the Bandit SAST scanner in Jenkins.
# Bandit will catch this hardcoded credential and automatically fail your pipeline!
# DB_PASSWORD = "super_secret_password_123"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)