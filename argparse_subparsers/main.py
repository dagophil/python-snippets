import argparse


def main(args):
    print("Successfully parsed arguments:")
    print(args)


parser = argparse.ArgumentParser(description="Collection of workflows.")
subparsers = parser.add_subparsers(dest="workflow", help="the executed workflow")
subparsers.required = True

w0_parser = subparsers.add_parser("w0", description="First workflow.")
w0_parser.add_argument("--w0arg1", type=str, required=True, help="some required w0 argument")
w0_parser.add_argument("--w0arg2", type=int, help="some optional w0 argument")

w1_parser = subparsers.add_parser("w1", description="Second workflow.")
w1_parser.add_argument("--w1arg1", type=str, required=True, help="some required w1 argument")
w1_parser.add_argument("--w1arg2", type=int, help="some optional w1 argument")


if __name__ == "__main__":
    main(parser.parse_args())
