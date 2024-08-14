# Hotel Django Project

## Project Overview

This is a Django-based hotel management system. The project includes features for managing hotel rooms, handling user feedback, creating blog posts, and more. It is designed to help hotel owners manage their properties and interact with their customers.

## Features

- **Room Management**: Add and manage hotel rooms with images, descriptions, prices, and booking links.
- **Instagram Feed**: Display images from Instagram.
- **Feedback System**: Collect and manage customer feedback.
- **Blog**: Create and manage blog posts.
- **Comments**: Allow users to comment on blog posts.

## Models

The project includes the following Django models:

- **Room**: Represents a hotel room with images, description, price, and view options.
- **Instagram**: Stores Instagram images.
- **Feedback**: Collects feedback from users with their name, email, and message.
- **Blog**: Represents a blog post with an image, title, and text.
- **Comment**: Allows users to comment on blog posts.
- **User**: Custom user model with phone number authentication and additional fields.

## Requirements

- Python 3.10+
- Django

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/abduvalimurodullayev1/hotel.git
Navigate to the project directory:

bash

cd hotel
Create a virtual environment (optional but recommended):

bash

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:

bash
pip install -r requirements.txt

Apply database migrations:

bash

python manage.py migrate
Run the development server:

bash

python manage.py runserver

Usage
Visit http://127.0.0.1:8000/ in your browser to access the application.
Admin panel is available at http://127.0.0.1:8000/admin/.


Notes
This project does not include an .env file. Ensure you configure your environment variables as needed.


Ensure to have Python 3.10+ installed.


License
This project is licensed under the MIT License.

Contact
For any questions or issues, please contact Abduvali Murodullayev.
