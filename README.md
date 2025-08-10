# AirSneaker Backend (Django + DRF + SSLCommerz) - PostgreSQL Ready

This repository contains a Django REST backend for the Air Sneaker storefront.

## Quick start (local)

1. Copy `.env.example` -> `.env` and fill values (SECRET_KEY, DATABASE_URL, SSLC credentials)
2. Create virtualenv and install:
   ```
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```
   python manage.py migrate
   ```
4. Load sample data (optional):
   ```
   python manage.py loaddata fixtures/sample_products.json
   ```
5. Create superuser:
   ```
   python manage.py createsuperuser
   ```
6. Run server:
   ```
   python manage.py runserver
   ```

## Deploy to Render (Postgres)

- Create a Postgres instance on Render, copy DATABASE_URL.
- Create a Web Service on Render from this repo.
- Set environment variables:
  - SECRET_KEY, DEBUG, ALLOWED_HOSTS, DATABASE_URL
  - SSLC_STORE_ID, SSLC_STORE_PASSWORD, SSLC_SUCCESS_URL, SSLC_FAIL_URL, SSLC_CANCEL_URL
- Set Build Command:
  ```
  pip install -r requirements.txt
  python manage.py migrate
  python manage.py loaddata fixtures/sample_products.json
  ```
- Start Command:
  ```
  gunicorn airtag.wsgi:application --bind 0.0.0.0:$PORT
  ```

## Frontend

- Update your frontend `API_BASE` to point to your Render service: e.g. `https://<your-render-service>.onrender.com/api`
- Use the provided checkout flow (POST /api/checkout/) which returns SSLCommerz initiation data including `GatewayPageURL`.

## Notes

- Do NOT commit `.env` to GitHub.
- For production, set DEBUG=False and correct ALLOWED_HOSTS.
- Validate payment callbacks properly in production using SSLCommerz validation APIs.
