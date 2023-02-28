from typing import Iterator, Iterable, Union
import re


class RequestHandler:
    @staticmethod
    def filter(iterable: Iterator, value: str) -> Iterable:
        if not isinstance(value, str):
            raise TypeError
        return filter(lambda line: value in line, iterable)

    @staticmethod
    def sort(iterable: Iterator, order: str = "asc") -> list:
        if not order in ["asc", "desc"]:
            raise ValueError
        if order == "desc":
            return sorted(iterable, reverse=True)
        return sorted(iterable)

    @staticmethod
    def map(iterable: Iterator, column: Union[str, int]) -> Iterable:
        if not str(column).isdigit():
            raise TypeError
        return map(lambda line: line.split(" ")[int(column)] + "\n", iterable)

    @staticmethod
    def limit(iterable: Iterator, number: Union[str, int]) -> list:
        if not str(number).isdigit():
            raise TypeError
        return list(iterable)[:int(number)]

    @staticmethod
    def unique(iterable: Iterator, value="") -> set:
        return set(iterable)

    @staticmethod
    def regexp(iterable: Iterator, value: str) -> Iterable:
        regexp = re.compile(rf"str({str})")
        return filter(lambda line: regexp.search(line), value)
