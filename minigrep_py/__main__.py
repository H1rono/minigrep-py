# Standard Library
import sys

# Local Library
from . import ArgumentParser, Search


def main() -> None:
    parser = ArgumentParser()
    args = parser.parse_args()
    patterns = args.patterns or []
    search = Search.new(patterns, sys.stdin)
    result = search.run()
    print("\n".join(result))


if __name__ == "__main__":
    main()
