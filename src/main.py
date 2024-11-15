from manim import *
from manim_slides import Slide

from mobjects import *
from scenes import *


class Main(Slide):
    def construct(self):
        self.next_slide(notes="Start")
        blocker = Square()
        blocker.set_opacity(0)
        self.play(Create(blocker))

        self.next_slide(notes="Introduction")
        title = Title()
        self.play(Create(title))
        self.next_slide(notes="Next")
        sym = Layer()
        dot = Dot()
        circle = Circle(radius=3, color=RED)
        self.play(GrowFromCenter(circle))
        self.next_slide()
        self.play(Create(sym))

        self.next_slide(loop=True)
        self.play(MoveAlongPath(dot, sym[0][0]), run_time=2, rate_func=linear)
        # check = Tex(r"\checkmark", color=GREEN, stroke_width=8).scale(3)
        # check.stretch(0.8, dim=1)
        # check.stretch(1.1, dim=0)
        # self.add(check)
