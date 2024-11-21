from manim import *


class TitlePage(VGroup):
    def __init__(self):
        super().__init__()
        self.construct()

    def construct(self):
        self.add(Text("DevCom: Containers Dev & Deployment"))
        self.add(Underline(self[0]))
        # author = Text("Tane Barriball", color=YELLOW, font_size=36)
        # author.next_to(title, DOWN)


class ContentsPage(VGroup):
    def __init__(self):
        super().__init__()
        self.construct()

    def construct(self):
        self.add(Text("Outline"))
        self.add(Underline(self[0]))
        self.add(Square(side_length=0.2))
        self[2].set_opacity(0)
        self.add(Text("- Containers 101", font_size=24))
        self.add(Text("- Best practices", font_size=24))
        self.add(Text("- Deployment", font_size=24))
        self.arrange(DOWN, center=False, aligned_edge=LEFT).move_to(LEFT * 3)
