import os


def set_environment(request):
    return {
        'environment': os.getenv('PY_ENV') if os.getenv('PY_ENV') else 'development'
    }
