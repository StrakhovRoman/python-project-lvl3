"""Page loader."""

import logging.config  # noqa: WPS301

# isort: off
from page_loader import (
    data_processing,
    naming,
    paths_constructing,
    url_processing,
)
from page_loader.logger_config import configuring_dict

logging.config.dictConfig(configuring_dict)
logger = logging.getLogger('app_logger')


def download(page_url: str, output_path: str) -> str:

    soup = url_processing.get_soup(page_url)

    logger.info('soup done')

    path_to_file = paths_constructing.make_path(
        output_path,
        naming.get_file_name(page_url),
    )

    logger.info('path with file name done')

    resource_dir_name = naming.get_directory_name(page_url)

    logger.info('directory name for downloadable resources done')

    path_to_resource_dir = paths_constructing.make_dir(
        output_path,
        resource_dir_name,
    )

    logger.info('path to directory for downloadable resources done')

    print(  # noqa: WPS421
        'Loading page ...\n',
    )

    html_with_local_links = data_processing.change_local_links(
        page_url,
        soup,
        path_to_resource_dir,
    )

    logger.info('change links done')

    data_processing.save_page(path_to_file, html_with_local_links)

    logger.info('saving page with new local links done')

    return path_to_file
