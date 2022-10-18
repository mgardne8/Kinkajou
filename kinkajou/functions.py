"""Core kinkajou functions
This module contains the core functions for the kinkajou library

Todo:
    Write Todo
"""

import os.path

import csv

from kinkajou.errors import CagingError
from kinkajou.objects import DataCage


def cage_csv(
    infile: str, has_header: bool = True, encoding: str = None, **fmtparams
) -> DataCage:
    """Cage a CSV file from a path

    Args:
        infile (str): relative path to csv file to cage
        has_header (bool, optional): Generate header if one doesn't exist. Defaults to True.
        **fmtparams: any Dialect and Formatting paramaters from the CSV module -
                    `https://docs.python.org/3/library/csv.html#csv-fmt-params` for more information

    Raises:
        CagingError: Was unable to Cage the data - it continues to run free.

    Returns:
        DataCage: Cage containing data from the provided CSV file
    """

    try:
        infile = os.path.abspath(os.path.join(os.path.dirname(__file__), infile))
        with open(infile, mode="r", encoding=encoding) as csvfile:
            csvdata = csv.reader(csvfile=csvfile, **fmtparams)
            # Todo: Stuff with csvdata
    except Exception as exc:
        raise CagingError from exc

    raise NotImplementedError


def uncage_csv(cage: DataCage, outfile: str) -> None:
    """Release a csv file from it's cage to return to the wild in the file system

    Args:
        cage (DataCage): cage to open
        outfile (str): relative path to relase the cage into

    Raises:
        NotImplementedError: _description_
    """
    raise NotImplementedError
