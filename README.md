
# FitFoodie

FitFoodie is a Django-based fitness tracker application designed to help users track their calorie intake, exercise routines, and overall fitness progress. With FitFoodie, users can log their meals, record workouts, and monitor their calorie balance to achieve their health and fitness goals.

## Features

- **User Authentication**: Secure user authentication system allows users to register, log in, and log out.
  
- **Meal Logging**: Users can log their meals, including details such as meal type, food items consumed, and calorie intake.

- **Workout Logging**: Users can log their workouts, including exercise type, duration, and calories burned.

- **Calorie Tracking**: FitFoodie calculates and tracks users' calorie balance based on their logged meals and workouts.

- **Comprehensive Food Database**: FitFoodie includes a user-friendly interface and a comprehensive food database to make meal logging quick and easy.

- **Exercise Routines**: FitFoodie supports various exercise routines, allowing users to select from a predefined list of exercises or add custom exercises.

## Installation

### Prerequisites

- Python 3
- pip (Python package installer)

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/FitFoodie.git
   ```

2. Navigate to the project directory:

   ```bash
   cd FitFoodie
   ```

3. Create and activate a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

6. Create a superuser (admin account) for accessing the Django admin interface:

   ```bash
   python manage.py createsuperuser
   ```

7. Start the development server:

   ```bash
   python manage.py runserver
   ```

8. Open a web browser and visit `http://127.0.0.1:8000/` to access FitFoodie.

## Usage

- **Register**: Create a new account by registering with your email address and password.

- **Log In**: Log in to your account with your email address and password.

- **Log Out**: Log out of your account to securely end your session.

- **Log Meals**: Log your meals by providing details such as meal type, food items consumed, and calorie intake.

- **Log Workouts**: Log your workouts by providing details such as exercise type, duration, and calories burned.

- **View Calorie Balance**: Monitor your calorie balance to track your progress towards your fitness goals.

## Contributing

Contributions are welcome! If you'd like to contribute to FitFoodie, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-name`).
6. Create a new pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This project was inspired by a passion for health and fitness.
- Special thanks to the Django community for creating such a powerful web framework.

---
