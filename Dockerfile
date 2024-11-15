FROM manimcommunity/manim:latest
RUN pip install manim-slides[pyqt6-full]
ENV PATH=$HOME/.local/bin:$PATH

EXPOSE 8000

WORKDIR /work
