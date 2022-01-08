"""Test page loader."""
import tempfile

import pytest
import requests_mock

from page_loader.loader import download
from page_loader.naming import get_directory_name, get_file_name
from page_loader.url_processing import get_url_from_local_link

TEST_URL = 'https://ru.hexlet.io/courses'
FILE_NAME = 'ru-hexlet-io-courses.html'
DIRECTORY_NAME = 'ru-hexlet-io-courses_files'

'''
def test_download():
    with tempfile.TemporaryDirectory() as temporary_directory:
        with requests_mock.Mocker() as mocker:
            mocker.get('http://test.com', text='testing_page')
            file_path = download('http://test.com', temporary_directory)
            with open(file_path, 'r') as file:  # noqa: WPS110
                page = file.read()
                assert page == 'testing_page'
'''


def test_get_file_name():
    assert FILE_NAME == get_file_name(TEST_URL)


def test_get_directory_name():
    assert DIRECTORY_NAME == get_directory_name(TEST_URL)


@pytest.mark.parametrize(
    'link, correct_value',
    [
        (
            '/assets/application.css',
            'https://ru.hexlet.io/assets/application.css',
        ),
        (
            '/courses',
            'https://ru.hexlet.io/courses',
        ),
        (
            '/assets/professions/nodejs.png',
            'https://ru.hexlet.io/assets/professions/nodejs.png',
        ),
    ],
)
def test_get_url_from_local_link(link, correct_value):
    assert get_url_from_local_link(TEST_URL, link) == correct_value
