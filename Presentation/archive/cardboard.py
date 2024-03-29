from manim import *
from manim_slides import Slide, ThreeDSlide

def make_textbox(str, box):
		myBaseTemplate = TexTemplate(
			documentclass="\documentclass[preview]{standalone}"
		)
		myBaseTemplate.add_to_preamble(r"\usepackage{ragged2e}")

		text = Tex("\\justifying{" + str + "}", tex_template=myBaseTemplate).scale(0.5)
		text.move_to(box)

		return VGroup(box, text)

class Example_1_1(ThreeDSlide):
	def construct(self):
		# *: Slide 1
		box = Prism([2, 4, 2]) # TODO: Animate cardboard folding.
		box_z_offset = -1.5

		self.set_camera_orientation(phi=90*DEGREES, theta=0)
		box.move_to(point_or_mobject=(0, 0, 1+box_z_offset))
		box.set_color(DARK_BROWN)
		self.play(SpinInFromNothing(box, angle=-135*DEGREES))
		self.move_camera(phi=60*DEGREES, theta=0)
		self.play(Rotating(box, axis=OUT, radians=-150*DEGREES, run_time=2, rate_func=rate_functions.ease_in_out_elastic))

		# *: Slide 2
		self.next_slide()

		q1_textbox = Rectangle(width=9, height=2, fill_opacity=0, stroke_opacity=0).shift(RIGHT*2.5)
		q1 = make_textbox(
			"We have a 2 ft by 4 ft cardboard sheet. We're going to cut square corners and fold up the sides to form a box.\\\\\\\\Determine the height of the box that will give its maximum volume.",
			q1_textbox
		)

		self.move_camera(frame_center=np.array([0, 4.5, 0]))
		self.add_fixed_in_frame_mobjects(q1)
		box.generate_target()
		box.target.stretch_to_fit_depth(1)
		box.target.move_to(point_or_mobject=(0, 0, 1/2+box_z_offset))
		self.play(Write(q1), MoveToTarget(box, run_time=1, rate_func=rate_functions.smootherstep))
		box.generate_target()
		box.target.stretch_to_fit_depth(0.5)
		box.target.move_to(point_or_mobject=(0, 0, 0.5/2+box_z_offset))
		self.play(MoveToTarget(box, run_time=1, rate_func=rate_functions.smootherstep))
		box.generate_target()
		box.target.stretch_to_fit_depth(3.5)
		box.target.move_to(point_or_mobject=(0, 0, 3.5/2+box_z_offset))
		self.play(MoveToTarget(box, run_time=2, rate_func=rate_functions.smootherstep))
		box.generate_target()
		box.target.stretch_to_fit_depth(2)
		box.target.move_to(point_or_mobject=(0, 0, 1+box_z_offset))
		self.play(MoveToTarget(box, run_time=1, rate_func=rate_functions.smootherstep))

		# *: Slide 3
		self.next_slide(loop=True)
		self.play(Wiggle(box))

		# *: Slide 4
		self.next_slide()
		self.play(Unwrite(q1))
		self.move_camera(frame_center=np.array([0, 0, 0]))
		box.generate_target()
		box.target.set_color(BLACK)
		box.target.scale(0)
		self.play(MoveToTarget(box))
class Example_1_2(Slide):
	def construct(self):
		# *: Slide 1
		board = Rectangle(color=DARK_BROWN, height=2, width=4, fill_opacity=1, stroke_opacity=0).scale(2) # TODO: Display cut-edge colors.
		
		self.play(GrowFromPoint(board, board.get_corner(UL)))

		# *: Slide 2
		self.next_slide()

		cuts = [[Square(color=BLACK, fill_opacity=1, stroke_width=0).scale(0.5)] for x in range(4)]
		cuts[0] += [UL, DR]
		cuts[1] += [UR, DL]
		cuts[2] += [DL, UR]
		cuts[3] += [DR, UL]

		for i in range(4):
			cuts[i][0].move_to(board.get_corner(cuts[i][1])+cuts[i][0].get_corner(cuts[i][2]))

		self.play(*[GrowFromPoint(cuts[x][0], board.get_corner(cuts[x][1]), rate_func=rate_functions.smoothererstep, run_time=1) for x in range(4)])

		# *: Slide 3
		self.next_slide()

		def resize_cuts(scale):
			for cut in cuts:
				cut[0].generate_target()
				cut[0].target.scale(scale) # TODO: Move along with scaling.
			self.play(*[MoveToTarget(cuts[x][0]) for x in range(4)])

		resize_cuts(3/2)
		self.wait(0.25)
		resize_cuts(2/3)
		self.wait(0.1)
		resize_cuts(2)
		self.wait(0.15)
		resize_cuts(1/2)