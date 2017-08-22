from django.http import HttpResponse


def homepage(request):
    return HttpResponse('<h3>this is homepage</h3>')


def test_function():
    return 'test'
