""""""


from celestine.interface import Abstract as Abstract_
from celestine.interface import Button as Button_
from celestine.interface import Image as Image_
from celestine.interface import Label as Label_
from celestine.interface import View as View_
from celestine.interface import Window as Window_
from celestine.typed import (
    A,
    B,
    C,
    H,
    N,
    P,
    R,
    override,
)
from celestine.window.collection import Plane


class Abstract(Abstract_):
    """"""

    @override
    def hide(self) -> N:
        """"""
        super().hide()
        if self.keep:
            # check may be removed if view has object
            self.keep.place_forget()

    @override
    def show(self) -> N:
        """"""
        super().show()
        if self.keep:
            # check may be removed if view has object
            # also this mostly calling render()
            width, height = self.area.size
            dot_x, dot_y = self.area.origin.int
            self.keep.place(
                x=dot_x,
                y=dot_y,
                width=width,
                height=height,
            )

    def render(self, keep: C, **star: R) -> N:
        """"""
        self.keep = keep(self.canvas, **star)

        width, height = self.area.size
        dot_x, dot_y = self.area.origin.int
        self.keep.place(
            x=dot_x,
            y=dot_y,
            width=width,
            height=height,
        )


class Button(Button_, Abstract):
    """"""

    def callback(self) -> N:
        """"""
        self.call(self.action, **self.argument)

    @override
    def make(self, canvas: A, **star: R) -> B:
        """"""
        tkinter = self.hold.package.tkinter

        if super().make(canvas, **star):
            self.render(
                tkinter.Button,
                command=self.callback,
                text=f"button: {self.data}",
            )

        return True


class Image(Image_, Abstract):
    """"""

    @override
    def make(self, canvas: A, **star: R) -> B:
        """"""
        tkinter = self.hold.package.tkinter

        if super().make(canvas, **star):
            self.render(
                tkinter.Label,
                image=self.image.image,
            )

        return True

    @override
    def update(self, path: P, **star: R) -> N:
        """"""
        super().update(path)
        tkinter = self.hold.package.tkinter
        pillow = self.hold.package.pillow

        if pillow:
            image = pillow.open(self.path)
            size = self.resize(image.size)
            image.resize(size)
            self.image = pillow.ImageTk.PhotoImage(image=image.image)
        else:
            self.image = tkinter.PhotoImage(file=self.path)

        self.keep.configure(image=self.image)
        self.keep.image = self.image


class Label(Label_, Abstract):
    """"""

    @override
    def make(self, canvas: A, **star: R) -> B:
        """"""
        tkinter = self.hold.package.tkinter

        if super().make(canvas, **star):
            self.render(
                tkinter.Label,
                fg="blue",
                height=4,
                text=f"label: {self.data}",
                width=100,
            )

        return True


class View(View_, Abstract):
    """"""

    @override
    def hide(self) -> N:
        """"""
        super().hide()
        for _, item in self:
            item.hide()

    @override
    def show(self) -> N:
        """"""
        super().show()
        for _, item in self:
            item.show()


class Window(Window_, Abstract):
    """"""

    @override
    def extension(self):
        """"""
        if self.hold.package.pillow:
            return self.hold.package.pillow.extension()

        return [
            ".pbm",
            ".pgm",
            ".ppm",
            ".pnm",
            ".gif",
            ".png",
        ]

    @override
    def make(self, canvas: A, **star: R) -> B:
        """"""
        tkinter = self.hold.package.tkinter

        canvas = self.hold.package.tkinter.Tk()
        canvas.title(self.hold.language.APPLICATION_TITLE)
        canvas.geometry("1920x1080")
        canvas.minsize(640, 480)
        canvas.maxsize(3840, 2160)
        canvas.config(bg="blue")

        if super().make(canvas, **star):
            for _, item in self:
                canvas1 = tkinter.Frame(
                    canvas,
                    padx=5,
                    pady=5,
                    bg="skyblue",
                    width=1920,
                    height=1080,
                )
                canvas1.place(x=0, y=0)
                item.make(canvas1)

        return True

    @override
    def turn(self, page):
        super().turn(page)
        self.page.canvas.tkraise()

    @override
    def __exit__(self, exc_type, exc_value, traceback):
        super().__exit__(exc_type, exc_value, traceback)
        self.canvas.mainloop()
        return False

    @override
    def __init__(self, hold: H, **star: R) -> N:
        element = {
            "button": Button,
            "image": Image,
            "label": Label,
            "view": View,
            "window": self,
        }
        super().__init__(hold, element, **star)
        self.area = Plane.make(1280, 1080)
