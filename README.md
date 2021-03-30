[![CircleCI](https://circleci.com/gh/circleci/Savannah-eProject.svg?style=svg)](https://circleci.com/gh/circleci/circleci-docs)

# Installation Steps

1. Ensure you have python3 installed

2. Clone the repository

3. create a virtual environment using python3 -m venv /path/to/new/virtual/environment.

4. Activate the virtual environment by running source venv/bin/activate

- On Windows use source venv\Scripts\activate

5. Install the dependencies using pip install -r requirements.txt

6. Migrate existing db tables by running python manage.py migrate

7. Run the django development server using python manage.py runserver

# App Testing

Run the tests by running python manage.py tests
