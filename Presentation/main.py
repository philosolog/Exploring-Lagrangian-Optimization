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
		self.play(MoveToTarget(box))
class Example_1_2(Slide):
	def construct(self):
		board = Rectangle(color=DARK_BROWN, height=2, width=4, fill_opacity=1, stroke_opacity=0).scale(2) # TODO: Display cut-edge colors.
		self.play(GrowFromPoint(board, board.get_corner(UL)))

		self.next_slide()
		cuts = [[Square(color=BLACK, fill_opacity=1, stroke_opacity=0).scale(0.5)] for x in range(4)]
		cuts[0] += [UL, DR]
		cuts[1] += [UR, DL]
		cuts[2] += [DL, UR]
		cuts[3] += [DR, UL]
		for i in range(4):
			cuts[i][0].move_to(board.get_corner(cuts[i][1])+cuts[i][0].get_corner(cuts[i][2]))
		self.play(*[GrowFromPoint(cuts[x][0], board.get_corner(cuts[x][1]), rate_func=rate_functions.smoothererstep, run_time=1) for x in range(4)])

		self.next_slide()
		def resize_cuts(scale):
			for cut in cuts:
				cut[0].generate_target()
				cut[0].target.scale(scale)
			self.play(*[MoveToTarget(cuts[x][0]) for x in range(4)])
		resize_cuts(1.75)
		self.wait(0.5)
		resize_cuts(0.75)
		self.wait(0.2)
		resize_cuts(1)
