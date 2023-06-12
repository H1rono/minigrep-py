# Standard Library
import re
from dataclasses import dataclass
from typing import Self, TextIO


@dataclass
class SearchConfig:
    patterns: list[re.Pattern]
    input: str

    @classmethod
    def new(cls, patterns: list[str], input: TextIO) -> Self:
        pats = [re.compile(pat) for pat in patterns]
        return cls(pats, input.read())


class Search:
    __slots__ = ("__config",)

    Config = SearchConfig

    def __init__(self, config: SearchConfig) -> None:
        self.__config = config

    def run(self) -> list[str]:
        return [
            line
            for line in self.__config.input.splitlines()
            if any(pat.search(line) for pat in self.__config.patterns)
        ]

    @classmethod
    def new(cls, patterns: list[str], input: TextIO) -> Self:
        return cls(cls.Config.new(patterns, input))
