"""The View page."""


from celestine.session.session import Session
from celestine.typed import N
from celestine.window.container import Container as View


def main(ring: Session, view: View) -> N:
    """"""
    with view.zone("main") as line:
        line.call(
            "main_action",
            "Translate Files",
            "translate",
        )


# TODO:figure out how to make actions not trigger on function load
def report(ring: Session, view: View) -> N:
    """"""
    with view.zone("head") as line:
        line.label("title", "Page main")
    train = {}

    line.call(
        "main_action",
        "Translate Files",
        "train",
        page=ring,
    )

    for tag, text in train.items():
        with view.zone("body") as line:
            line.label(tag, text)
