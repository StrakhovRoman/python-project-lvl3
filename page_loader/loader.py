"""Page loader."""

import logging.config  # noqa: WPS301

from page_loader import data_processing, naming
from page_loader.logger_config import logger_config

logging.config.dictConfig(logger_config)
logger = logging.getLogger('app_logger')


def download(page_url: str, output_path: str) -> str:

    logger.info('make soup')

    soup = data_processing.get_soup(page_url)

    logger.info('make path with file name')

    path_to_file = data_processing.make_path(
        output_path,
        naming.get_file_name(page_url),
    )

    logger.info('make path and dir for resource')

    path_to_resource_dir = data_processing.make_dir(page_url, output_path)

    logger.info('changing links')

    print(f'Loading to {path_to_resource_dir}:\n')  # noqa: WPS421

    html_with_local_links = data_processing.change_local_links(
        page_url,
        soup,
        path_to_resource_dir,
    )

    logger.info('saving page with new local links')

    data_processing.save_page(path_to_file, html_with_local_links)
    return path_to_file
