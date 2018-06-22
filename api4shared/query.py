from enum import Enum


class SortType(Enum):
    NAME = 'name'
    SIZE = 'size'
    DOWNLOADS = 'downloads'
    DOWNLOADS_MONTHLY = 'downloads_monthly'
    TIME = 'time'


class SortOrder(Enum):
    ASC = 'asc'
    DESC = 'desc'
