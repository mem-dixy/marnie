""""""

from celestine.data import (
    main,
    view,
)
from celestine.typed import OB
from celestine.window.container import View


@main
def zero(view: View) -> OB:
    """"""
    language = view.hold.language
    with view.zone("zero_head") as line:
        line.new("zero_title", text=language.DEMO_ZERO_TITLE)
        line.new(
            "zero_A",
            text=language.DEMO_ZERO_ACTION,
            code="cow",
            say=language.DEMO_ZERO_SAY,
        )
    with view.zone("zero_body") as line:
        line.new("zero_past", text=language.DEMO_MAIN_PAST, view="one")
        line.new("zero_next", text=language.DEMO_MAIN_NEXT, view="two")


@view
def one(view: View) -> OB:
    """"""
    language = view.hold.language
    with view.zone("one_head") as line:
        line.new("one_title", text=language.DEMO_ONE_TITLE)
        line.new(
            "one_A",
            text=language.DEMO_ONE_ACTION,
            code="cow",
            say=language.DEMO_ONE_SAY,
        )
    with view.zone("one_body") as line:
        line.new("one_past", text=language.DEMO_ONE_PAST, view="zero")
        line.new("one_next", text=language.DEMO_ONE_NEXT, view="two")


@view
def two(view: View) -> OB:
    """"""
    language = view.hold.language
    with view.zone("two_head") as line:
        line.new("two_title", text=language.DEMO_TWO_TITLE)
        line.new(
            "two_A",
            text=language.DEMO_TWO_ACTION,
            code="cow",
            say=language.DEMO_TWO_SAY,
        )
    with view.zone("two_body") as line:
        line.new("two_past", text=language.DEMO_TWO_PAST, view="one")
        line.new("two_next", text=language.DEMO_TWO_NEXT, view="zero")
