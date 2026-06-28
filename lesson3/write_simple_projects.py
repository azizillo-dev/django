from pathlib import Path
import subprocess
import textwrap

base = Path(r'D:\django\lesson3')
projects = [
    ('vazifa3', ['books', 'users', 'products']),
    ('vazifa4', ['blog', 'services', 'contacts']),
    ('vazifa5', ['menu', 'orders', 'reviews']),
]

for folder, apps in projects:
    project_dir = base / folder
    project_dir.mkdir(parents=True, exist_ok=True)

    if not (project_dir / 'manage.py').exists():
        subprocess.run(['D:\\django\\lesson3\\vazifa3\\venv\\Scripts\\python.exe', '-m', 'django', 'startproject', 'config', '.'], cwd=project_dir, check=True)

    for app in apps:
        app_dir = project_dir / app
        if not app_dir.exists():
            subprocess.run(['D:\\django\\lesson3\\vazifa3\\venv\\Scripts\\python.exe', 'manage.py', 'startapp', app], cwd=project_dir, check=True)

    settings_path = project_dir / 'config' / 'settings.py'
    settings_text = settings_path.read_text(encoding='utf-8')
    for app in apps:
        if f"'{app}'," not in settings_text:
            settings_text = settings_text.replace(
                "    'django.contrib.staticfiles',\n",
                "    'django.contrib.staticfiles',\n    '" + app + "',\n",
                1
            )
    settings_path.write_text(settings_text, encoding='utf-8')

    urls_path = project_dir / 'config' / 'urls.py'
    urls_text = urls_path.read_text(encoding='utf-8')
    if 'from django.urls import include, path' not in urls_text:
        urls_text = urls_text.replace('from django.urls import path', 'from django.urls import include, path')
    routes = ''.join([f"    path('{app}/', include('{app}.urls')),\n" for app in apps])
    if 'urlpatterns = [' in urls_text:
        urls_text = urls_text.replace('urlpatterns = [\n', 'urlpatterns = [\n' + routes)
    urls_path.write_text(urls_text, encoding='utf-8')

    for app in apps:
        app_dir = project_dir / app
        (app_dir / 'views.py').write_text(textwrap.dedent(f'''\
            from django.http import HttpResponse

            def home(request):
                return HttpResponse("{app.capitalize()} home")

            def list_items(request):
                return HttpResponse("{app.capitalize()} list")
        '''), encoding='utf-8')
        (app_dir / 'urls.py').write_text(textwrap.dedent(f'''\
            from django.urls import path
            from .views import home, list_items

            urlpatterns = [
                path('', home, name='home'),
                path('list/', list_items, name='list_items'),
            ]
        '''), encoding='utf-8')

print('Created simple Django apps for vazifa3, vazifa4, vazifa5')
