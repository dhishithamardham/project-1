Spam Message Detector

Overview

Spam Message Detector is a web-based application built using Django that classifies user messages as Spam or Not Spam. Users can enter a message through a simple interface and get instant predictions.

Features

- User-friendly web interface
- Detects spam messages in real time
- Built using Django framework
- Responsive and customizable UI
- Easy to extend with advanced machine learning models

Technologies Used

- Python 3
- Django
- HTML5
- CSS3
- Git
- GitHub

Project Structure

spamproject/
│
├── spamapp/
│   ├── templates/
│   │   └── home.html
│   ├── views.py
│   ├── models.py
│   └── ...
│
├── static/
│   └── css/
│       └── style.css
│
├── spamproject/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── manage.py
├── db.sqlite3
└── README.md

Installation

Clone the Repository

git clone <repository-url>
cd spamproject

Install Dependencies

pip install django

Run the Server

python manage.py runserver

Open your browser and visit:

http://127.0.0.1:8000/

Future Improvements

- Integrate a trained Machine Learning model.
- Improve prediction accuracy.
- Add user authentication.
- Deploy the project online.

Author

M.Dhishitha

Int Mtech Data science Student