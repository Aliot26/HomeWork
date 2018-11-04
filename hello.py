import sys
import argparse


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', '-n', default="world")
    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

print("Hello, {}!".format(namespace.name))
