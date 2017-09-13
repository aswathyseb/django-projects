import django
from django.conf import settings
from django.template.loader import get_template
import json
from django.template.loader import render_to_string


def set_env():
    '''
    Specify template engine and template directory.
    Pass the settings variable to configure.
    '''

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': ['./templates'],
        }
    ]
    settings.configure(TEMPLATES=TEMPLATES)


def metadata_loader(fname):
    '''
    reads json file and returns the data
    :param fname:
    :return: data dictionary.
    '''

    data = open(fname).read()
    data = json.loads(data)
    return data


if __name__ == '__main__':
    set_env()
    django.setup()
    metadata = metadata_loader("input.json")
    template = get_template('igv.html')
    html = template.render(metadata)

    # the above two lines can be replaced bt render_to_string method as below.
    #html = rendender_to_string('template_make.html',metadata)

    print(html)

