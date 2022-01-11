"""Data processing."""

import logging.config  # noqa: WPS301
import pathlib

from bs4 import BeautifulSoup
from progress.bar import Bar

from page_loader import naming, url_processing
from page_loader.logger_config import configuring_dict

logging.config.dictConfig(configuring_dict)
logger = logging.getLogger('app_logger')

resources_tags = {'link', 'script', 'img'}
required_attributes = {'src', 'href'}


def change_local_links(  # noqa: WPS210, WPS213, WPS231
    page_url,
    soup,
    path_to_resource_dir,
):
    logger.info('start link search loop...')

    tags = soup.find_all(resources_tags)
    for tag in tags:
        attr_and_value = get_link(tag.attrs, required_attributes)
        if attr_and_value:
            attr, link = attr_and_value
            if url_processing.is_local_resource(page_url, link):

                logger.debug(f'resource tag: {tag}')
                logger.debug(
                    f'required attribute {attr} and its value: {link}',
                )

                if link.startswith('data:'):
                    continue
                resource_url = url_processing.get_url_from_local_link(
                    page_url,
                    link,
                )

                logger.debug(f'resource URL done: {resource_url}')

                resource_file_name = naming.get_file_name(
                    page_url,
                    resource_url,
                )

                logger.debug(f'resource file name done: {resource_file_name}')

                resource_path = make_path(
                    path_to_resource_dir,
                    resource_file_name,
                )

                logger.debug(f'resource path done: {resource_path}')

                resource_content = url_processing.get_response(
                    resource_url,
                    content_type='content',
                )

                logger.debug(f'resource content done: {resource_file_name}')

                save_content(
                    resource_path, resource_file_name, resource_content,
                )

                logger.debug('saving resource in file done')

                tag[attr] = make_path(path_to_resource_dir, resource_file_name)

                logger.debug(
                    f'local link done: {tag[attr]}',
                )
    return soup.prettify(formatter='html5')


def get_soup(page_url):
    html = url_processing.get_response(page_url)
    return BeautifulSoup(html, 'html.parser')


def get_link(tag_attrs: dict, required_attrs: set):
    for attr, value in tag_attrs.items():
        if attr in required_attrs:
            return attr, value


def save_content(path_to_file, resource_file_name, resource_content):

    bar = Bar(f'{resource_file_name}', suffix='%(percent).1d%%', color='cyan')

    try:
        with open(path_to_file, 'wb') as file:
            for chunk in resource_content:
                file.write(chunk)
                file.flush()
                bar.next()  # noqa: B305
            bar.finish()

    except OSError as error:
        logger.exception(error)
        raise OSError()


def save_page(path_to_file, resource_content):
    try:
        with open(path_to_file, 'w') as file:
            file.write(resource_content)
    except OSError as error:
        logger.exception(error)
        raise OSError()


def make_dir(page_url: str, output_path: str) -> str:
    path_to_directory = make_path(
        output_path,
        naming.get_directory_name(page_url),
    )

    try:
        pathlib.Path(path_to_directory).mkdir(exist_ok=True)

    except OSError as error:
        logger.exception(error)
        raise RuntimeError(
            f"Unable to create directory '{path_to_directory}'",
        ) from error
    return path_to_directory


def make_path(path: str, path_component: str) -> str:
    if pathlib.Path(path).exists():
        return pathlib.Path(f'{path}/{path_component}')
    raise RuntimeError(
        f"The path or folder '{path}' does not exist!",
    )
