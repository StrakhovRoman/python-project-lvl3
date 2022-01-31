"""Test fixtures."""
import os

import pytest

path_to_fixtures = os.path.join('tests', 'fixtures', 'resources')


@pytest.fixture
def test_html():
    with open(os.path.join(
        path_to_fixtures,
        'test_page.html',
    )) as fixture:
        fixture_data = fixture.read()
    return fixture_data


@pytest.fixture
def expect_test_html():
    with open(os.path.join(
        path_to_fixtures,
        'expect_test_page.html',
    )) as fixture:
        fixture_data = fixture.read()
    return fixture_data
