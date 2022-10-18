"""Error objects for Kinkajou
"""


class KinkajouError(Exception):
    """Base class for Kinkajou exceptions."""


class CagingError(KinkajouError):
    """This exception is raised when an uncageable object is passed to the cage() method."""

    def __init__(self) -> None:
        self.message = "Supplied Object could not be caged"
        super().__init__(self.message)


class ReleasingError(KinkajouError):
    """This exception is raised when a caged objects refuses to return to the wild"""

    def __init__(self) -> None:
        self.message = "Supplied Object could not be released"
        super().__init__(self.message)
