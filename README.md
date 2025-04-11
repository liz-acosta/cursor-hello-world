# Pokedex Flask Application

A simple Flask web application that displays Pokemon information from a SQLite database.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Setup

1. Clone this repository
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Database Setup

1. Make sure you have the `pokemon.txt` file in the root directory with Pokemon data in the following format:
   ```
   id|name|description
   ```
   Example:
   ```
   1|Bulbasaur|A strange seed was planted...
   ```

2. Initialize the database with the Pokemon data:
   ```bash
   python init_db.py
   ```

## Running the Application

1. Make sure your virtual environment is activated
2. Run the Flask application:
   ```bash
   python app.py
   ```
3. Open your web browser and navigate to `http://localhost:5000`

## Project Structure

```
pokedex/
├── app.py              # Main Flask application
├── init_db.py          # Database initialization script
├── pokemon.txt         # Pokemon data file
├── database.db         # SQLite database
├── requirements.txt    # Python dependencies
├── .github/
│   └── workflows/
│       └── sonarqube.yml  # SonarQube workflow configuration
├── static/
│   └── styles.css      # CSS styles
└── templates/
    ├── index.html      # Main page template
    └── profile.html    # Pokemon profile template
```

## Features

- View all Pokemon in a grid layout
- Click on a Pokemon to view its detailed profile
- Responsive design that works on all screen sizes
- Clean and modern user interface
- Pokemon images loaded directly from PokeAPI
- Automated code quality checks with SonarQube

## Code Quality

This project uses SonarQube Cloud for code quality analysis. The analysis runs automatically on pull requests. To set up SonarQube:

1. Create a SonarQube Cloud account
2. Generate a SonarQube token
3. Add the following secrets to your GitHub repository:
   - `SONAR_TOKEN`: Your SonarQube authentication token
   - `SONAR_HOST_URL`: Your SonarQube Cloud instance URL

The SonarQube analysis will run automatically when:
- A new pull request is created
- New commits are pushed to an existing pull request
- A pull request is reopened 