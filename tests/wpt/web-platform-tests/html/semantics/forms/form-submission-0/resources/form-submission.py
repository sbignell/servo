def main(request, response):
    if request.headers.get('Content-Type') == 'application/x-www-form-urlencoded':
        result = request.body == 'foo=bara'
    elif request.headers.get('Content-Type') == 'text/plain':
        result = request.body == 'qux=baz\r\n'
    else:
        result = request.POST.first('foo') == 'bar'

    result = result and request.url_parts.query == 'query=1'

    return ([("Content-Type", "text/plain")],
            "OK" if result else "FAIL")
