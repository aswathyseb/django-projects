import django
from django.template import Template, Context
from django.conf import settings


TEMPLATES =[
    {
        'BACKEND':'django.template.backends.django.DjangoTemplates'
    }
]

settings.configure(TEMPLATES=TEMPLATES)
django.setup()
myTemplate = Template('My name is {{ my_name }}.')

myContext = Context({'my_name': 'Aswathy Sebastian'})
myTemplate.render(myContext)
