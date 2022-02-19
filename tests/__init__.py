import os

# Make sure our dependencies can find the environment variables they're expecting,
# mostly means we need everything to be on the same page about where the settings
# module is
settings_module_env = os.getenv('KDR_SETTINGS_MODULE')
if not settings_module_env:
    raise RuntimeError('Missing environment variable "KDR_SETTINGS_MODULE". '
        'Did you export it before importing kivy_django_restful. ')
else:
    os.environ.setdefault('PICKLE_STORAGE_SETTINGS', settings_module_env)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module_env)