from manim import *
from manim_slides import Slide, ThreeDSlide

preamble = TexTemplate(documentclass="\documentclass[preview]{standalone}")
preamble.add_to_preamble(r"\usepackage{ragged2e}")
preamble.add_to_preamble(r"\usepackage{amssymb}")

class MovingCameraSlide(Slide, MovingCameraScene):
	pass

def make_textbox(str, box, **kwargs):
		color = kwargs.get("color", None)

		text = Tex(
			r"\justifying{" + str + "}",
			tex_template=preamble
		).scale(0.75)

		if color:
			text.color = color

		text.move_to(box)

		return VGroup(box, text)

# *: Aaron
class Introduction(ThreeDSlide):
	def construct(self):
		# *: 0
		title_1 = Tex("Exploring Lagrangian Optimization\n\nAaron, Brennan, Jordan, Kerem, Oliver", tex_template=preamble)
		
		self.play(Write(title_1))

		# *: 1
		self.next_slide()
		self.play(Unwrite(title_1))

		title_2 = Tex(r"The Extreme Value Theorem in $\mathbb{R}^3$ and Lagrange Multipliers", tex_template=preamble)
		
		self.play(Write(title_2))
		# *: 2
		self.next_slide()
		self.play(FadeOut(title_2))

		axes = ThreeDAxes()
		x_label = axes.get_x_axis_label(Tex("x"))
		y_label = axes.get_y_axis_label(Tex("y")).shift(LEFT + UP*1.6)
		z_label = axes.get_z_axis_label(Tex("z"))
		dot = Dot3D()

		self.set_camera_orientation(phi = 90*DEGREES, theta = 0*DEGREES, distance = 1)

		equation_1 = Tex(r"$z = y^2$\\$y\in [0,\frac{\pi}{2}]$")
		equation_2 = Tex(r"$z = y^2 + \sin(x)$\\$y\in [0,\frac{\pi}{2}]$\\$x\in [0,\frac{\pi}{2}]$")
		equation_3 = Tex(r"$z = y^2 + \sin(x)$\\$y\in [0,-x+\frac{\pi}{2}]$\\$x\in [0,\frac{\pi}{2}]$")
		equation_1.to_corner(UL)
		equation_2.to_corner(UL)
		equation_3.to_corner(UL)
		self.add_fixed_in_frame_mobjects(equation_1)
		self.play(FadeIn(equation_1, shift=RIGHT))
		self.play(Write(axes), FadeIn(dot), FadeIn(x_label), FadeIn(z_label))

		phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers()
		curve_1 = ParametricFunction(
			lambda t: np.array(
				[
					0,
					t,
					t**2
				]
			),
			color = YELLOW,
			t_range = [0, PI/2]
		)

		self.play(Write(curve_1))
		# *: 3
		self.next_slide()

		surface_1_resolution = 8 # TODO: Increase later...
		self.move_camera(phi = 60*DEGREES, theta = 30*DEGREES)

		def surface_1_parameters(u, v):
			x = u
			y = v
			z = y**2 + np.sin(x)
			return np.array([x, y, z])

		surface_1 = Surface(
			surface_1_parameters,
			resolution=(surface_1_resolution, surface_1_resolution),
			v_range=[0, +PI/2],
			u_range=[0, +PI/2]
		)

		surface_1.scale(1, about_point=ORIGIN)
		surface_1.set_style(fill_opacity=0.5,stroke_color=WHITE)
		self.play(FadeOut(equation_1))
		self.add_fixed_in_frame_mobjects(equation_2)
		self.play(FadeIn(equation_2))
		self.play(Write(surface_1), phi.animate.set_value(30*DEGREES), theta.animate.set_value(-120*DEGREES), run_time=2)
		self.play(FadeOut(z_label), FadeIn(y_label))

		# *: 4
		self.next_slide()

		curve_2 = ParametricFunction(
			lambda t: np.array(
				[
					t,
					0,
					np.sin(t)
				]
			),
			color = YELLOW,
			t_range = [0, PI/2]
		)
		curve_3 = ParametricFunction(
			lambda t: np.array(
				[
					PI/2,
					t,
					t**2 + np.sin(PI/2)
				]
			),
			color = YELLOW,
			t_range = [0, PI/2]
		)
		curve_4 = ParametricFunction(
			lambda t: np.array(
				[
					t,
					PI/2,
					(PI/2)**2 + np.sin(t)
				]
			),
			color = YELLOW,
			t_range = [0, PI/2]
		)

		self.play(Write(curve_2))
		self.play(Write(curve_3), Write(curve_4))
		
		# *: 4
		self.next_slide()

		old_curve = Group(curve_3, curve_4)
		curve_5 = ParametricFunction(
			lambda t: np.array(
				[
					t,
					-t + PI/2,
					(-t + PI/2)**2 + np.sin(t)
				]
			),
			color = YELLOW,
			t_range = [0, PI/2]
		)

		self.play(FadeOut(equation_2))
		self.add_fixed_in_frame_mobjects(equation_3)
		self.play(FadeIn(equation_3))
		self.play(Transform(old_curve, curve_5))
class Lagrange_Multipliers(ThreeDSlide):
	def construct(self):
		# *: 1
		self.next_slide()

		title = Tex(r"What the Fuck are Lagrange Multipliers", tex_template=preamble)

		self.play(Write(title))

		# *: 2
		self.next_slide()
		self.play(FadeOut(title))

		e1 = Tex(r"$\nabla f(x,y)=\lambda \nabla g(x,y)$", tex_template=preamble)

		self.play(FadeIn(e1, shift=UP))

		# *: 3
		self.next_slide()

		e2 = Tex(r"$\langle f_x,f_y\rangle =\lambda \langle g_x,g_y\rangle$", tex_template=preamble)

		self.play(Transform(e1, e2))

		# *: 4
		self.next_slide()

		e3 = Tex(r"$f_x(x,y)=\lambda g_x(x,y)$\\$f_y(x,y)=\lambda g_y(x,y)$", tex_template=preamble)

		self.play(Transform(e1, e3))

		# *: 5
		self.next_slide()

		e4 = Tex(r"$f_x(x,y)=\lambda g_x(x,y)$\\$f_y(x,y)=\lambda g_y(x,y)$\\$g(x,y)=k$", tex_template=preamble)

		self.play(Transform(e1, e4))

		# *: 6
		self.next_slide()

		self.play(FadeOut(e1, shift=UP))

		e5 = Tex(r"$...=k$", tex_template=preamble)
		e6 = Tex(r"$...-k=0$", tex_template=preamble)
		e7 = Tex(r"$...-k=g(x,y)$", tex_template=preamble) # *: Dimension bump to take partial derivatives.

		self.play(FadeIn(e5, scale=1.5))
		self.next_slide()
		self.play(Transform(e5, e6))
		self.next_slide()
		self.play(Transform(e5, e7))

class Key_Differences(Slide): # *: Between when to apply EVT in 3D vs. LM.
	def construct(self):
		title = Text("Key Differences")
		self.play(Write(title))

		# *: 2
		self.next_slide()
		self.play(Unwrite(title))

		nerd = SVGMobject("references/nerd.svg").scale_to_fit_width(10)
		self.play(SpinInFromNothing(nerd))
		self.next_slide()
		continuous = ImageMobject("references/continuous_distribution.png").scale_to_fit_width(8)
		self.play(FadeOut(nerd, shift=UP), FadeIn(continuous, shift=UP))
		self.next_slide()
		discrete = ImageMobject("references/discrete_distribution.jpg").scale_to_fit_width(8)
		self.play(FadeOut(continuous, shift=UP), FadeIn(discrete, shift=UP))

# *: Brennan & Jordan
class Cobb_Douglas_Introduction(ThreeDSlide):
	def construct(self):
		# *: 1
		title = Text("Cobb-Douglas and Burgers")
		self.play(Write(title))

		# *: 2
		self.next_slide()
		self.play(FadeOut(title))

		# TODO: Add stuff here
class Cobb_Douglas_Problem(MovingCameraSlide):
	def construct(self):
		# *: 1
		mcdonalds = VGroup(SVGMobject("references/mcdonalds.svg").scale_to_fit_width(6).to_edge(LEFT))
		burger_king = VGroup(SVGMobject("references/burger_king.svg").scale_to_fit_width(6).to_edge(RIGHT))

		self.play(Write(mcdonalds))
		self.play(Write(burger_king))

		# *: 2
		self.next_slide()

		ronald = ImageMobject("references/Ronald.jpg").move_to(RIGHT*25).scale(1.5)

		self.play(self.camera.frame.animate.move_to(ronald))
		self.play(SpinInFromNothing(ronald))

		# *: 3
		self.next_slide(loop=True)
		self.play(Wiggle(ronald))

		# *: 4
		self.next_slide()

		king = ImageMobject("references/King.jpg").move_to(RIGHT*25).scale(1.25)

		self.play(ShrinkToCenter(ronald))
		self.play(GrowFromCenter(king))

		# *: 5
		self.next_slide()
		self.play(FadeOut(king))
		
		statement_box = Rectangle(width=40, height=20, fill_opacity=0, stroke_opacity=0).move_to(RIGHT*25)
		statement = make_textbox(r"At Burger King, each employee is paid $\$15$ per hour and works $10$ hours a day. Each grill costs $\$7,300$ and lasts for $1$ year. On an average day, each unit of input produces $20$ burgers. The output elasticity of capital is $30\%$ while labor's is $70\%$.", statement_box)
		question_box = Rectangle(width=20, height=10, fill_opacity=0, stroke_opacity=0).move_to(RIGHT*25+DOWN*2)
		question = make_textbox(r"To maximize output, how many grills and workers should this Burger King location have with their budget being $\$1.5$ million per year?", question_box, color=YELLOW)

		self.play(Write(statement))
		self.play(Write(question))
class Cobb_Douglas_Solution(Slide):
	def construct(self):
		pass
# *: Kerem & Oliver
class Physics_Problem(Slide):
	def construct(self):
		# *: 1
		title = Text("Dumans")
		self.play(Write(title))

		# *: 2
		self.next_slide()
		self.play(FadeOut(title))
		question_box = Rectangle(width=40, height=20, fill_opacity=0, stroke_opacity=0)
		question = make_textbox(r"Dr. Kerem discovers a new property of an object that relates its pressure (P), volume (V), and time (t). The property is named a Duman and can be represented by the following equation: \[\mathbb{D}(P,V,t)=3P^2Vt\] Novice researcher Aaron wants to maximize the amount of Dumans he can find in his lab. Because Aaron sucks at physics, he wants to make sure that the sum of eight times the unitless pressure, six times the unitless volume, and double the amount of unitless time he uses must equal eight.", question_box)

		self.play(Write(question))

		self.next_slide()
		self.play(Unwrite(question))

		e5 = Tex(r"$8P+6V+2t=8$", tex_template=preamble)
		e6 = Tex(r"$8P+6V+2t-8=0$", tex_template=preamble)
		e7 = Tex(r"$8P+6V+2t-8=g(P,V,t)$", tex_template=preamble) # *: Dimension bump to take partial derivatives.

		self.play(FadeIn(e5, scale=1.5))
		self.next_slide()
		self.play(Transform(e5, e6))
		self.next_slide()
		self.play(Transform(e5, e7))