"""Principal module."""
from pathlib import Path
from tomli import load

pyproject = Path(__file__).parents[4] / 'pyproject.toml'
versionfile = Path(__file__).parent / 'version.txt'

with pyproject.open("rb") as f:
    versionfile.write_text(
        f"{load(f)['tool']['poetry']['version']}\n"
    )


__version__ = versionfile.read_text().strip()
