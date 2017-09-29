from django.shortcuts import render


# Create your views here.
def index(request):
    """Root route for the application."""
    return render(request, 'index.html')
