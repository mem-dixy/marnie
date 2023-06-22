""""""

import enum
import math

from celestine.typed import (
    D,
    N,
    S,
)
from celestine.window.collection import (
    Collection,
    Item,
    Rectangle,
)


class Zone(enum.Enum):
    """"""

    DROP = enum.auto()
    GRID = enum.auto()
    NONE = enum.auto()
    SPAN = enum.auto()


class Container(Item, Collection):
    """"""

    item: D[S, Item]

    def call(self, name, text, action, **star):
        """"""
        self.save(
            self._button(
                name,
                text,
                call=self.window.work,
                action=action,
                argument=star,
                ring=self.ring,
                **star,
            )
        )

    def draw(self, ring, view, **star):
        """"""
        for _, item in self.item.items():
            item.draw(ring, view, **star)

    def image(self, name, path, **star):
        """A thumbnail image of a big picture."""
        self.save(
            self._image(
                name,
                path,
                **star,
            )
        )

    def label(self, name, text, **star):
        """"""
        self.save(
            self._label(
                name,
                text,
                **star,
            )
        )

    def poke(self, x_dot, y_dot, **star):
        """"""
        for _, item in self.item.items():
            item.poke(x_dot, y_dot, **star)

    def spot(self, area: Rectangle, **star) -> N:
        """"""
        self.area.copy(area)

        match self.mode:
            case Zone.DROP:
                partition_x = 1
                partition_y = len(self.item)
            case Zone.SPAN:
                partition_x = len(self.item)
                partition_y = 1
            case Zone.GRID:
                partition_x = self.width
                partition_y = math.ceil(len(self.item) / self.width)
            case Zone.NONE:
                partition_x = 1
                partition_y = 1

        size_x, size_y = self.area.size
        index = 0

        fragment_x = size_x // partition_x
        fragment_y = size_y // partition_y

        items = self.item.items()
        for _, item in items:
            index_x = index % partition_x
            index_y = min(index // partition_x, partition_y - 1)
            index += 1

            ymin = self.area.upper + fragment_y * (index_y + 0)
            ymax = self.area.upper + fragment_y * (index_y + 1)
            xmin = self.area.left + fragment_x * (index_x + 0)
            xmax = self.area.left + fragment_x * (index_x + 1)

            rectangle = Rectangle(xmin, ymin, xmax, ymax)
            item.spot(rectangle)

    def view(self, name, text, action):
        """"""
        item = self._button(
            name,
            text,
            call=self.turn,
            action=action,
            argument={},
        )
        return self.save(item)

    def zone(self, name: S, *, mode=Zone.SPAN, **star):
        """"""
        return self.item_set(
            name,
            Container(
                self.ring,
                name,
                self.window,
                self.element,
                self.area,
                mode=mode,
                **star,
            ),
        )

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False

    def __init__(
        self,
        ring,
        name,
        window,
        element,
        area,
        *,
        mode=Zone.NONE,
        row=0,
        col=0,
        **star,
    ) -> N:
        self.ring = ring

        self.window = window

        self.data = None
        #
        self.element = element
        self._button = element["button"]
        self._image = element["image"]
        self._label = element["label"]

        self.turn = window.turn

        super().__init__(name, area, **star)

        self.width = col
        self.height = row
        self.mode = mode

        for range_y in range(row):
            for range_x in range(col):
                name = f"{self.name}_{range_x}-{range_y}"
                self.item[name] = Item(name, area)
