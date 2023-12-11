from manim import *
from manim_slides import ThreeDSlide

class lesson(ThreeDSlide):
	def construct(self):
		self.set_camera_orientation(phi=90*DEGREES, theta=0)
		box = Prism([2, 3, 2])
		box.set_color(LIGHT_BROWN)
		self.play(
			SpinInFromNothing(box, angle=-135*DEGREES)
		)
		self.move_camera(phi=60*DEGREES, theta=0)
		self.play(
			Rotating(box, axis=OUT, radians=-150*DEGREES, run_time=2, rate_func=rate_functions.ease_in_out_elastic)
		)

		self.next_slide()
		self.move_camera(frame_center=np.array([0,4,0]))