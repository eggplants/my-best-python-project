"""A module for CLI implementation."""

from __future__ import annotations

import shutil
import sys
import textwrap
from argparse import (
    ArgumentDefaultsHelpFormatter,
    ArgumentParser,
    ArgumentTypeError,
    Namespace,
    RawDescriptionHelpFormatter,
)
from pathlib import Path

from . import __version__


class MBBPHelpFormatter(
    ArgumentDefaultsHelpFormatter,
    RawDescriptionHelpFormatter,
):
    """Custom formatter class."""


def check_out(s: str | None) -> Path | None:
    """Check if output path is valid directory or not.

    Args:
        s (str | None): given argument.

    Raises:
        argparse.ArgumentTypeError: raise if it is invalid path.

    Returns:
        Path | None: valid path or None.
    """
    if s is None:
        return None
    if Path(s).is_dir():
        msg = f"File '{s}' is a dir."
        raise ArgumentTypeError(msg)
    return Path(s)


def parse_args(test_args: list[str] | None = None) -> Namespace:
    """Parse given commandline arguments.

    Returns:
        Namespace: argparse.Namespace
    """
    usage = textwrap.dedent(
        """
    note:
        This package and tool is a sample.
    """,
    )

    parser = ArgumentParser(
        prog="mbpp",
        description="This command prints package's version.",
        formatter_class=(
            lambda prog: MBBPHelpFormatter(
                prog,
                width=shutil.get_terminal_size(fallback=(120, 50)).columns,
                max_help_position=40,
            )
        ),
        epilog=usage,
    )
    parser.add_argument(
        "-o",
        "--output",
        type=check_out,
        help="output to file",
        metavar="PATH",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="overwrite when using `-o`",
    )
    parser.add_argument("-q", "--quiet", action="store_true", help="quiet mode")
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    if test_args is None:
        return parser.parse_args()

    return parser.parse_args(test_args)


def main(test_args: list[str] | None = None) -> None:
    """CLI main."""
    args = parse_args(test_args)
    quiet: bool = args.quiet
    overwrite: bool = args.overwrite
    output_path: Path | None = args.output

    contents: list[str] = []
    if not quiet:
        contents.append("This package's version is:")
    contents.append(__version__)
    content = " ".join(contents)

    if output_path is None:
        print(content)  # noqa: T201
    elif not output_path.is_file() or overwrite:
        print(content, file=output_path.open(mode="w"))
        if not quiet:
            print(f"Output: File '{output_path}'")  # noqa: T201
    else:
        print(  # noqa: T201
            f"Error: File '{output_path}' exists. To overwrite, use `--overwrite`.",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
