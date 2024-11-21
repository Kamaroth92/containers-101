from manim import *
from manim_slides import Slide

from mobjects import *

import textwrap


class SpeakerNotes:
    def __init__(self, title="", body="", next="") -> None:
        self._title = title
        self._body = body
        self._next = next

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def body(self):
        tNext = self._body
        self.body = ""
        return textwrap.dedent(tNext)

    @body.setter
    def body(self, value):
        self._body = value

    @property
    def next(self):
        tNext = self._next
        self.next = ""
        return tNext

    @next.setter
    def next(self, value):
        self._next = value

    def render(self):
        notes = ""
        title = self.title
        body = self.body
        next = self.next
        if title != "":
            notes += f"**{title}**  \n"
        if body != "":
            notes += f"{body}  \n"
        if next != "":
            notes += f"*Next: {next}*  \n"
        return notes


class Main(Slide):
    def construct(self):
        speakerNotes = SpeakerNotes()
        self.wait_time_between_slides = 1
        self.skip_reversing = True
        self.skip_animations = True

        buffer = Dot()
        buffer.to_corner(UL)
        self.add(buffer)
        self.wait()
        self.next_slide(notes=speakerNotes.render())
        self.remove(buffer)

        speakerNotes.title = "Introduction"
        speakerNotes.next = "Outline"
        self.next_slide(notes=speakerNotes.render())
        title = VGroup()
        title.add(Text("DevCom: Containers Dev & Deployment"))
        title.add(Underline(title[0]))
        # title.add(
        #     Text('"Containers with Tane"', font_size=36, color=YELLOW).next_to(
        #         title[1], DOWN
        #     )
        # )
        self.play(Write(title))

        speakerNotes.title = "Outline"
        speakerNotes.body = """
            - quick 101 to make sure everyone is on the same page
            - best practices for developing and running containers
            - moving them to production, how might you run them.
                - ecs, kubernetes, open shift
            """
        self.next_slide(notes=speakerNotes.render())
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        outline = VGroup(Text("Outline").move_to(UP * 1.2))
        outline.add(Underline(outline[0]))
        contents = VGroup()
        contents.add(Text("- Containers 101", font_size=24))
        contents.add(Text("- Best practices", font_size=24))
        contents.add(Text("- Deployment", font_size=24))
        contents.arrange(DOWN, center=True, aligned_edge=LEFT).next_to(
            outline, DOWN * 2
        )
        self.play(Write(outline), Write(contents))

        speakerNotes.title = "Containers 101"
        self.next_slide(notes=speakerNotes.render())
        heading = VGroup()
        heading.add(Text("Containers 101", font_size=24).to_corner(UL))
        heading.add(Underline(heading[0]))
        tContents = contents[0].copy()
        contents.remove(contents[0])
        self.add(tContents)
        self.play(Circumscribe(tContents))
        self.play(
            *[Unwrite(mob) for mob in [*contents, *outline]],
            ReplacementTransform(tContents, heading),
        )
        # self.add(heading)  ## DELETE ME

        # self.next_slide(notes=speakerNotes.render())
        subheading = VGroup()
        subheading.add(Text(" . ").next_to(heading[0], RIGHT))
        subheading.add(
            Text("What are containers?", font_size=24).next_to(subheading[0], RIGHT)
        )
        subheading.add(Underline(subheading[1]))
        self.play(Write(subheading))
        body = VGroup()
        body.add(Text("Lightweight, portable, and isolated", font_size=24))
        body.add(Text("Package applications with their dependencies", font_size=24))
        body.add(Text("Makes use of the operating system kernel", font_size=24))
        body.arrange(DOWN, center=True, aligned_edge=LEFT)
        self.play(Write(body[0]))
        self.play(Write(body[1]))
        self.play(Write(body[2]))

        self.next_slide(notes=speakerNotes.render())
        body_h = VGroup()
        body_h.add(
            Text(
                "Lightweight, portable, and isolated",
                font_size=24,
                t2c={"isolated": RED},
            )
        )
        body_h.add(Text("Package applications with their dependencies", font_size=24))
        body_h.add(Text("Makes use of the operating system kernel", font_size=24))
        body_h.arrange(DOWN, center=True, aligned_edge=LEFT)
        self.play(FadeTransform(body[0], body_h[0]))

        self.wait(3)
