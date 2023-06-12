# First Party Library
from minigrep_py import ArgumentParser


def test_parser_new() -> None:
    parser = ArgumentParser()
    assert parser is not None and isinstance(parser, ArgumentParser)


def test_parser_parse_args() -> None:
    parser = ArgumentParser()
    args = parser.parse_args(["foo"])
    assert args is not None and isinstance(args, ArgumentParser.Namespace)
    assert args.patterns == ["foo"]
