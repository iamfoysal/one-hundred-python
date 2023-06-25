import os
import sys
import subprocess


def create_django_project():
    project_dir = input("Enter the project directory name: ")
    os.makedirs(project_dir)
    os.chdir(project_dir)
    project_name = input("Enter the project name: ")
    print("Creating virtual environment...")

    subprocess.run(["python", "-m", "venv", "env"])
    if sys.platform.startswith('win'):
        activate_cmd = os.path.join("env", "Scripts", "activate")
        subprocess.call(activate_cmd, shell=True)
    else:
        activate_cmd = os.path.join("env", "bin", "activate")
        subprocess.call(f"source {activate_cmd}", shell=True)

    print("Installing Django and other packages...")
    with open(".gitignore", "w") as f:
        f.write("env/\n")
        f.write("*.pyc\n")
        f.write("__pycache__/\n")
        f.write("db.sqlite3\n")
        f.write("media/\n")
        f.write("staticfiles/\n")
        f.write(".DS_Store\n")

    subprocess.run(["pip", "install", "django"])
    subprocess.run(["pip", "freeze", ">", "requirements.txt"], shell=True)
    subprocess.run(["django-admin", "startproject", project_name])
    os.chdir(project_name)

    app_name = input("Enter the app name: ")
    print("Creating app...", app_name)
    subprocess.run(["python", "manage.py", "startapp", app_name])

    with open(os.path.join(project_name, "settings.py"), "r") as f:
        lines = f.readlines()
    with open(os.path.join(project_name, "settings.py"), "w") as f:
        for line in lines:
            f.write(line)
            if line.startswith("INSTALLED_APPS = ["):
                f.write(f"    '{app_name}',\n")
            if line.startswith("ALLOWED_HOSTS = ["):
                f.write(f"ALLOWED_HOSTS = ['*']\n")
            if line.startswith("LANGUAGE_CODE = 'en-us'"):
                f.write(f"LANGUAGE_CODE = 'en-in'\n")
            if line.startswith("TIME_ZONE = 'UTC'"):
                f.write(f"TIME_ZONE = 'Asia/Dhaka'\n")
            if line.startswith("STATIC_URL = '/static/'"):
                f.write(f"STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')\n")
                f.write(f"STATICFILES_DIRS = [\n")
                f.write(f"    os.path.join(BASE_DIR, 'static')\n")
                f.write(f"]\n")
                f.write(f"MEDIA_URL = '/media/'\n")
                f.write(f"MEDIA_ROOT = os.path.join(BASE_DIR, 'media')\n")

            if line.startswith("DATABASES = {"):
                f.write(f"DATABASES = {{\n")
                f.write(f"    'default': {{\n")
                f.write(f"        'ENGINE': 'django.db.backends.sqlite3',\n")
                f.write(f"        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),\n")
                f.write(f"    }}\n")
                f.write(f"}}\n")

    with open(os.path.join(app_name, "urls.py"), "w") as f:
        f.write(f"from django.urls import path\n\n")
        f.write(f"urlpatterns = [\n")
        f.write(f"]\n")

    with open(os.path.join(project_name, "urls.py"), "r") as f:
        lines = f.readlines()
    with open(os.path.join(project_name, "urls.py"), "w") as f:
        for line in lines:
            f.write(line)
            if line.startswith("from django.urls import path"):
                f.write(f"from django.urls import path, include\n")
            if line.startswith("urlpatterns = ["):
                f.write(f"    path('', include('{app_name}.urls')),\n")

    with open(os.path.join(app_name, "models.py"), "w") as f:
        f.write(f"from django.db import models\n\n")
        f.write(f"class {app_name.capitalize()}(models.Model):\n")
        f.write(f"  name = models.CharField(max_length=100)\n")
        f.write(f"  age = models.IntegerField()\n")
        f.write(f"  email = models.EmailField()\n\n")
        f.write(f"  def __str__(self):\n")
        f.write(f"    return self.name\n")

    with open(os.path.join(app_name, "admin.py"), "w") as f:
        f.write(f"from django.contrib import admin\n")
        f.write(f"from .models import {app_name.capitalize()}\n\n")
        f.write(f"admin.site.register({app_name.capitalize()})\n")

    subprocess.run(["python", "manage.py", "makemigrations"])
    subprocess.run(["python", "manage.py", "migrate"])

    print("Creating superuser... here username is 'admin' Enter the password for admin user")
    subprocess.run(["python", "manage.py", "createsuperuser",
                   "--username=admin", "--email=admin@example.com"])
    subprocess.run(["python", "manage.py", "runserver"])


if __name__ == "__main__":
    create_django_project()
