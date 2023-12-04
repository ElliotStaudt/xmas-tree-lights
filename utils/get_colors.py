import json
import argparse
import os

from loguru import logger

parser = argparse.ArgumentParser(
    prog="Stripe CSV Reader",
    description="Reads Stripe CSV and exports useful info.",
    epilog="Thanks for trying!",
)

parser.add_argument("-f", "--filename", type=str, help="file path to .txt")


def main(args):
    if not args.filename.endswith(".txt"):
        raise RuntimeError("Program expects .txt as input.")
    if not os.path.exists(args.filename):
        raise FileNotFoundError(f"No such file or directory: {args.filename}")

    colors = {}
    with open(args.filename) as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            color = lines[i].strip()
            rgb = lines[i + 1].strip()
            rgb = rgb[1:-1]
            rgbs = rgb.split(",")
            colors[color] = [int(x) for x in rgbs]

    with open("colors.json", "w") as outfile:
        json.dump(colors, outfile)


if __name__ == "__main__":
    # parse args
    args = parser.parse_args()
    try:
        main(args)
    except Exception as e:
        logger.error(type(e))
        logger.error(e.args)
        logger.error(e)
