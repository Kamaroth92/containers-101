from .container_symbols import *


class Buffer(VGroup):
    def __init__(self, count=3):
        self.count = count
        super().__init__()

        buffer = Square()
        buffer.set_opacity(0)
        self.add(buffer)
