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

# *: Introduction
class EVT_in_2D_Problem(Slide):
	def construct(self):
		pass
class EVT_in_2D_Solution(Slide):
	def construct(self):
		pass
class EVT_in_3D_Problem(ThreeDSlide):
	def construct(self):
		pass
class EVT_in_3D_Solution(ThreeDSlide):
	def construct(self):
		pass
class Lagrange_Multipliers_Problem(ThreeDSlide):
	def construct(self):
		pass
class Lagrange_Multipliers_Solution(ThreeDSlide):
	def construct(self):
		pass
class Key_Differences(Slide): # *: Between when to apply EVT in 3D vs. LM.
	def construct(self):
		pass
# *: Profit
	class Profit_Problem(Slide):
		def construct(self):
			pass
	class Profit_Solution(Slide): # TODO: Ask if a 3D version is requested?
		def construct(self):
			pass
# *: Cobb-Douglas
class Cobb_Douglas_Introduction(ThreeDSlide):
	def construct(self):
		pass
class Cobb_Douglas_Problem(Slide):
	def construct(self):
		pass
class Cobb_Douglas_Solution(ThreeDSlide):
	def construct(self):
		pass
# *: 