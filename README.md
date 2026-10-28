# Student Identity — Django Profile Website

A responsive student profile website developed with **Django**. This project builds on the original *Django Context Assignment* by adding a database-backed **Home Page**, a **Student model**, and **Django Admin** integration.

## Project Features

- **Original Index Page:** Displays profile information using a Django context dictionary and template filters.
- **New Home Page:** Displays student details dynamically from the database using the Django ORM and templates.
- **Student Model:** Stores seven fields with suitable Django data types and validation constraints.
- **Django Admin:** Supports adding and editing student information, including a profile photo.
- **Responsive UI:** Custom HTML and CSS with a purple, lavender, and pink visual theme.
- **Media Support:** Displays uploaded photos through Django's media configuration.

## Student Model

| Field | Django Field Type | Purpose |
| --- | --- | --- |
| `std_name` | `CharField` | Student's full name. |
| `std_id` | `CharField` (`unique=True`) | Unique university identifier, preserved as text. |
| `age` | `PositiveIntegerField` | Student's age as a non-negative integer. |
| `date_of_birth` | `DateField` | Date of birth. |
| `address` | `CharField` (choices) | City selected from predefined options. |
| `salary` | `DecimalField` | Salary with two decimal places. |
| `photo` | `ImageField` | Uploaded student photo, stored under `media/images/`. |

## Technologies

- Python and Django
- SQLite
- Django ORM, Templates, and Template Language (DTL)
- HTML5 and CSS3
- Pillow (for `ImageField`)

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/MayarAl-habbash/Django-Context-Assignment.git
cd Django-Context-Assignment
```

### 2. Create and activate a virtual environment

**Windows (Command Prompt):**

```bat
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

> **Note:** `Pillow` must be included in `requirements.txt` because the Student model uses an `ImageField`.

### 4. Apply database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create an admin account

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

## Available Pages

| URL | Description |
| --- | --- |
| `http://127.0.0.1:8000/` | Original Index Page. |
| `http://127.0.0.1:8000/homepage/` | New database-driven Student Home Page. |
| `http://127.0.0.1:8000/admin/` | Django administration panel. |

## How to Add Student Data

1. Open `/admin/` and sign in with the superuser account.
2. Under **Pages → Students**, select **Add student**.
3. Complete the student fields, upload a photo, and click **Save**.
4. Visit `/homepage/` to see the stored information displayed in the profile layout.

**Important:** The Home Page currently displays the **first Student record** returned by the model's default university-ID ordering. If there are no records in the database, it displays an empty-state message.

## Project Notes

- `db.sqlite3` and the local virtual environment are excluded from version control. A fresh clone starts without saved student records; add one using Django Admin.
- Uploaded media is intended for the local development project. Use demonstration data rather than sensitive personal information in a public repository.
- The project uses Django's development server and is **not configured for production deployment**.

---

**Project:** Django Student Identity  
**Repository:** [MayarAl-habbash/Django-Context-Assignment](https://github.com/MayarAl-habbash/Django-Context-Assignment)
