from manim import *

class MultiMobjectFadeInAndOut(Scene):
    def construct(self):
        circles = [Circle(r / 10) for r in range(10)]
        circlesb = [Circle(r / 10) for r in range(10)]

        anims_in = [FadeIn(c) for c in circles]
        anims_out = [FadeOut(c) for c in circlesb]
        anims_t = [ReplacementTransform(anims_in[i],anims_out[i],lag_ratio=0.1) for i in range(10)]
        self.play(*anims_t)


