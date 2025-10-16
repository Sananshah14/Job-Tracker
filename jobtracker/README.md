# Job-Tracker

A modern Django web application to track and manage your job applications.

## Features

- User registration and login
- Dashboard with sidebar navigation
- Add, update, and delete job applications
- Job list and management
- Job statistics with charts
- Responsive, modern UI (Bootstrap)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Sananshah14/Job-Tracker.git
cd Job-Tracker
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate   # On Mac/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, install manually:

```bash
pip install django djangorestframework djangorestframework-simplejwt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create a Superuser (Optional, for admin access)

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to use the app.

## Project Structure

```
jobtracker/
├── accounts/
├── jobs/
│   └── templates/
│       └── jobs/
│           ├── base.html
│           ├── dashboard.html
│           ├── job_list.html
│           ├── add_job.html
│           ├── update_job.html
│           ├── delete_job.html
│           ├── job_statistics.html
│           ├── login.html
│           ├── signup.html
│           └── ...
├── jobtracker/
└── manage.py
```

## License

MIT License

---

**Happy job tracking!**