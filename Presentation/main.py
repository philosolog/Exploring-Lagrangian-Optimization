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

# *: Aaron
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
# *: Brennan & Jordan
class test(Slide):
	def construct(self):
		# *: 1
		mcdonalds = SVGMobject("references/mcdonalds.svg").scale_to_fit_width(6).to_edge(LEFT)
		mcdonalds_text = Tex("McDonald's").move_to(LEFT*2.5)
		mcdonalds_text.set_color_by_gradient(YELLOW, RED)
		burger_king = SVGMobject("references/burger_king.svg").scale_to_fit_width(6).to_edge(RIGHT)
		burger_king_text = Tex("Burger King").move_to(RIGHT*2.5)
		burger_king_text.set_color_by_gradient(RED, ORANGE)

		self.play(Write(mcdonalds_text))
		self.play(Write(burger_king_text))
		# *: 2
		self.next_slide()
		self.play(Transform(mcdonalds_text, mcdonalds))
		self.play(Transform(burger_king_text, burger_king))
class Cobb_Douglas_Introduction(ThreeDSlide):
	def construct(self):
		pass
class Profit_Problem(Slide):
	def construct(self):
		pass
# *: Kerem & Oliver
		