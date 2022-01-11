"""Page loader."""

import logging.config  # noqa: WPS301

from page_loader import data_processing, naming
from page_loader.logger_config import configuring_dict

logging.config.dictConfig(configuring_dict)
logger = logging.getLogger('app_logger')


def download(page_url: str, output_path: str) -> str:

    soup = data_processing.get_soup(page_url)

    logger.info('soup done')

    path_to_file = data_processing.make_path(
        output_path,
        naming.get_file_name(page_url),
    )

    logger.info('path with file name done')

    path_to_resource_dir = data_processing.make_dir(page_url, output_path)

    logger.info('path and dir for downloadable resources done')

    print(f'Loading to {path_to_resource_dir}:\n')  # noqa: WPS421

    html_with_local_links = data_processing.change_local_links(
        page_url,
        soup,
        path_to_resource_dir,
    )

    logger.info('change links done')

    data_processing.save_page(path_to_file, html_with_local_links)

    logger.info('saving page with new local links done')

    return path_to_file
