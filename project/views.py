from django.http import HttpResponse

# to render html pages


HTML_STRING ="""
  <h1>Hello Ahmed</h1>
"""

def home(request):
    # take in a request -->return response
    return HttpResponse(HTML_STRING)
