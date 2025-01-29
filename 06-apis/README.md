# APIs

This course is about developing APIs using Python and Django.

## Module 1

- [Assignment 1: First API](module1/assignment1/README.md)
- [Quiz](module1/index.html)

## Module 2: Django Rest Framework (DRF)

To set up new project, you can use below commands.

```shell
pipenv install django
pipenv shell
django-admin startproject myproject
python manage.py startapp myapp
pipenv install djangorestframework
```

Open `settings.py` file and add `rest_framework` to the `INSTALLED_APPS` list.

- [Assignment 1: BookList API](module2/assignment1/README.md)
- [Assignment 2: Restaurant Menu API using serialization](module2/assignment2/README.md)
- [Quiz](module2/index.html)

## Module 3: Filtering, Ordering and Searching and Security

This module explains how to implement filtering, ordering of data based on certain fields and searching.
The module also includes authentication and authorization features built in Django Rest Framework.

- [Assignment 1: Restaurant Menu API - Filtering, Ordering](module3/assignment1/README.md)
- [Assignment 2: User account management](module3/assignment2/README.md)
- [Quiz](module3/index.html)

## Module 4: 

This module includes a project building restaurant menu API with groups like manager, customer and delivery-person. A customer can also make an order.

- [Assignment: Little Lemon API Project](module4/assignment1/README.md)