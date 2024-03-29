#!/usr/bin/env python

"""Page loader script."""


from page_loader.cli_argparser import get_parser
from page_loader.loader import download


def main():
    args = get_parser().parse_args()
    try:
        page = download(args.url, args.output)
    except Exception as error:
        print(error)

    print()
    print('Page is completely loaded into:')
    print(page)


if __name__ == '__main__':
    main()
