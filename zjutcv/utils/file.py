# Copyright (c) ZJUTCV. All rights reserved.
import os
from pathlib import Path, PosixPath, WindowsPath


class ZPath(type(Path()), Path):
    """This class used to index 'Path' like a list.

    There maybe something wrong with directly inheriting from Path due to
    __new__ in Path. Thanks to `Alex Deft` for his wonderful solution.
    https://stackoverflow.com/a/62812595
    """

    def __getitem__(self, idx):
        """Index path component like a list.

        Path: "DeskTop / dir1 / User / Game / CSGO.exe"
                  0        1     2      3       4

        Args:
            idx (int): The index of component.

        Returns:
            Component string.
        """
        return self.parts[idx]
