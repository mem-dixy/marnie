"""Python Game Development."""


from celestine.session import Abstract
from celestine.typed import (
    A,
    M,
    S,
)


class Package(Abstract):
    """"""

    image: M

    def __getattr__(self, name: S) -> A:
        result = None
        match name:
            case _:
                result = getattr(self.package, name)
        return result
