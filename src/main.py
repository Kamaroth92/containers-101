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
        title.add(
            Text('"Containers with Tane"', font_size=36, color=YELLOW).next_to(
                title[1], DOWN
            )
        )
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

        subheading = VGroup()
        subheading.add(Text(" . ").next_to(heading[0], RIGHT))
        subheading.add(
            Text("What are containers?", font_size=24).next_to(subheading[0], RIGHT)
        )
        subheading.add(Underline(subheading[1]))
        self.play(Write(subheading))
        self.next_slide(notes=speakerNotes.render())
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

        self.next_slide(notes=speakerNotes.render())
        self.play(*[FadeOut(mob) for mob in self.mobjects if type(mob) is not VGroup])

        subheading2 = VGroup()
        subheading2.add(Text(" . ").next_to(heading[0], RIGHT))
        subheading2.add(
            Text("Containers and VMs", font_size=24).next_to(subheading2[0], RIGHT)
        )
        subheading2.add(Underline(subheading2[1]))

        self.play(ReplacementTransform(subheading, subheading2))
        vm_title = (
            Text("Virtual Machines", font_size=24)
            .to_edge(UP)
            .shift(LEFT * 3.5)
            .shift(DOWN)
        )
        container_title = (
            Text("Containers", font_size=24).to_edge(UP).shift(RIGHT * 3.5).shift(DOWN)
        )
        divider = Line(Dot().move_to(UP * 3), Dot().move_to(DOWN * 3))
        self.play(Write(vm_title), Write(container_title), Write(divider))

        self.next_slide(notes=speakerNotes.render())
        phys_machine = Rectangle(width=5, height=0.8, color=BLUE).shift(DOWN * 2.5)
        phys_machine_label = Text("Phyiscal Machine", font_size=20).move_to(
            phys_machine.get_center()
        )
        vm_hypervisor = Rectangle(width=5, height=0.8, color=GREEN).next_to(
            phys_machine, UP, buff=0.1
        )
        hypervisor_label = Text("Hypervisor", font_size=20).move_to(vm_hypervisor)

        vm1 = (
            Rectangle(width=1.5, height=2.5, color=RED)
            .next_to(vm_hypervisor, UP, buff=0.1)
            .shift(LEFT * 1.7)
        )
        vm1_label = Text("VM1\n- Guest OS\n- Libraries\n- App", font_size=16).move_to(
            vm1
        )
        vm2 = Rectangle(width=1.5, height=2.5, color=RED).next_to(
            vm_hypervisor, UP, buff=0.1
        )
        vm2_label = Text("VM2\n- Guest OS\n- Libraries\n- App", font_size=16).move_to(
            vm2
        )
        vm3 = (
            Rectangle(width=1.5, height=2.5, color=RED)
            .next_to(vm_hypervisor, UP, buff=0.1)
            .shift(RIGHT * 1.7)
        )
        vm3_label = Text("VM3\n- Guest OS\n- Libraries\n- App", font_size=16).move_to(
            vm3
        )

        vm = VGroup()
        vm.add(phys_machine, phys_machine_label)
        vm.add(vm_hypervisor, hypervisor_label)
        vm.add(vm1, vm1_label)
        vm.add(vm2, vm2_label)
        vm.add(vm3, vm3_label)
        vm.shift(LEFT * 3.5)

        self.play(Write(vm))
        self.wait(3)
        speakerNotes.title = "Runtimes"
        speakerNotes.body = """
            - runc: Default Docker runtime, OCI-compliant.
            - containerd: Daemon-based runtime used by Docker.
            - CRI-O: Lightweight runtime for Kubernetes, OCI-compliant.
            - Kata Containers: Secure runtime using micro-VMs for isolation.
            - gVisor: Secure runtime with kernel emulation in user space.
            - crun: Faster, lightweight runc alternative written in C.
            - youki: OCI-compliant runtime written in Rust.
            """
        self.next_slide(notes=speakerNotes.render())
        phys_machine2 = Rectangle(width=5, height=0.8, color=YELLOW).shift(DOWN * 2.5)
        phys_machine2_label = Text(
            "Phyiscal Machine Shared Kernel", font_size=20
        ).move_to(phys_machine2.get_center())

        container_runtime = Rectangle(width=5, height=0.8, color=GREEN).next_to(
            phys_machine2, UP, buff=0.1
        )

        runtime_label = Text("Container Runtime", font_size=18).move_to(
            container_runtime
        )

        container1 = (
            Rectangle(width=1.5, height=1.8, color=ORANGE)
            .next_to(container_runtime, UP, buff=0.1)
            .shift(LEFT * 1.7)
        )
        container1_label = Text("Container1\n- Libraries\n- App", font_size=16).move_to(
            container1
        )
        container2 = Rectangle(width=1.5, height=1.8, color=ORANGE).next_to(
            container_runtime, UP, buff=0.1
        )
        container2_label = Text("Container2\n- Libraries\n- App", font_size=16).move_to(
            container2
        )
        container3 = (
            Rectangle(width=1.5, height=1.8, color=ORANGE)
            .next_to(container_runtime, UP, buff=0.1)
            .shift(RIGHT * 1.7)
        )
        container3_label = Text("Container3\n- Libraries\n- App", font_size=16).move_to(
            container3
        )

        container = VGroup()
        container.add(phys_machine2, phys_machine2_label)
        container.add(container_runtime, runtime_label)
        container.add(container1, container1_label)
        container.add(container2, container2_label)
        container.add(container3, container3_label)
        container.shift(RIGHT * 3.5)

        self.play(Write(container))

        self.next_slide(notes=speakerNotes.render())
        self.play(
            *[FadeOut(mob) for mob in self.mobjects if type(mob) is not VGroup],
            FadeOut(vm),
            FadeOut(container),
        )

        subheading3 = VGroup()
        subheading3.add(Text(" . ").next_to(heading[0], RIGHT))
        subheading3.add(
            Text("Building a container", font_size=24).next_to(subheading3[0], RIGHT)
        )
        subheading3.add(Underline(subheading3[1]))
        self.play(ReplacementTransform(subheading2, subheading3))
        self.next_slide(notes=speakerNotes.render())

        dockerfile = Code(
            "files/Dockerfile",
            tab_width=4,
            background_stroke_width=1,
            background_stroke_color=WHITE,
            insert_line_no=False,
            language="docker",
        )

        dockerfile_instructions = Code(
            "files/instructions",
            tab_width=4,
            background_stroke_width=1,
            background_stroke_color=WHITE,
            insert_line_no=False,
            language="docker",
        )

        VGroup(dockerfile, dockerfile_instructions).arrange(RIGHT, buff=1.5)
        self.play(Write(dockerfile_instructions))
        self.next_slide(notes=speakerNotes.render())
        self.play(Write(dockerfile))
        self.next_slide(notes=speakerNotes.render())
        self.play(*[FadeOut(mob) for mob in self.mobjects if type(mob) is not VGroup])

        # # =============================================================
        # heading = VGroup()
        # heading.add(Text("Containers 101", font_size=24).to_corner(UL))
        # heading.add(Underline(heading[0]))
        # subheading3 = VGroup()
        # subheading3.add(Text(" . ").next_to(heading[0], RIGHT))
        # subheading3.add(
        #     Text("Building a container", font_size=24).next_to(subheading3[0], RIGHT)
        # )
        # subheading3.add(Underline(subheading3[1]))
        # self.add(heading, subheading3)
        # self.wait(1)
        # # =============================================================

        subheading4 = VGroup()
        subheading4.add(Text(" . ").next_to(heading[0], RIGHT))
        subheading4.add(Text("Layers", font_size=24).next_to(subheading4[0], RIGHT))
        subheading4.add(Underline(subheading4[1]))
        self.play(ReplacementTransform(subheading3, subheading4))

        layer = Layer().shift(LEFT * 3.5)
        self.play(Write(layer))
        self.play(layer[0].animate.arrange(DOWN, buff=0.8).shift(LEFT * 3))
        layer1_text = Text("'FROM ubuntu:latest'", font_size=20).next_to(layer[0][0])
        layer2_text = Text(
            "'RUN apt-get update && apt-get install -y curl'", font_size=20
        ).next_to(layer[0][1])
        layer3_text = Text(
            "'COPY hello.sh /usr/local/bin/hello.sh'", font_size=20
        ).next_to(layer[0][2])
        self.play(Write(layer1_text), Write(layer2_text), Write(layer3_text))
        self.wait(3)
