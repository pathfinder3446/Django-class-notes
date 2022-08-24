from django.shortcuts import render

from django.http import HttpResponse
# def home(request):
#     print(request)
#     print(request.method)
#     print(request.COOKIES)
#     print(request.META)

#     html='Hello FS Team'
#     return HttpResponse(html)

def home(request):
    return render(request, 'dsApp/index.html')