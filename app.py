from flask import Flask
import socket
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return f"""
    <html>
    <head>
        <title>Terraform Deployed App</title>
        <style>
            body {{
                background-color: #0d1117;
                color: #58a6ff;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                text-align: center;
                padding-top: 60px;
            }}
            h1 {{
                font-size: 3em;
                margin-bottom: 20px;
                color: #c9d1d9;
            }}
            p {{
                font-size: 1.2em;
                margin: 10px 0;
            }}
            .highlight {{
                color: #ffffff;
                font-weight: bold;
            }}
            .badge {{
                margin-top: 30px;
            }}
        </style>
    </head>
    <body>
        <h1>🚀 Flask App Deployed via <span class="highlight">Terraform</span></h1>
        <p>🖥️ EC2 Hostname: <span class="highlight">{hostname}</span></p>
        <p>🌐 Public IP: <span class="highlight">{ip}</span></p>
        <p>📅 Deployment Time: <span class="highlight">{now}</span></p>
        <div class="badge">
            <img src="https://img.shields.io/badge/IaC-Terraform-blueviolet?style=for-the-badge&logo=terraform" alt="Terraform Badge" />
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
