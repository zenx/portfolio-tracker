# Sample Django Investment Portfolio Tracker App
Sample Django Project for the [Pybites](https://pybit.es/) Code Clinic sessions. 

## Instructions
1. Create a free account at https://marketstack.com/
2. Add the token to the `MARKETSTACK_API_KEY` environment variable or to the `MARKETSTACK_API_KEY` setting in `settings.py`
3. Install requirements with `pip install requirements.txt`
4. Execute database migrations with `python manage.py migrate`
5. To access the administration site create a superuser with `python manage.py createsuperuser`
6. Run the project on your local machine with the command `python manage.py runserver`
7. Access http://127.0.0.1:8000/ for the web application and http://127.0.0.1:8000/admin/ for the administration site
8. Add some assets to the database using the administration site (sample tickers: `TSLA`, `AAPL`, `BABA`, `NVDA`, `AMZN`)
9. Retrieve prices from Marketstach using `python manage.py load_prices`
10. Open http://127.0.0.1:8000/, add buy/sell orders and track your investment portfolio

## Management commands
- `load_prices`: Retrieves the last end of day prices from Marketstack for all the assets and stores them in the database. This command can be scheduled to run on a daily basis with cron.

## Additional Resources
- Django models – https://docs.djangoproject.com/en/4.1/topics/db/models/
- Many-to-one relationships – https://docs.djangoproject.com/en/4.1/topics/db/examples/many_to_one/
- Django forms – https://docs.djangoproject.com/en/4.1/topics/forms/
- Django form field validation – https://docs.djangoproject.com/en/4.1/ref/forms/validation/
- Creating forms from models – https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/
- Making queries with the Django ORM – https://docs.djangoproject.com/en/4.1/topics/db/queries/
- Using `aggregate()` to generate aggregates over a QuerySet – https://docs.djangoproject.com/en/4.1/topics/db/aggregation/#generating-aggregates-over-a-queryset
- Django `F()` query expressions – https://docs.djangoproject.com/en/4.1/ref/models/expressions/
- Serving static files during development – https://docs.djangoproject.com/en/4.1/howto/static-files/#serving-static-files-during-development

## Book
[<img src="https://djangobyexample.com/static/v4/img/django_by_example_4_cover.png" style="width:140px;"  align="left">](https://djangobyexample.com/)
Learn more with [Django 4 by Example](https://djangobyexample.com/). This book will walk you through the creation of four real-world applications, solving common problems, and implementing best practices, using a step-by-step approach that is easy to follow. After reading this book, you will have a good understanding of how Django works and how to build practical, advanced web applications.
