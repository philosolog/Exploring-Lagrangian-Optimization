from manim import *
from manim_slides import Slide, ThreeDSlide

def make_textbox(str, box):
		myBaseTemplate = TexTemplate( # TODO: Make my own preamble...
			documentclass="\documentclass[preview]{standalone}"
		)
		myBaseTemplate.add_to_preamble(r"\usepackage{ragged2e}")

		text = Tex("\\justifying{" + str + "}", tex_template=myBaseTemplate).scale(0.5)
		text.move_to(box)

		return VGroup(box, text)

class Example_1_1(ThreeDSlide):
	def construct(self):
		self.set_camera_orientation(phi=90*DEGREES, theta=0)
		box = Prism([2, 4, 0.05]) # TODO: Animate cardboard folding.
		box.set_color(DARK_BROWN)
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
		q1 = make_textbox(
			"We have a piece of cardboard that is 2 feet by 4 feet and we're going to cut out the corners and fold up the sides to form a box.\\\\\\\\Determine the height of the box that will give a maximum volume.",
			q1_textbox
		)
		self.add_fixed_in_frame_mobjects(q1)
		self.play(FadeIn(q1))

		self.next_slide(loop=True)
		self.play(Wiggle(box))

		self.next_slide()
		self.play(Unwrite(q1))
		self.move_camera(frame_center=np.array([0, 0, 0]))
		box.generate_target()
		box.target.set_color(BLACK)
		box.target.scale(0)
		self.play(
			MoveToTarget(box)
		)
		# s1 = Rectangle().scale(0.5)
		# s2 = Triangle().shift(DOWN + RIGHT).scale(0.5)
		# c = Cutout(s1, s2, fill_opacity=1, color=BLUE, stroke_color=RED)
		# self.add_fixed_in_frame_mobjects(c)
		# self.play(Write(c), run_time=1)

class Example_1_2(Slide):
	def construct(self):
		board = Rectangle(color=DARK_BROWN, height=2, width=4, fill_opacity=1).scale(2)

		self.next_slide()
		c1 = Square().scale(0.5)
		c1.move_to(board.get_corner(UL)+c1.get_corner(DR))
		c2 = Square().scale(0.5)
		c2.move_to(board.get_corner(UR)+c2.get_corner(DL))
		c3 = Square().scale(0.5)
		c3.move_to(board.get_corner(DL)+c3.get_corner(UR))
		c4 = Square().scale(0.5)
		c4.move_to(board.get_corner(DR)+c4.get_corner(UL))
		template = Cutout(board, c1, c2, c3, c4, fill_opacity=1, color=DARK_BROWN, stroke_color=BLUE, stroke_opacity=0.125)
		self.play(Write(template), run_time=1)
