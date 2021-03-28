"""Test page loader."""
import tempfile

import requests_mock

from page_loader.page_loader import download, get_file_name

TEST_URL = 'https://ru.hexlet.io/courses'
GENERATED_FILENAME = 'ru-hexlet-io-courses.html'


def test_download():
    with tempfile.TemporaryDirectory() as temporary_directory:
        with requests_mock.Mocker() as mocker:
            mocker.get('http://test.com', text='testing_page')
            file_path = download('http://test.com', temporary_directory)
            with open(file_path, 'r') as file:  # noqa: WPS110
                page = file.read()
                assert page == 'testing_page'


def test_get_file_name():
    assert GENERATED_FILENAME == get_file_name(TEST_URL)
