"""Page loader."""

import os
import re

from requests import request


def download(url, directory):
    response = request('GET', url).text
    file_path = get_file_path(url, directory)
    with open(file_path, 'w', encoding='utf-8') as file:  # noqa: WPS110
        file.write(response)
    return file_path


def get_file_name(url):
    url_without_scheme = re.sub(r'^(https|http):\/\/', '', url)
    file_name = re.sub(r'\.|\/', '-', url_without_scheme)
    return '{0}{1}'.format(file_name, '.html')


def get_file_path(url, directory):
    file_name = get_file_name(url)
    return os.path.join(directory, file_name)
