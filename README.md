[![CircleCI](https://circleci.com/gh/circleci/circleci-docs.svg?style=shield&circle-token=2bd74d82daa65bc8b3f928fe355752dac19a0ff9)](https://circleci.com/gh/circleci/circleci-docs) [![Maintainability](https://api.codeclimate.com/v1/badges/52bf57c9a06b4c1ed18a/maintainability)](https://codeclimate.com/github/timlubanga/Savannah-eProject/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/52bf57c9a06b4c1ed18a/test_coverage)](https://codeclimate.com/github/timlubanga/Savannah-eProject/test_coverage)

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
