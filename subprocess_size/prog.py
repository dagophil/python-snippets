import sys
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("infiles", type=str, nargs="*")
    args = parser.parse_args()

    print "prog.py got", len(args.infiles), "numbers"

    return 0


if __name__ == "__main__":
    status = main()
    sys.exit(status)
