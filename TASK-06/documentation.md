# Detailed Documentation for Microblog

## Introduction
Microblog is a simple microblogging application built with Flask, a popular Python web framework. This application demonstrates core features of a microblogging platform, including user authentication, posting updates, following users, and viewing posts.

## Project Overview
Microblog provides a platform for users to:
- Register and authenticate accounts
- Post updates and view posts from themselves and others
- Follow other users to see their updates
- Interact with posts through likes and comments

The application is designed to be a lightweight and straightforward example of a web application built with Flask, demonstrating key concepts in web development.

## Main Features
- **User Authentication**: Users can register, log in, and log out. Passwords are securely hashed.
- **User Profiles**: Each user has a profile page where their posts and information are displayed.
- **Post Creation**: Users can create, edit, and delete their posts.
- **Following System**: Users can follow other users to see their updates in their feed.
- **User Interaction**: Users can like and comment on posts (if implemented in the future).

## Functional Components

### User Registration and Authentication
- **Registration:** Users can create a new account by providing a username and email address. The registration form validates input and securely stores user information in the database.
- **Login:** Registered users can log in using their username and password. The system uses sessions to manage user authentication.
- **Logout:** Users can log out, which invalidates their session and redirects them to the login page.

### Post Management
- **Create Post:** Authenticated users can create a new post from their profile or home page.
- **Edit Post:** Users can edit their existing posts to update content.
- **Delete Post:** Users can delete their posts if they no longer wish to display them.

### User Following
- **Follow Users:** Users can follow other users to receive their updates in their feed.
- **View Followers/Following:** Users can view a list of their followers and the users they are following.

### Homepage and Feed
- **Homepage:** The main page displays a feed of posts. Users see posts from users they follow as well as their own posts.
- **Profile Page:** Each user has a profile page that shows their posts and personal information.

## Key Functions

### `create_app()`
**Location:** `app/__init__.py`

**Description:** Initializes and configures the Flask application, sets up database connections, and integrates Flask extensions.

```python
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    login_manager.init_app(app)
    return app

