# Movie Review API

A RESTful API for adding, browsing, and reviewing movies built with Django and Django REST Framework. The API includes user authentication, rating systems, and search functionalities.

## Features

- **User Authentication:** Register and obtain authentication tokens.
- **Movie Management:** Add, view, update, and delete movies.
- **Reviews:** Users can add, edit, and delete their reviews for movies.
- **Search:** Search movies by title or description.
- **Ratings:** Rate movies from 1 to 5.
- **Deployment:** Hosted on Render with PostgreSQL database.

## Technologies Used

- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Deployment:** Render
- **Others:** Gunicorn, Whitenoise

## Getting Started

### Prerequisites

- Python 3.8+
- Git
- Virtual Environment Tool

### Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/movie_review_api.git
    cd movie_review_api
    ```

2. **Create and Activate Virtual Environment**

    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the Server**

    ```bash
    python manage.py runserver
    ```

### API Endpoints

- **Register:** `POST /api/register/`
- **Obtain Token:** `POST /api/api-token-auth/`
- **Movies:**
  - `GET /api/movies/`
  - `POST /api/movies/`
  - `GET /api/movies/{id}/`
  - `PUT /api/movies/{id}/`
  - `DELETE /api/movies/{id}/`
- **Reviews:**
  - `GET /api/reviews/`
  - `POST /api/reviews/`
  - `GET /api/reviews/{id}/`
  - `PUT /api/reviews/{id}/`
  - `DELETE /api/reviews/{id}/`

### Deployment

The application is deployed on [Render](https://render.com/). To deploy your own:

1. **Create a Render Account**
2. **Connect Your GitHub Repository**
3. **Set Environment Variables**
4. **Add a PostgreSQL Database**
5. **Deploy**

### Testing

Use tools like Postman or cURL to interact with the API endpoints. Ensure to include the authentication token in the headers for protected routes.

### License

MIT
