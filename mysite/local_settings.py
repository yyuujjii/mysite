import os

SECRET_KEY = 'jx19rs6ish5%w6^koyhw8!uelw+j!)^cpk&l-m2o5z3il6o7sn'

# settings.pyからそのままコピー
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# settings.pyからそのままコピー
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True  # ローカルでDebugできるようになります
