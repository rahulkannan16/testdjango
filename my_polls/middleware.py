from prometheus_client import Counter, generate_latest
from prometheus_client.registry import REGISTRY
from django.http import HttpResponse


# Create a Counter metric to count all HTTP requests
http_requests_total = Counter('http_requests_total', 'Total number of HTTP requests')


# Create a Counter metric to count successful HTTP requests (status code 200)
http_requests_success = Counter('http_requests_success', 'Total number of successful HTTP requests')


# Create a Counter metric to count HTTP errors (status code 404)
http_requests_errors = Counter('http_requests_errors', 'Total number of HTTP errors')


class PrometheusMiddleware:
   def __init__(self, get_response):
       self.get_response = get_response

   def __call__(self, request):
       # Increment the total HTTP requests counter for each request
       http_requests_total.inc()
       response = self.get_response(request)


       # Increment the appropriate counter based on the response status code
       if 200 <= response.status_code < 300:
           http_requests_success.inc()
       elif response.status_code == 404:
           http_requests_errors.inc()
       return response


   def metrics(request):
       # Expose all counters in Prometheus format
       content = generate_latest(REGISTRY)
       return HttpResponse(content, content_type='text/plain')
