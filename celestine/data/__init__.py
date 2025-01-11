""""""

from celestine import (
    bank,
    load,
    regex,
)
from celestine.interface import View
from celestine.literal import FULL_STOP
from celestine.typed import (
    A,
    B,
    C,
    N,
    Protocol,
    R,
    S,
    W,
)


class Code(Protocol):
    """Type for code functions."""

    def __call__(self, **star: R) -> B:
        raise NotImplementedError(self, star)


class Draw(Protocol):
    """Type for draw functions."""

    def __call__(self, view: View) -> N:
        raise NotImplementedError(self, view)


def call(function: Code) -> Code:
    """"""

    def decorator(**star: R) -> B:
        return function(**star)

    return decorator


def draw(function: Draw) -> Draw:
    """"""

    def decorator(view: View) -> N:
        return function(view)

    return decorator


def main(function: Draw) -> Draw:
    """"""

    def decorator(view: View) -> N:
        return function(view)

    return decorator


def wrapper(name: S) -> C[[W[A]], A]:
    """"""

    def rapper(function: W[A]) -> W[A]:

        wrap = None

        def decorator(*data: A, **star: R) -> A:
            nonlocal wrap
            if not wrap:
                pattern = r"<function ([\w\.]+) "
                string = repr(function)
                find = regex.match(pattern, string)

                split = name.split(FULL_STOP)
                index = split[-1]
                source = bank.package[index].package
                wrap = load.find_function(source, find)

            try:
                result = function(*data, **star, wrap=wrap)
            except NotImplementedError:
                result = wrap(*data, **star)

            return result

        return decorator

    return rapper
