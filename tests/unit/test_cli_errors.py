import pytest
from src.cli.main import SafeArgumentParser, ArgumentParseError


def test_safe_argument_parser_raises_on_error():
    parser = SafeArgumentParser()
    parser.add_argument("--test", required=True)

    with pytest.raises(ArgumentParseError):
        parser.parse_args([])
