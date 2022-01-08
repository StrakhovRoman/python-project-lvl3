"""Naming downloadable resource."""

import os
import re
from urllib.parse import urlparse

NAME = '{0}{1}'


def get_name(page_url, link=False, directory=False):  # noqa: WPS210
    """Get a file or directory name from page URL.

    Returns a pair (name, extension) if you want to get the file name
    or just name if you want to get the name of the directory
    (directory=True)
    """
    domain_name = urlparse(page_url).netloc
    if link:
        root, extension = os.path.splitext(link)
        path_parts = urlparse(root).path
        extension = '.html' if extension == '' else extension
    else:
        path_parts = urlparse(page_url).path
        extension = '.html'
    name = NAME.format(domain_name, path_parts.rstrip('/'))
    if directory:
        return convert_name(name)
    return convert_name(name), extension


def convert_name(resource):
    return re.sub(r'\W', '-', resource)


def get_file_name(page_url, source_link=False):
    return NAME.format(*get_name(page_url, link=source_link))


def get_directory_name(page_url):
    return NAME.format(get_name(page_url, directory=True), '_files')
