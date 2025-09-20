🌱 Johgaro Agricultural Products Website

This is a Django-powered agricultural products website for Johgaro Company Limited.
The platform showcases agricultural imports, provides company information, and integrates features such as a News API to keep users updated on agricultural trends worldwide.

🚀 Features

🏡 Home Page – Company introduction & mission.

🌍 Products Pages – Agricultural products from different countries.

📰 News API Integration – Live agricultural and business-related news.

📞 Contact Page – Customers can reach out easily.

📑 About Page – Company background, mission, and vision.

📂 Project Structure
johgaro-website/
│── manage.py
│── requirements.txt
│── johgaro/            # Main Django project
│── products/           # App for agricultural products
│── news/               # App for News API integration
│── templates/          # HTML templates
│── static/             # CSS, JS, images
│── .venv/              # Virtual environment (not tracked in Git)

🛠️ Installation & Setup
1. Clone the Repository
git clone https://github.com/254jack/johgaro-website.git
cd johgaro-website

2. Create & Activate Virtual Environment

Linux/macOS:

python3 -m venv venv
source venv/bin/activate


Windows (PowerShell):

python -m venv venv
venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Run Database Migrations
python manage.py migrate

5. Run the Development Server
python manage.py runserver


Then open your browser and visit 👉 http://127.0.0.1:8000/

🌐 Deployment

This project can be deployed on:

Heroku

PythonAnywhere

Vercel (with Django backend via API routes)

Any VPS (Nginx + Gunicorn + PostgreSQL)

🤝 Contributing

Pull requests are welcome!
If you’d like to contribute:

Fork the repo

Create a new branch (feature/new-feature)

Commit your changes

Open a Pull Request

📜 License

This project is licensed under the MIT License.

✨ Johgaro – Building a world where agriculture meets technology.
