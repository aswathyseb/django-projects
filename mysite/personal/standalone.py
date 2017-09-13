from mysite.settings import defaults
from django.template import Template, Context
from django.conf import settings
settings.configure(default_settings=defaults)
myTemplate = Template('My name is {{ my_name }}.')
myContext = Context({'my_name': 'Aswathy Sebastian'})
