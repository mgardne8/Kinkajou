"""Core kinkajou functions
This module contains the core functions for the kinkajou library

Todo:
    Write Todo
"""

import os.path

import csv

from kinkajou.errors import CagingError
from kinkajou.objects import DataCage


def cage_csv(infile: str, has_header: bool = True, encoding: str = None) -> DataCage:
    """Cage a CSV file from a path

    Args:
        infile (str): relative path to csv file to cage
        has_header (bool, optional): Generates header if one doesn't exist. Defaults to True.
        encoding (str): encoding type of csv file. Defaults to None (Attempts to automatically detect)

    Raises:
        CagingError: Was unable to Cage the data - it continues to run free.

    Returns:
        DataCage: Cage containing data from the provided CSV file

    TODO: Parameterize csv options
    """
    try:
        infile = os.path.abspath(os.path.join(os.path.dirname(__file__), infile))
        with open(infile, mode="r", encoding=encoding) as csv_file:
            csvdata = csv.reader(csv_file, delimiter=",")
            data = list(csvdata)

        if has_header:
            header = data.pop(0)
        else:
            header = [f"Column_{x}" for x in range(len(data[0]))]

    except Exception as exc:
        raise CagingError from exc

    res = DataCage(header, data)

    return res


def uncage_csv(cage: DataCage, outfile: str) -> None:
    """Release a csv file from it's cage to return to the wild in the file system

    Args:
        cage (DataCage): cage to open
        outfile (str): relative path to relase the cage into

    TODO: write DataCage to CSV export function
    """
    raise NotImplementedError
