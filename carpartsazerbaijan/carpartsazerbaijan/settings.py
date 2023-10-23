import os
import django_heroku
import dj_database_url

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-x4#2&gx-+epl=^hs1^b74!s@5@$um5o26@hxmzj5ji!+^+!!ip'

DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'admin_interface',
    'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'car_parts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'carpartsazerbaijan.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'carpartsazerbaijan.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'az'

TIME_ZONE = 'Asia/Baku'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# settings.py

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

X_FRAME_OPTIONS = 'SAMEORIGIN'
SILENCED_SYSTEM_CHECKS = ['security.W019']



CAR_BRANDS_CHOICES = (
    ('Toyota', 'Toyota'),
    ('Ford', 'Ford'),
    ('Honda', 'Honda'),
    ('Chevrolet', 'Chevrolet'),
    ('Nissan', 'Nissan'),
    ('Volkswagen', 'Volkswagen'),
    ('BMW', 'BMW'),
    ('Mercedes-Benz', 'Mercedes-Benz'),
    ('Audi', 'Audi'),
    ('Hyundai', 'Hyundai'),
    ('Kia', 'Kia'),
    ('Mazda', 'Mazda'),
    ('Subaru', 'Subaru'),
    ('Jeep', 'Jeep'),
    ('Lexus', 'Lexus'),
    ('Chrysler', 'Chrysler'),
    ('Volvo', 'Volvo'),
    ('Porsche', 'Porsche'),
    ('Jaguar', 'Jaguar'),
    ('Land Rover', 'Land Rover'),
)

CAR_PARTS_CHOICES = (
    ('Spoiler', 'Spoiler'),
    ('LED işıq', 'LED işıq'),
    ('Təkər', 'Təkər'),
    ('Dırnaq', 'Dırnaq'),
    ('Ayrıqca', 'Ayrıqca'),
    ('Stop lampa', 'Stop lampa'),
    ('Aydınlatma', 'Aydınlatma'),
    ('Motor', 'Motor'),
    ('Suspension', 'Suspension'),
    ('Qapı', 'Qapı'),
    ('Pəncərə', 'Pəncərə'),
    ('Yan pəncərə', 'Yan pəncərə'),
    ('Bağaj', 'Bağaj'),
    ('Stabilizator çubuğu', 'Stabilizator çubuğu'),
    ('Süspension', 'Süspension'),
    ('Tormoz', 'Tormoz'),
    ('Şaquliq', 'Şaquliq'),
    ('AirBag', 'AirBag'),
    ('Elektrika', 'Elektrika'),
    ('İnteriör', 'İnteriör'),
    ('Təmizlənmə', 'Təmizlənmə'),
    ('Yağ', 'Yağ'),
    ('Dəmir', 'Dəmir'),
    ('Plastik', 'Plastik'),
    ('Hərəkət', 'Hərəkət'),
    ('Zincir', 'Zincir'),
    ('Ağır qışıq', 'Ağır qışıq'),
    ('Hava filteri', 'Hava filteri'),
    ('Elektrik sistemi', 'Elektrik sistemi'),
    ('Dəmir əşyalar', 'Dəmir əşyalar'),
    ('Süspension parçaları', 'Süspension parçaları'),
    ('Qapı hissələri', 'Qapı hissələri'),
    ('Zəngər', 'Zəngər'),
    ('Difuzor', 'Difuzor'),
    ('Kuzov', 'Kuzov'),
    ('Avtomobil yastıqları', 'Avtomobil yastıqları'),
    ('Təzələmə', 'Təzələmə'),
    ('Yağ filteri', 'Yağ filteri'),
    ('Yan qapı', 'Yan qapı'),
    ('Çubuq', 'Çubuq'),
    ('Vixlop truba', 'Vixlop truba'),
    ('İskarpin', 'İskarpin'),
    ('Labavoy', 'Labavoy'),
    ('Sirqalar', 'Sirqalar'),
    ('Vəziyyət', 'Vəziyyət'),
    ('Qapi elceyi', 'Qapi elceyi'),
)

django_heroku.settings(locals())