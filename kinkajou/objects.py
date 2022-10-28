""" This module contains the core objects for the kinkajou library.

Currently this consists of only the abstract KinkajouClass class and the main DataCage class.
"""

# TODO: Objects Module documentation

from __future__ import annotations
from typing import Callable, Iterable


class KinkajouClass:
    """Base Abstract Class for other kinkajou Classes"""


class DataCage(KinkajouClass):
    """DataCage object"""

    # TODO: DataCage class documentation

    def __init__(self: DataCage, header: list, data: list) -> None:
        self._header = header
        self._data = data

    def __str__(self: DataCage) -> str:
        raise NotImplementedError
        # TODO: Implement __str__ for DataCage

    def __repr__(self: DataCage) -> str:
        raise NotImplementedError
        # TODO: Implement __repr__ for DataCage

    def __len__(self: DataCage) -> int:
        return len(self._data)

    @property
    def header(self: DataCage) -> Iterable:
        """Yields Iterable object of headers"""
        return (x for x in self._header)

    @header.setter
    def header(self: DataCage, newheader: list) -> None:
        """
        Todo: Write this function so that
        if: len(self._header) = len(newheader) - then set them
        if: len(self._header) < len(newheader) - then add empty values to each row
        if: len(self._header) > len(newheader) -
            if right column(s) are empty - remove them
            else raise error (can-not delete non-empty columns through setting headers)
        """
        # TODO: Header.setter logic (see docstring)
        self._header = newheader

    def column(self: DataCage, column: int | str = 0) -> Iterable:
        """Yields iterable object containing all values from a column

        Args:
            column (int | str): either index or header of column to fetch

        Yields:
            Iterable: iterable generator of values from column
        """
        if isinstance(column, str):
            column = self._header.index(column)
        # TODO: Add exception handling when column header string is not valid (column)

        return (row[column] for row in self._data)

    def row(self: DataCage, row: int) -> Iterable:
        """Yields iterable object containing all values from a row

        Args:
            row (int): index of row to fetch

        Yields:
            Iterable: iterable generator of values from row
        """
        return (data for data in self._data[row])

    def modify_column(self: DataCage, column: int | str, operation: Callable) -> None:
        """Modify a column in the datacage through provided Callable

        Args:
            Column (int | str): either index or header of column to modify
            operation (Callable): Callable to map to column
        """
        # TODO: add example code to modify_column function

        if isinstance(column, str):
            column = self._header.index(column)
        # TODO: Add exception handling when column header string is not valid (modify_column)

        # get an interable of our column values
        original_data = self.column(column)

        # map our existing values with the provided callable
        working_data = map(operation, original_data)

        # replace our old values with our new modified values
        for index, value in enumerate(working_data):
            self._data[index][column] = value

    def filter(self: DataCage, opeartion: Callable) -> Iterable:
        """return rows that match checks set in provided Callable

        Args:
            opeartion (Callable): Callable to run against each row

        Yields:
            Iterable: all rows that return True for callable
        """
        return (row for row in self._data if opeartion(row))

    def head(self: DataCage, rows: int = 5) -> None:
        """Print header and first <rows> from datacage

        Args:
            rows (int, optional): Number of Rows(lists) to print. Defaults to 5.
        """
        print(self._header)
        for row in self._data[:rows]:
            print(row)

    def tail(self: DataCage, rows: int = 5) -> None:
        """Print header and last <rows> from datacage

        Args:
            rows (int, optional): Number of Rows(lists) to print. Defaults to 5.
        """
        print(self._header)
        for row in self._data[-rows:]:
            print(row)
