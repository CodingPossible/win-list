Suggested:

#### Video Demonstration: <URL HERE>

#### Description:
Daily Wins Tracker is a responsive web application designed to help users log, organize, and reflect on their daily achievements. Built as my CS50 Final Project, the application encourages positive habit-tracking and productivity by providing a clear visual record of what the user has successfully accomplished each day.

## Tech Stack
*   **Frontend:** HTML5, CSS3, Jinja2 Templates (with Bootstrap for layout and styling)
*   **Backend:** Python 3, Flask Web Framework
*   **Database:** PostgreSQL

## Key Features
*   **User Authentication:** Secure user registration, password hashing, and login sessions.
*   **Daily Log:** A clean interface to quickly submit "wins" with text and custom categories.
*   **Historical Timeline:** A dashboard displaying past wins grouped by date.
*   **Streak Tracking:** A background logic feature calculating how many consecutive days the user has recorded a win.

## File Structure & Component Overview
*   `app.py` - The main Python controller containing Flask routing, session controls, and API endpoints.
*   `helpers.py` - Custom Python middleware for login requirements, formatting dates, and calculating user streaks.
*   `schema.sql` - The architectural blueprint for the PostgreSQL tables (Users, Wins, Categories).
*   `templates/` - Jinja2 layout pages including `layout.html` (base structure), `login.html`, `index.html` (the daily dashboard), and `history.html`.
*   `static/` - Custom CSS overrides (`styles.css`) and client-side JavaScript assets.

## Design Choices & Challenges
*   **Database Choice:** I migrated from CS50's default SQLite to PostgreSQL to simulate production-ready environments, requiring precise data type handling for timestamps.
*   **State Retention:** Using Jinja loops allowed the frontend to remain lightweight and fast by pre-rendering data directly from SQL queries before delivering pages to the client.

## Installation & Setup
1.  **Clone the repository:**
    ```bash
    git clone <YOUR_REPOSITORY_URL>
    cd <YOUR_PROJECT_DIRECTORY_NAME>
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure environment variables:**
    Create a `.env` file and define your database credentials:
    ```env
    DATABASE_URL="postgresql://username:password@localhost:5432/wins_db"
    FLASK_SECRET_KEY="your-secret-key"
    ```
4.  **Run the Flask application:**
    ```bash
    flask run
    ```
