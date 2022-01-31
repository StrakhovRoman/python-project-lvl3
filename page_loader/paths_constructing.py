"""Constructing paths and directories."""

import logging.config  # noqa: WPS301
import pathlib

from page_loader.logger_config import configuring_dict

logging.config.dictConfig(configuring_dict)
logger = logging.getLogger('app_logger')


def make_dir(output_path: str, path_component: str) -> str:
    path_to_directory = make_path(
        output_path,
        path_component,
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


def make_path_to_soup_link(path):
    parts = pathlib.Path(path).parts
    return pathlib.Path(parts[-2]) / parts[-1]
