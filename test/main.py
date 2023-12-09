from manim import *
from manim_slides import Slide, ThreeDSlide

class lesson(Slide):
    def construct(self):
        circle = Circle(radius=3, color=BLUE)
        dot = Dot()

        self.play(GrowFromCenter(circle))

        self.next_slide(loop=True)
        self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
        
        self.next_slide()
        self.play(dot.animate.move_to(ORIGIN))