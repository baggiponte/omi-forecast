"""Utility functions for OMI."""

from __future__ import annotations


def get_read_url(url: str) -> str:
    """Return a readable URL from a Google Drive share link."""
    base_url = "https://drive.google.com/uc?id="
    file_id = url.split("/")[-2]

    return base_url + file_id
