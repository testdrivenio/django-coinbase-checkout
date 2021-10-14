# Django Coinbase Checkout

Accept payments using the [Coinbase Checkout API](https://commerce.coinbase.com/docs/api/#checkouts).

## Want to learn how to build this?

Check out the [tutorial](https://testdriven.io/blog/django-coinbase/).

## Want to use this project?

1. Fork/Clone

1. Create and activate a virtual environment:

    ```sh
    $ python3 -m venv venv && source venv/bin/activate
    ```

1. Install the requirements:

    ```sh
    (venv)$ pip install -r requirements.txt
    ```

1. Apply the migrations:

    ```sh
    (venv)$ python manage.py migrate
    ```

1. Add your Coinbase Commerce API key, webhook secret and checkout ID to *settings.py* file:

    ```python
    COINBASE_COMMERCE_API_KEY = '<your coinbase api key here>'
    COINBASE_COMMERCE_WEBHOOK_SHARED_SECRET = '<your coinbase webhook secret here>'
    COINBASE_CHECKOUT_ID = '<your checkout id>'
    ```

1. Run the server:

    ```sh
    (venv)$ python manage.py runserver
    ```
