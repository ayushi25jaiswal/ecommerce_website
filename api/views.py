from django.http import JsonResponse

# Create your views here.
def home(request):
    return JsonResponse({'info': 'TEri jalak Sarfi naina madak barfi oh', 'name': 'OH Ayushi'})

