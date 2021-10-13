import logging

from coinbase_commerce.client import Client
from coinbase_commerce.error import SignatureVerificationError, WebhookInvalidPayload
from coinbase_commerce.webhook import Webhook
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from core import settings


def home_view(request):
    client = Client(api_key=settings.COINBASE_COMMERCE_API_KEY)
    checkout = client.checkout.retrieve(settings.COINBASE_CHECKOUT_ID)
    checkout_link = f'https://commerce.coinbase.com/checkout/{checkout.id}'

    return render(request, 'home.html', {
        'checkout': checkout,
        'checkout_link': checkout_link,
    })


@csrf_exempt
@require_http_methods(['POST'])
def coinbase_webhook(request):
    import logging

    request_data = request.body.decode('utf-8')
    request_sig = request.headers.get('X-CC-Webhook-Signature', None)
    webhook_secret = settings.COINBASE_COMMERCE_WEBHOOK_SHARED_SECRET

    try:
        event = Webhook.construct_event(request_data, request_sig, webhook_secret)

        # List of all Coinbase webhook events:
        # https://commerce.coinbase.com/docs/api/#webhooks

        if event['type'] == 'charge:confirmed':
            logger.info('Payment confirmed.')
            customer_id = event['data']['metadata']['custom']
            # TODO: run some custom code here
            # you can also use 'customer_id'
            # to fetch an actual Django user

    except (SignatureVerificationError, WebhookInvalidPayload) as e:
        return HttpResponse(e, status=400)

    logger.info(f'Received event: id={event.id}, type={event.type}')
    return HttpResponse('ok', status=200)
