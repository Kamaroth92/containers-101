from manim import *


class Layer(VGroup):
    def __init__(self, count=3):
        self.count = count
        super().__init__()

        syms = VGroup()
        for i in range(count):
            sym = RoundedRectangle(
                height=0.5,
                width=0.5,
                corner_radius=0.05,
            )
            sym.rotate(PI / 4)
            sym.scale([1, 0.7, 1])
            sym.set_z_index(i * -1)
            sym.set_fill(BLACK, opacity=1)
            # sym.set_sheen(0.4, direction=UP)
            syms.add(sym)
        syms.arrange(DOWN, -0.3)
        self.add(syms)
