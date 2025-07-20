from typing import Union
from pathlib import Path
import sqlite3


def connect(db: Union[Path, str]) -> sqlite3.Connection:
    """ Create a database connection with appropriate project settings. """
    conn = sqlite3.connect(str(db))
    conn.cursor().execute("PRAGMA foreign_keys = ON")
    conn.row_factory = sqlite3.Row  # return rows as dictionaries
    return conn
