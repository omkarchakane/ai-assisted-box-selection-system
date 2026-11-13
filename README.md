
# AI-Assisted Box Selection System

## Project Overview

A Django-based application that recommends the most
suitable shipping box for ecommerce orders based on
product dimensions, weight capacity, and box cost.

## Features

- Product management
- Shipping box management
- Order and order item management
- Automatic box recommendations
- Dimension validation with rotation
- Weight capacity validation
- Cost-based box selection
- No suitable box handling
- Automated test cases

## Technologies Used

- Python
- Django
- SQLite
- HTML
- Bootstrap
- Git and GitHub


## Installation

### 1. Clone the repository

git clone https://github.com/omkarchakane/ai-assisted-box-selection-system.git

### 2. Open the project folder

cd ai-assisted-box-selection-system

### 3. Create virtual environment

python -m venv venv

### 4. Activate virtual environment

Windows:

venv\Scripts\activate

### 5. Install dependencies

pip install -r requirements.txt

### 6. Set Django secret key

PowerShell:

$env:DJANGO_SECRET_KEY="zyt$47dd-!#on%c3@oad_s0iymjurtz-jw*^7*fy78-^ets@5uv"

### 7. Apply database migrations

python manage.py migrate

### 8. Create admin account

python manage.py createsuperuser

### 9. Start the server

python manage.py runserver

### 10. Run tests

python manage.py test

## Access

Admin: http://127.0.0.1:8000/admin/

## Run Tests

python manage.py test

## Recommendation Logic

The application checks:
- Product dimensions
- Product rotation
- Total order volume
- Total order weight
- Box weight capacity
- Shipping box cost

It selects the lowest-cost eligible box.

## Limitations

The current implementation uses a simplified packing
heuristic. It does not guarantee a physically valid
3D arrangement for multiple products.

## Project Structure

config/
packaging/
README.md
AI_USAGE.md
TEST_OUTPUT.md
