from manim import *
import json
import yaml


class JęzykaPolskiego(Scene):

    def przypadek(self, data):
        for item in data:
            m1 = Text(item[0]['t'], t2c={item[0]['c']: RED}).scale(5)
            m2 = Text(item[1]['t'], t2c={item[1]['c']: RED}).scale(5)
            m3 = Text(item[2]['t'], t2c={item[2]['c']: BLUE}).scale(5)
            m4 = Text(item[3]['t'], t2c={item[3]['c']: YELLOW}).scale(5)
            m5 = Text(item[4]['t'], t2c={item[4]['c']: GREEN}).scale(5)
            m6 = Text(item[5]['t'], t2c={item[5]['c']: PINK}).scale(5)

            self.play(FadeIn(m1))
            self.play(FadeOut(m1, scale=10))

            self.play(FadeIn(m2, shift=DOWN), run_time=1)
            self.play(FadeOut(m2))

            self.play(FadeIn(m3, shift=RIGHT), run_time=1)
            self.play(FadeOut(m3))

            self.play(FadeIn(m4, shift=LEFT), run_time=1)
            self.play(FadeOut(m4))

            self.play(FadeIn(m5, shift=UP), run_time=1)
            self.play(FadeOut(m5))

            self.play(FadeIn(m6, scale=3.0), run_time=1)
            self.play(FadeOut(m6))

    def construct(self):
        self.camera.background_color = BLACK
        with open("data.yml", 'r') as stream:
            data = yaml.safe_load(stream)

        self.przypadek(data)
