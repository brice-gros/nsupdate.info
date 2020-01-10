"""
Utility functions to process http request and response
"""

def get_original_remote_address(request):
    """
    For details see https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For
    """
    return request.META['HTTP_X_FORWARDED_FOR'] if 'HTTP_X_FORWARDED_FOR' in request.META else request.META['REMOTE_ADDR']