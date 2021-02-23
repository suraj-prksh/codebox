from django.shortcuts import render
from django.http import JsonResponse, HttpResponseForbidden
import requests
from django.contrib.auth.decorators import login_required
import json
RUN_URL = 'https://api.hackerearth.com/v3/code/run/'

@login_required
def ide(request):
    return render(request, 'ide/ide.html', {})


# From HackerEarth API
def runCode(request):
    if request.is_ajax():
        source = request.POST['source']
        lang = request.POST['lang']
        data = {
            'client_secret': '6bd33be8349bbbb9496f094d690c6d9141a5d9ea',
            'async': 0,
            'source': source,
            'lang': lang,
            'time_limit': 5,
            'memory_limit': 262144,
        }
        if 'input' in request.POST:
            data['input'] = request.POST['input']
        r = requests.post(RUN_URL, data=data)
        return JsonResponse(r.json(), safe=False)
    else:
        return HttpResponseForbidden()
