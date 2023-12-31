# Standard Library
import argparse
from dataclasses import dataclass
from typing import Optional


@dataclass
class Args:
    patterns: Optional[list[str]] = None


class ArgumentParser:
    __slots__ = ("__parser",)

    Namespace = Args

    def __init__(self) -> None:
        self.__parser = argparse.ArgumentParser(
            description="minimal grep implementation in python",
            epilog="This takes pattern from arguments and file from stdin.",
        )
        self.__parser.add_argument(
            "patterns",
            nargs="+",
            help="pattern(s) of regular expression to search for",
        )

    def parse_args(self, args: Optional[list[str]] = None) -> Args:
        return self.__parser.parse_args(args, namespace=Args())
