# Food Timetable Backend

A Django-based REST API backend for managing food timetables, meals, and ingredients. This application helps users organize their meal planning by providing a structured way to create and manage weekly meal schedules.

## Features

- Meal Management
  - Create, read, update, and delete meals
  - Add ingredients to meals
  - Track meal descriptions
- Ingredient Management
  - Maintain a database of ingredients
  - Track ingredient prices
  - Associate ingredients with meals
- Timetable Management
  - Create weekly meal schedules
  - Organize meals by day and type (Breakfast, Lunch, Dinner, Snack)
  - Automatic scheduling with Celery tasks

## Technology Stack

- **Python 3.13**
- **Django 5.2.3**: Web framework
- **Django REST Framework 3.16.0**: REST API development
- **Celery 5.5.3**: Asynchronous task queue
- **SQLite**: Database (default)
- **Django CORS Headers**: Cross-Origin Resource Sharing support

## Prerequisites

- Python 3.13 or higher
- pip (Python package manager)
- A message broker (for Celery tasks)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Food-Timetable-Backend.git
   cd Food-Timetable-Backend
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Project Structure

```
food_timetable/          # Main project directory
├── foodManager/         # App for managing meals and ingredients
│   ├── models.py       # Database models for meals and ingredients
│   ├── views.py        # API views
│   └── urls.py         # URL routing
├── timetableManager/    # App for managing food timetables
│   ├── models.py       # Database models for timetables
│   ├── views.py        # API views
│   ├── tasks.py        # Celery tasks
│   └── urls.py         # URL routing
└── core/               # Core functionality and shared components
```

## API Endpoints

### Meals
- `GET /api/meals/`: List all meals
- `POST /api/meals/`: Create a new meal
- `GET /api/meals/{id}/`: Retrieve a specific meal
- `PUT /api/meals/{id}/`: Update a meal
- `DELETE /api/meals/{id}/`: Delete a meal

### Ingredients
- `GET /api/ingredients/`: List all ingredients
- `POST /api/ingredients/`: Create a new ingredient
- `GET /api/ingredients/{id}/`: Retrieve a specific ingredient
- `PUT /api/ingredients/{id}/`: Update an ingredient
- `DELETE /api/ingredients/{id}/`: Delete an ingredient

### Timetable
- `GET /api/timetable/`: List all timetable entries
- `POST /api/timetable/`: Create a new timetable entry
- `GET /api/timetable/{id}/`: Retrieve a specific timetable entry
- `PUT /api/timetable/{id}/`: Update a timetable entry
- `DELETE /api/timetable/{id}/`: Delete a timetable entry

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/awesome-feature`)
3. Commit your changes (`git commit -m 'Add awesome feature'`)
4. Push to the branch (`git push origin feature/awesome-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.
