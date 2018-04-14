import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description='Splash headless browser adapter for Requests.'
    )

    return parser.parse_args()


def main():
    args = parse_args()


if __name__ == "__main__":
    main()
