from django.shortcuts import render

# Create your views here.
def index():
    """Root route for the application."""
    render('index.html', {"name": "Bolaji"})
