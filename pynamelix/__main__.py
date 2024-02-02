import argparse
import logging
from check_pypi_name import check_pypi_name
from pynamelix import __version__
from pynamelix.utils import get_names

logger = logging.getLogger(__name__)

def set_logger(verbose):
    levels = [logging.WARNING, logging.INFO, logging.DEBUG]
    level = levels[min(len(levels) - 1, verbose)]
    logging.basicConfig(level=level, format="%(asctime)s %(levelname)s %(message)s")

def main(argv=None):
    parser = argparse.ArgumentParser(prog='pynamelix')
    parser.add_argument('-V', '--version',
                            action='version',
                            version=__version__,
                            help="Show program version.")
    parser.add_argument('-v', '--verbose',
                            action='count',
                            default=0)
    parser.add_argument('-p', '--pypi',
                            action='store_true')
    parser.add_argument('-s', '--styles',
                            choices=['multiword', 'brandable', 'language', 'wordmix',
                                'spelling', 'dictionary', 'rhyme', 'person'],
                            default='brandable',
                            help="Select a preferred STYLE of your generated words.")
    parser.add_argument('-l', '--lengths',
                            choices=['short', 'medium', 'long'],
                            default='short',
                            help="Select a preferred LENGTH of your generated words.")
    parser.add_argument('-f', '--filename',
                            default='-',
                            help="Write API output to a file.")
    parser.add_argument('keywords',
                            nargs='+',
                            help="A word or words to base the word generator on. Multiple words should be separated by a space (' ').")

    args = parser.parse_args(argv)
    set_logger(args.verbose) # Log any errors

    '''
    # Original library program
    index = 1
    for name in get_names(args.keywords, args.styles, args.lengths):
        logger.debug('check %s', name)
        if (not args.pypi) or (args.pypi and not check_pypi_name(name, 'pypi.org')):
            print(index, name)
            index += 1
    '''

    if args.filename != '-': # Write in file
        # Use current directory location to store file
        f = open("{0}.txt".format(args.filename), 'w')
        index = 1
        for entry in get_names(args.keywords, args.styles, args.lengths):
            f.write("{} {}\n".format(index, entry)) # Write to file
            index += 1
        f.close()
    else:
        index = 1
        for entry in get_names(args.keywords, args.styles, args.lengths):
            print(index, entry)
            index += 1

if __name__ == '__main__':
    main()
