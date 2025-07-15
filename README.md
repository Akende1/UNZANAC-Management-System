# UNZANAC-Management-System

A collaborative project building a church management system with Django (backend) and React (frontend).

## Features

- User authentication and management (`auth_app`)
- Committees management (`commitees`)
- Donations tracking (`donations`)
- Events management (`events`)
- Finance management (`finance`)
- Members management (`members`)
- Notifications system (`notifications`)

## Project Structure

```
UNZANAC-Management-System/
│
├── UNZANAC_Management_System/   # Django project settings and root urls
├── auth_app/                    # Authentication app
├── commitees/                   # Committees app
├── donations/                   # Donations app
├── events/                      # Events app
├── finance/                     # Finance app
├── members/                     # Members app
├── notifications/               # Notifications app
├── templates/                   # Shared templates (e.g., base.html)
├── manage.py
└── requirements.txt
```

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/UNZANAC-Management-System.git
   cd UNZANAC-Management-System
   ```

2. **Create a virtual environment and activate it:**
   ```sh
   python -m venv venv
   venv\Scripts\activate   # On Windows
   # source venv/bin/activate  # On Linux/Mac
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure the database:**
   - By default, the project uses SQLite3 for development.
   - No extra configuration is needed for SQLite.

5. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

6. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

7. **Access the app:**
   - Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Dummy Templates

Each app contains a simple dummy template at:
- `auth_app/templates/auth_app/index.html`
- `commitees/templates/commitees/index.html`
- `donations/templates/donations/index.html`
- `events/templates/events/index.html`
- `finance/templates/finance/index.html`
- `members/templates/index.html`
- `notifications/templates/notifications/index.html`

## Navigation

The main navigation is provided in `templates/base.html` and links to each app's dummy index page.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Create a new Pull Request

---

**Note:**  
If you want to use PostgreSQL or another database, update the `DATABASES` setting in `UNZANAC_Management_System/settings.py` accordingly.
