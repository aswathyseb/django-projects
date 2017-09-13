import django
from django.conf import settings
from django.template.loader import get_template
import json

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['.'],
    }
]
settings.configure(TEMPLATES=TEMPLATES)
django.setup()

template = get_template('template_make.html')
context = {'name': 'Aswathy Sebastian'}


def metadata_loader(fname):
    data = open(fname).read()
    data = json.loads(data)
    return data


metadata = metadata_loader("input.json")

html = template.render(metadata)

print(html)



