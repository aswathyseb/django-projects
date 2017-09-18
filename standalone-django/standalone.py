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


def read_data2json(fname):
    '''
    reads a config file in the form
    data1 = val1
    data2 = val2,val3
    and returns a json file.
    :param fname: input file in text format
    :return: writes a json file
    '''
    data = dict()
    with open(fname) as fh:
        for stream in fh:
            param = stream.split("=")
            vals = param[1].strip().split(",")
            data[param[0].strip()] = vals if len(vals) >1 else param[1].strip()
    with open('input.json', 'w') as outfile:
        json.dump(data, outfile, indent=4, separators=(',', ': '))
    return

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
    read_data2json("input.txt")
    metadata = metadata_loader("input.json")
    template = get_template('igv.html')
    html = template.render(metadata)

    # the above two lines can be replaced bt render_to_string method as below.
    #html = rendender_to_string('template_make.html',metadata)

    print(html)



