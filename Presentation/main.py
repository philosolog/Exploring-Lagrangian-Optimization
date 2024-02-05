from manim import *
from manim_slides import Slide, ThreeDSlide

class MovingCameraSlide(Slide, MovingCameraScene):
    pass

def make_textbox(str, box, **kwargs):
		color = kwargs.get("color", None)
		myBaseTemplate = TexTemplate(
			documentclass="\documentclass[preview]{standalone}"
		)
		myBaseTemplate.add_to_preamble(r"\usepackage{ragged2e}")

		text = Tex(
			r"\justifying{" + str + "}",
			tex_template=myBaseTemplate
		).scale(0.75)

		if color:
			text.color = color

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
class Cobb_Douglas_Introduction(ThreeDSlide):
	def construct(self):
		# *: 1
		title = Text("Applications in Business")
		self.play(Write(title))

		# *: 2
		self.next_slide()
		self.play(FadeOut(title))
class Cobb_Douglas_Problem(MovingCameraSlide):
	def construct(self):
		# *: 1
		mcdonalds = VGroup(SVGMobject("references/mcdonalds.svg").scale_to_fit_width(6).to_edge(LEFT))
		burger_king = VGroup(SVGMobject("references/burger_king.svg").scale_to_fit_width(6).to_edge(RIGHT))

		self.play(Write(mcdonalds))
		self.play(Write(burger_king))

		# *: 2
		self.next_slide()

		ronald = ImageMobject("references/ronald.jpg").move_to(RIGHT*25).scale(1.5)

		self.play(self.camera.frame.animate.move_to(ronald))
		self.play(SpinInFromNothing(ronald))

		# *: 3
		self.next_slide(loop=True)
		self.play(Wiggle(ronald))

		# *: 4
		self.next_slide()

		king = ImageMobject("references/king.jpg").move_to(RIGHT*25).scale(1.25)

		self.play(ShrinkToCenter(ronald))
		self.play(GrowFromCenter(king))

		# *: 5
		self.next_slide()
		self.play(FadeOut(king))
		
		statement_box = Rectangle(width=40, height=20, fill_opacity=0, stroke_opacity=0).move_to(RIGHT*25)
		statement = make_textbox(r"At Burger King, each employee is paid $\$15$ per hour and works $\$10$ hours a day. Each grill costs $\$7,300$ and lasts for $1$ year. On an average day, each unit of input produces $20$ burgers. The output elasticity of capital is $30\%$ while labor's is $70\%$.", statement_box)
		question_box = Rectangle(width=20, height=10, fill_opacity=0, stroke_opacity=0).move_to(RIGHT*25+DOWN*2)
		question = make_textbox(r"To maximize profit, how many grills and workers should this Burger King location have with their budget being $\$1.5$ million per year?", question_box, color=YELLOW)

		self.play(Write(statement))
		self.play(Write(question))
class Cobb_Douglas_Solution(Slide):
	def construct(self):
		pass
class Profit_Problem(Slide):
	def construct(self):
		pass
# *: Kerem & Oliver
		