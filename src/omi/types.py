"""Datatypes for OMI."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from pandas import DataFrame


@dataclass
class ColumnSpec:
    """Specification for a column model in the OMI dataset."""

    oldname: str
    colname: str
    dtype: str


class DataLoader(Protocol):
    """Protocol for data loaders."""

    URL: str
    MODEL: list[ColumnSpec]

    def _load_raw(self) -> DataFrame:
        """Load raw data from the URL."""
        ...

    def load(self) -> DataFrame:
        """Load processed data from the URL."""
        ...
