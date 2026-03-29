# a2-smart-schedule

Django site for the **Smart Game Scheduling Platform** concept: a landing page with product copy, a demo interest form, and static styling.

## Prerequisites

- **Python 3.10+** (3.12 works with the current stack)

## Run locally

From the project root:

1. **Create and activate a virtual environment**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   On Windows: `.venv\Scripts\activate`

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Apply database migrations** (needed for sessions and the Django admin stack)

   ```bash
   python manage.py migrate
   ```

4. **Start the development server**

   ```bash
   python manage.py runserver
   ```

   Open **http://127.0.0.1:8000/** in your browser.

### Use a different port

Pass the port number as the last argument:

```bash
python manage.py runserver 8383
```

Then use **http://127.0.0.1:8383/**.

## Project layout

| Path | Purpose |
|------|---------|
| `smartschedule/` | Django project settings and root URL config |
| `siteapp/` | App with views, forms, and templates for the public site |
| `static/css/site.css` | Site styles |
| `manage.py` | Django CLI entry point |

## License

See [LICENSE](LICENSE).
