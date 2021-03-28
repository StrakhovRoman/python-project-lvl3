"""CLI argument parser."""
import argparse
import os

DEFAULT_OUTPUT = os.getcwd()


def get_parser():
    parser = argparse.ArgumentParser(description='Page loader')
    parser.add_argument(
        '-o',
        '--output',
        type=str,
        help='Download path',
        default=DEFAULT_OUTPUT,
    )
    parser.add_argument('url', type=str, help='URL reference to web page')
    return parser
