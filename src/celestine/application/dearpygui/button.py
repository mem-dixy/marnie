from . import dearpygui
from .widget import Widget


class Button(Widget):
    def __init__(self, tag, label, sender, action, function):
        dearpygui.add_button(
            tag=tag,
            label=label,
            user_data=(sender, action),
            callback=function,
        )
