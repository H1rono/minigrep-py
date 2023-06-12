# Standard Library
import io
import textwrap

# First Party Library
from minigrep_py import Search


def test_search_new() -> None:
    search = Search.new(["foo"], io.StringIO("bar"))
    assert search is not None and isinstance(search, Search)


def test_search_run() -> None:
    patterns = ["foo", "^bar", "baz$"]
    input_s = textwrap.dedent(
        """\
        some foo thing
        bar only matches
        eol: baz
        baz bar no match
    """
    )
    search = Search.new(patterns, io.StringIO(input_s))
    assert search.run() == ["some foo thing", "bar only matches", "eol: baz"]
