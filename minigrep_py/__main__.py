from . import ArgumentParser


def main() -> None:
    parser = ArgumentParser()
    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
    main()
