def check_response_success(response):
    status_code = response.status_code
    if 200 <= status_code <= 299:
        return True
    return False


def check_response_header_json(response):
    headers = response.headers
    content_type = headers.get('content-type')
    if content_type.startswith('application/json') or content_type.startswith('application/hal+json'):
        return True
    return False
