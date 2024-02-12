from pathlib import Path

import pytest

from my_best_python_project import __version__
from my_best_python_project.main import main


def test_version() -> None:
    assert __version__ is not None


def test_cli_no_args(capfd: pytest.CaptureFixture[str]) -> None:
    main(test_args=[])
    captured = capfd.readouterr()
    assert captured.out == f"This package's version is: {__version__}\n"
    assert not captured.err


def test_cli_write_file(tmp_path: Path, capfd: pytest.CaptureFixture[str]) -> None:
    path = tmp_path / "hoge"
    main(test_args=["-o", str(path)])
    captured = capfd.readouterr()
    assert captured.out == f"Output: File '{path}'\n"
    assert not captured.err

    with pytest.raises(SystemExit) as e:
        main(test_args=["-o", str(path)])
    assert e.value.args[0] == 1
    captured = capfd.readouterr()
    assert not captured.out
    assert captured.err == f"Error: File '{path}' exists. To overwrite, use `--overwrite`.\n"

    main(test_args=["-o", str(path), "--overwrite"])
    captured = capfd.readouterr()
    assert captured.out == f"Output: File '{path}'\n"
    assert not captured.err
    assert path.open("r").read() == f"This package's version is: {__version__}\n"


def test_cli_empty_output_path(capfd: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as e:
        main(test_args=["-o"])
    assert e.value.args[0] == 2  # noqa: PLR2004
    captured = capfd.readouterr()
    assert not captured.out
    assert "expected one argument" in captured.err


def test_cli_output_path_is_dir(tmp_path: Path, capfd: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as e:
        main(test_args=["-o", str(tmp_path)])
    assert e.value.args[0] == 2  # noqa: PLR2004
    captured = capfd.readouterr()
    assert not captured.out
    assert f"'{tmp_path}' is a dir.\n" in captured.err
