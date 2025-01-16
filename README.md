# Copal Manager

Copal Manager is a web application designed to simplify contract management for a concierge service. It allows you to easily create, edit, and manage contracts for clients. The app generates a database containing client information, their real estate properties, and contract details. Additionally, it can automatically generate pre-filled contracts in PDF format to save time and improve workflow efficiency.

## Features
	•	Manage client data, real estate properties, and contracts.
	•	Automatically generate pre-filled contracts in PDF format.
	•	Use of SQLite as the database backend for development and production.

## Installation 

1.	Clone the repository:

		git clone https://github.com/username/copal.git

2.	Navigate to the project directory:

		cd copal

3.1	Create a virtual environment:

		python3 -m venv .env
  
3.2.a Activate virtual environment (For MacOS/Linux):

		`source .env/bin/activate`  
  
3.2.b Activate virtual environment (For Windows):

		`.env\Scripts\activate` 

5.	Install the required dependencies:

		pip install -r requirements.txt

6.	(Optional) Apply the database migrations:

		python manage.py migrate

7.	Run the development server:

		python manage.py runserver

The project will be accessible at http://127.0.0.1:8000.

## Usage
	•	After running the server, visit the provided local URL to access the web app.
	•	You can start managing clients, properties, and contracts via the admin interface or custom views.

Configuration
	•	SQLite is used by default for the database. No additional configuration is needed for the database.
	•	For production deployment, you can configure additional settings, such as enabling static file handling, using a production database, and setting DEBUG = False in settings.py.

## API

The project initially included an intention to develop a separate front-end, but due to time limitations, I couldn’t complete the front-end part. However, I coded a REST API that is available in this repository.

You can find the code for the API under the api/ folder. Feel free to use it for connecting with the front-end if needed.

## Contributing

If you would like to contribute to this project, feel free to open an issue or submit a pull request. Contributions are always welcome!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
