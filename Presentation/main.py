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
class Single_Variable_Optimization(ThreeDSlide):
	def construct(self):
		pass
class EVT_in_3D(ThreeDSlide):
	def construct(self):
		pass
class Removing_the_Bounds(ThreeDSlide):
	def construct(self):
		pass
class Deriving_the_Method(ThreeDSlide):
	def construct(self):
		pass

# *: Examples
class Cobb_Douglas(ThreeDSlide):
	def construct(self):
		pass
class Cobb_Douglas_Optimization(ThreeDSlide):
	def construct(self):
		pass