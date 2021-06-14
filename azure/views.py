import requests

from django.shortcuts import render


def login(request):
    app_id = '07218E15-xxxxxxxxxxxxxx-xxxxxxxBCA66'
    state = 'user1'
    scope = 'vso.work'
    callback = 'https://localhost:8000/azure/redirect/'
    context = {
        'url': f'https://app.vssps.visualstudio.com/oauth2/authorize?client_id={app_id}&response_type=Assertion&state={state}&scope={scope}&redirect_uri={callback}',
    }
    return render(request, 'login.html', context)


def redirect(request):
    context = {}
    code = request.GET.get('code')
    state = request.GET.get('state')
    url = 'https://app.vssps.visualstudio.com/oauth2/token'
    client_secret = 'eyJ0eXAiOiJKV1QiRxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx3AtSGpJS2xGWHo5M3VfVjBabyJ9.exxxxxxxxxxxxxxxxGUxNS1lMzk4LTQ2ZWUtYmM5Mi00NDEwYzdmYmNhNjYiLCJjc2kiOiI1ODA0YTIxZS1mOWZmLTQzNGEtYmRmYy0zNTAwMWYzYjA2YjEiLCJuYW1laWQiOiI4NDkzZmU0Ni01YjhhLTZhNDItYmRiZS04YTIzNWYyNzEzOTgiLCJpc3MiOiJhcHAudnN0b2tlbi52aXN1YWxzdHVkaW8uY29tIiwiYXVkIjoiYXBwLnZzdG9rZW4udmlzdWFsc3R1ZGlvLmNvbSIsIm5iZiI6MTYyMzY2NTEwMywiZXhwIjoxNzgxNDMxNTAzfQ.2L7e8-PmXYbE6kFkM4epvhcFtO-q4hEFtL2NtQnikHuwRCV4E65H68gYMZ3m4_MnOQpmxsI-gqZpFepbp5krU5KKe2dJatcRDFyNLpLCmy-97vKmO_OZD77x0HCyr58hlBH9ISpnm8DNyVV-PlzC6WgiVJv08StU593WNT8jHmy4asWCp0Tf7fGhdSv4OiQMHX2tQt_unYUYL9VCRhb6Y3TZTapDwVvlb5zk0sQbAJHigRftGlfgc33J6NHq6h0EH4F12E4_sWtYq-XUarAa4oEKJFVpEmxx87T0MCoh4o8cJZAD4wRyyuWxD24HlnW10aTIkS3trHnL9jd77i4HzA'
    data = {
        'client_assertion_type': 'urn:ietf:params:oauth:client-assertion-type:jwt-bearer',
        'client_assertion': client_secret,
        'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer',
        'assertion': code,
        'redirect_uri': 'https://localhost:8000/azure/redirect/',
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    response = requests.post(url=url, data=data, headers=headers)
    context = response.json()
    return render(request, 'redirect.html', context)
