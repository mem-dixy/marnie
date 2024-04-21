"""A package for determining appropriate platform-specific dirs."""

import pathlib

from celestine.package import Abstract
from celestine.typed import P


class Package(Abstract):
    """"""

    @property
    def directory(self) -> P:
        """"""
        directory = self.package.user_data_dir(
            appname="celestine",
            appauthor=False,
            version=None,
            roaming=False,
            ensure_exists=True,
        )
        path = pathlib.Path(directory)
        return path
