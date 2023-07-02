"""Dataloading utilities."""

from __future__ import annotations

from typing import Literal

import pandas as pd

from omi.types import ColumnSpec
from omi.utils import get_read_url

DATA_SOURCES = {
    "values": {
        "2022": {
            "1": "https://drive.google.com/file/d/17UEpe0z_6f0YMVOCZ4UQYL5PxPWlCGBT/view?usp=drive_link",
            "2": "https://drive.google.com/file/d/1EXxMkNhoQUUryrQrIihhbW6iJKP2kKR9/view?usp=drive_link",
        }
    },
    "zones": {
        "2022": {
            "1": "https://drive.google.com/file/d/1CK7-C3TNb5kwuBs7w50meDsdHKWAssDS/view?usp=drive_link",
            "2": "https://drive.google.com/file/d/1bNodc6L_fEoGqAixaQ3UqSBi7qdwaMfK/view?usp=drive_link",
        }
    },
}


class ValuesDataLoader:
    """Loads OMI values data."""

    URLS: dict[str, dict[str, str]] = DATA_SOURCES["values"]

    MODEL = [
        ColumnSpec("Area_territoriale", "area_territoriale", "category"),
        ColumnSpec("Regione", "regione", "category"),
        ColumnSpec("Prov", "provincia", "category"),
        ColumnSpec("Comune_ISTAT", "comune_codice_istat", "string"),
        ColumnSpec("Comune_cat", "comune_codice_catastale", "string"),
        ColumnSpec("Comune_amm", "comune_codice_nazionale", "string"),
        ColumnSpec("Comune_descrizione", "comune_denominazione", "string"),
        ColumnSpec("Fascia", "fascia", "category"),
        ColumnSpec("Zona", "zona", "category"),
        ColumnSpec("LinkZona", "linkzona", "string"),
        ColumnSpec("Cod_Tip", "tipologia_codice", "category"),
        ColumnSpec("Descr_Tipologia", "tipologia_descrizione", "string"),
        ColumnSpec("Stato", "condizione", "category"),
        ColumnSpec("Compr_min", "prezzo_min", "float32"),
        ColumnSpec("Compr_max", "prezzo_max", "float32"),
        ColumnSpec("Loc_min", "affitto_min", "string"),
        ColumnSpec("Loc_max", "affitto_max", "string"),
        ColumnSpec("Sup_NL_loc", "affitto_superficie", "category"),
    ]

    def __init__(
        self,
        *,
        year: Literal["2022", 2022] = 2022,
    ) -> None:
        self.year = str(year)

    def _load_raw(
        self,
        semester: Literal["1", "2", 1, 2],
    ) -> pd.DataFrame:
        """Load raw data from the URL."""
        url: str = get_read_url(self.URLS[self.year][str(semester)])

        return pd.read_csv(
            url,
            sep=";",
            skiprows=1,
            skipinitialspace=True,
            usecols=range(21),
        )

    def load(
        self,
        semester: Literal["1", "2", 1, 2],
    ) -> pd.DataFrame:
        """Load data from the URL."""
        rawdata: pd.DataFrame = self._load_raw(semester)
        cols_to_drop = list(
            set(rawdata.columns) - {spec.oldname for spec in self.MODEL}
        )

        return (
            rawdata.rename(columns={spec.oldname: spec.colname for spec in self.MODEL})
            .drop(columns=cols_to_drop)
            .astype({spec.colname: spec.dtype for spec in self.MODEL})
            .assign(
                affitto_min=lambda df: df.affitto_min.str.replace(",", ".").astype(
                    "float32"
                ),
                affitto_max=lambda df: df.affitto_max.str.replace(",", ".").astype(
                    "float32"
                ),
            )
        )
