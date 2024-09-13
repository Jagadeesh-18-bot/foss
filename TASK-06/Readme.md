# Microblog

## Overview
Microblog is a simple microblogging application built with Flask, a Python web framework. It provides a platform for users to post short updates, follow other users, and interact with posts.

## Features
- User authentication and registration
- Posting and editing updates
- Following other users and viewing their posts
- A simple and clean user interface
- Admin interface for managing users and posts

## Getting Started

### Prerequisites
- Python 3.7 or higher
- Flask
- Other dependencies listed in `requirements.txt`

### Installation
To set up the project locally, follow these steps:

```bash
# Clone the repository
git clone https://github.com/miguelgrinberg/microblog.git

# Navigate to the project directory
cd microblog

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Initialize the database
python db_create.py

# Run the application
flask run

Usage
* Open a web browser and go to http://localhost:5000 to access the application.
* Register an account and start posting updates, following other users, and exploring the application.
Contributing
1)Fork the repository.
2)Create a new branch (git checkout -b feature/YourFeature).
3)Make your changes and commit them (git commit -am 'Add new feature').
4)Push to the branch (git push origin feature/YourFeature).
5)Create a pull request.

🖱️
