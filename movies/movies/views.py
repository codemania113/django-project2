import json

import django
from django.conf import settings
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def load(request, addr):
    title_list = addr.strip('/').split("/")
    with open('json2.json', 'r') as json_file:
        node = json.load(json_file)
        
        # taking base url as "Movies"
        if title_list[-1] == 'Movies':
            return render(request, 'parent.html', {'node': node, 'addr': addr})
        for child in node['movies']:
            if child['title'] == title_list[-1]:
                node = child
                break
        if node['title'] != title_list[-1]:
            return HttpResponseNotFound('<h1>Page Not Found</h1>')
        
        return render(request, 'child.html', {'node': node})
