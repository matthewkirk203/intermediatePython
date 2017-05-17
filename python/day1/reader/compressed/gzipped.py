import sys
import gzip

opener = gzip.open


def main():
    f = gzip.open(sys.argv[1], mode='wt')
    f.write(" ".join(sys.argv[2:]))


if __name__ == "__main__":
    main()