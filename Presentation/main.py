from manim import *
from manim_slides import ThreeDSlide

class Box(ThreeDSlide):
	def make_textbox(self, str, box):
		myBaseTemplate = TexTemplate( # TODO: Make my own preamble...
			documentclass="\documentclass[preview]{standalone}"
		)
		myBaseTemplate.add_to_preamble(r"\usepackage{ragged2e}")

		text = Tex("\\justifying{" + str + "}", tex_template=myBaseTemplate).scale(0.5)
		text.move_to(box)

		return VGroup(box, text)
	def construct(self):
		self.set_camera_orientation(phi=90*DEGREES, theta=0)
		box = Prism([2, 3, 2]) # TODO: Animate cardboard cutting.
		box.set_color(LIGHT_BROWN)
		self.play(
			SpinInFromNothing(box, angle=-135*DEGREES)
		)
		self.move_camera(phi=60*DEGREES, theta=0)
		self.play(
			Rotating(box, axis=OUT, radians=-150*DEGREES, run_time=2, rate_func=rate_functions.ease_in_out_elastic)
		)

		self.next_slide()
		self.move_camera(frame_center=np.array([0, 4.5, 0]))
		q1_textbox = Rectangle(width=9, height=2, stroke_width=0).shift(RIGHT*2.5)
		q1 = self.make_textbox(
			"We have a piece of cardboard that is 69 inches by 420 inches and we're going to cut out the corners and fold up the sides to form a box.\\\\\\\\Determine the height of the box that will give a maximum volume.",
			q1_textbox
		)
		self.add_fixed_in_frame_mobjects(q1)
		self.play(Write(q1))

		self.next_slide(loop=True)
		self.play(
			Wiggle(box)
		)
class Cobb_Douglas(ThreeDSlide):
	def construct(self):
		self.set_camera_orientation(phi=90*DEGREES, theta=0)
		box = Prism([2, 3, 2]) # TODO: Animate cardboard cutting.
		box.set_color(LIGHT_BROWN)
		self.play(
			SpinInFromNothing(box, angle=-135*DEGREES)
		)