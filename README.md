# Flask URL Shortener

This is a simple URL shortener application built with Flask, a popular Python web framework. The application allows users to submit long URLs and receive shortened versions, making it easier to share links on social media, messaging apps, or any other platform.

## Features

- **Shorten URLs**: Users can enter a long URL, and the application will generate a unique, shortened version of the URL.
- **Redirect to Original URL**: When a user visits the shortened URL, they are automatically redirected to the original, long URL.
- **URL Analytics**: The application tracks the total number of URLs shortened and displays the top 5 most popular shortened URLs based on click counts (social proof).

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/daviesevan/urlshortener.git
   ```

2. Navigate to the project directory:

   ```
   cd flask-url-shortener
   ```

3. Create a virtual environment and activate it:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:

   ```
   flask run
   ```

   The application should now be running at `http://localhost:5000`.

2. Open your web browser and navigate to `http://localhost:5000`.

3. Enter the long URL you want to shorten in the provided input field and click the "Shorten" button.

4. The application will generate a shortened URL for you. Copy this shortened URL and share it with others.

5. When someone visits the shortened URL, they will be automatically redirected to the original, long URL.

6. The application displays the total number of URLs shortened and the top 5 most popular shortened URLs based on click counts (social proof).

## Configuration

The application uses SQLite as the default database. If you want to use a different database, update the `SQLALCHEMY_DATABASE_URI` configuration in the Flask application code.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

This URL shortener application was built using the following technologies:

- [Flask](https://flask.palletsprojects.com/en/2.2.x/) - The Python web framework
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) - The Flask SQLAlchemy extension for database integration

Special thanks to the Flask and Flask-SQLAlchemy communities for their excellent documentation and support.