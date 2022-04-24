from __future__ import annotations

import argparse
import os
import shutil
import sys
import textwrap
from typing import Optional, cast

from . import __version__


class MBBPHelpFormatter(
    argparse.ArgumentDefaultsHelpFormatter,
    argparse.RawDescriptionHelpFormatter,
):
    pass


def check_out(s: str | None) -> str | None:
    if s is None:
        return None
    elif os.path.isdir(s):
        raise argparse.ArgumentTypeError(f"{repr(s)} is a dir.")
    else:
        return s


def parse_args() -> argparse.Namespace:
    usage = textwrap.dedent(
        """
    note:
        This package and tool is a sample.
    """,
    )

    parser = argparse.ArgumentParser(
        prog="mbpp",
        description="This command prints package's version.",
        formatter_class=(
            lambda prog: MBBPHelpFormatter(
                prog,
                **{
                    "width": shutil.get_terminal_size(fallback=(120, 50)).columns,
                    "max_help_position": 40,
                },
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
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    quiet = cast(bool, args.quiet)
    overwrite = cast(bool, args.overwrite)
    output_path = cast(Optional[str], args.output)

    contents = []
    if not quiet:
        contents.append("This package's version is:")
    contents.append(__version__)
    content = " ".join(contents)

    if output_path is None:
        print(content)
    elif not os.path.isfile(output_path) or overwrite:
        print(content, file=open(output_path, "w"))
        if not quiet:
            print(f"Output: {repr(output_path)}", file=sys.stderr)
    else:
        print(
            f"Error: File {repr(output_path)} exists. "
            "To overwrite, use `--overwrite`.",
            file=sys.stderr,
        )
        exit(1)


if __name__ == "__main__":
    main()
