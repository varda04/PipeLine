<h1 align="center">
  <br>
  <img src="https://i.ibb.co/Pvc6HFPF/PipeLine.png" alt="PipeLine" border="0" width="200">
  <br>
  PipeLine
  <br>
</h1> <h4 align="center">A Django-powered gas utility portal connecting customers and support staff seamlessly — all through one PipeLine 💡</h4> <p align="center"> <a href="#key-features">Key Features</a> • <a href="#getting-started">Getting Started</a> • <a href="#usage">Usage</a> • <a href="#tech-stack">Tech Stack</a> • <a href="#license">License</a> </p>
📌 Why the name "PipeLine"?
It’s a wordplay on gas pipelines and the support workflow pipeline — a neat metaphor for connecting customer issues through a clean and efficient system!

🚀 Key Features
🔐 Role-based login for Customers and Support Representatives
📄 Multiple file attachment logic for support requests
✅ CSRF-protected forms for secure submissions
📬 Admin-side ticket management
🌐 Clean UI templates powered by HTML & CSS
📦 Modular Django app structure

🛠 Getting Started
To run this project locally, make sure you have Python and Django installed. Then:
# Clone the repository
```
git clone https://github.com/varda04/PipeLine.git
```

# Install dependencies (ideally in a virtual environment)
```
pip install -r requirements.txt
```
# Run migrations
```
python manage.py migrate
```
# Run the development server
```
python manage.py runserver
```
Then open your browser and go to:
http://127.0.0.1:8000/

💻 Usage
Visit / to land on the homepage.
Navigate to /customer/ for the customer login and features.
Navigate to /support/ for support staff access.
Submit issues with optional multiple file attachments.
Support reps can view and manage submitted issues. You can use username: support and password: adminpass123 for trial!

🧰 Tech Stack
Python + Django (Backend)
HTML5 + CSS3 (Frontend)
PostgreSQL (Default DB)

Made with 🧠 and ☕ by varda :)
