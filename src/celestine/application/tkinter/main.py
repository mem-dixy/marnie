"""Package tkinter."""
# https://docs.python.org/3/library/tk.html
# https://www.tcl.tk/man/tcl8.6/TkCmd/contents.html
import tkinter
import tkinter.ttk
import tkinter.filedialog
from functools import partial

from celestine.application.window import Window as Window_


class Wiget():
    def __init__(self, item):
        self.item = item

    def grid(self, cord_x, cord_y):
        self.item.grid(column=cord_x, row=cord_y)


class Button(Wiget):
    def __init__(self, frame, text, command):
        super().__init__(
            tkinter.Button(
                frame,
                text=text,
                command=command,
            )
        )


class Label(Wiget):
    def __init__(self, frame, text, width, height, fg):
        super().__init__(
            tkinter.Label(
                frame,
                text=text,
                width=width,
                height=height,
                fg=fg,
            )
        )


class Image():
    """Holds an image."""

    def __init__(self, file):
        _image = tkinter.PhotoImage(file=file)
        self.height = _image.height()
        self.image = _image
        self.width = _image.width()
        self.name = file


class Window(Window_):

    def __init__(self, session):
        super().__init__(session)
        self.root = None

    def show_frame(self, index):
        frame = self.frame_get(index)
        frame.tkraise()

    def file_dialog_load(self, frame, tag):
        """pass"""
        filename = tkinter.filedialog.askopenfilename(
            initialdir="/",
            title="Select a File",
            filetypes=(
                ("Text files", "*.txt*"),
                ("all files", "*.*")
            )
        )
        self.item_get(frame, tag).configure(text="File Opened: " + filename)

    def image_load(self, file):
        """pass"""
        return Image(file)

    def button(self, frame, tag, label, action):
        item = Button(
            self.frame_get(frame),
            label,
            lambda: self.show_frame(action),
        )
        self.item_set(frame, tag, item)
        return item


    def file_dialog(self, frame, tag, bind, cord_x, cord_y):
        """pass"""
        self.item_set(
            frame,
            tag,
            tkinter.Button(
                self.frame_get(frame),
                text="Config find Exit",
                command=partial(self.file_dialog_load, frame, bind),
            ),
        )
        self.item_get(frame, tag).grid(column=cord_x, row=cord_y)

    def image(self, frame, tag, _image, cord_x, cord_y):
        """pass"""
        self.item_set(
            frame,
            tag,
            tkinter.Label(
                self.frame_get(frame),
                image=_image.image,
            ),
        )
        self.item_get(frame, tag).grid(column=cord_x, row=cord_y)

    def label(self, frame, tag, text):
        item = Label(
            self.frame_get(frame),
            text,
            width=100,
            height=4,
            fg="blue",
        )
        self.item_set(frame, tag, item)
        return item

    def main(self):
        """def main"""

        self.root = tkinter.Tk()
        self.root.title(self.session.language.APPLICATION_TITLE)

        self.root.geometry("1920x1080")
        self.root.minsize(640, 480)
        self.root.maxsize(3840, 2160)
        self.root.config(bg="blue")

        index = 0
        for window in self.session.window:
            frame = tkinter.Frame(self.root, padx=5, pady=5, bg="skyblue")
            frame.grid(row=0, column=0, sticky="nsew")

            self.frame_set(index, frame)
            window.main(self.session, index, self)
            index += 1

        self.show_frame(0)

        self.root.mainloop()
