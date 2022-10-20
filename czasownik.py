from manim import *


class JęzykaPolskiego(Scene):

    def __init__(
            self,
            renderer=None,
            camera_class=Camera,
            always_update_mobjects=False,
            random_seed=None,
            skip_animations=False,
    ):
        super().__init__(renderer, camera_class, always_update_mobjects, random_seed, skip_animations)

        self.uis = []
        self.strings = []

    def create_textbox(self, height, width, fill_color, stroke_color, fill_opacity, string):
        result = VGroup()  # create a VGroup
        box_ja = Rectangle(height=height, width=width, fill_color=fill_color, stroke_color=stroke_color,
                           fill_opacity=fill_opacity)
        text = Text(string).move_to(box_ja.get_center())  # create text
        result.add(box_ja, text)  # add both objects to the VGroup
        return result, text, box_ja

    def construct(self):
        czasownik = ['ja', 'my', 'ty', 'wy', 'on', 'ono', 'ona', 'oni', 'one', '']
        czasownik2 = ['ja', 'my', 'ty', 'wy', 'on', 'ono', 'ona', 'oni', 'one', 'Ja jem jabłka.']
        czasownik3 = ['Ja', 'my', 'ty', 'wy', 'on', 'ono', 'ona', 'oni', 'one', 'Ja jem jabłka.']
        czasownik4 = ['jem', 'jemy', 'jesz', 'jecie', 'je', 'je', 'je', 'jedzą', 'jedzą', 'Ja jem jabłka.']
        czasownik5 = ['', '', '', '', '', 'jabłko', '', '', 'jabłka', 'Ja jem jabłka.']

        czasownik_apple = ['jabłko', 'jabłka', 'jabłku', 'jabłko', 'jabłkiem', 'jabłku', 'jabłko']
        czasownik_apples = ['jabłka', 'jabłek', 'jabłkom', 'jabłka', 'jabłkami', 'jabłkach', 'jabłka']
        czasowniks = []
        czasowniks.append(czasownik_apples)
        czasowniks.append(czasownik_apple)

        self.zaimek(czasownik)
        self.update_zaimek(czasownik2)
        self.play(Indicate(self.uis[9]['txt']))

        self.update_zaimek(czasownik3)
        self.play(Indicate(self.uis[0]['txt']))

        self.update_zaimek(czasownik4)
        self.play(Indicate(self.uis[0]['txt']))

        self.update_zaimek(czasownik5)
        self.play(FadeOut(self.uis[8]['txt']), FadeOut(self.uis[5]['txt']))
        self.czasownik(czasowniks, [8, 5])

        self.play(FadeIn(self.uis[8]['txt'], shift=5 * LEFT), FadeIn(self.uis[5]['txt']))
        self.play(Indicate(self.uis[8]['txt']))

    def czasownik(self, czasowniks, locations):

        apples_list = []
        for item, location in zip(czasowniks, locations):
            apples = [Text(item[i]).move_to(self.uis[location]['box'].get_center()) for i in range(7)]
            apples_list.append(apples)

        for i, label in enumerate([{'scale': 10, 'shift': 2 * DL},
                                   {'scale': 10, 'shift': 2 * DOWN},
                                   {'scale': 10, 'shift': 2 * RIGHT},
                                   {'scale': 10, 'shift': 2 * LEFT},
                                   {'scale': 10, 'shift': 2 * UP},
                                   {'scale': 10, 'shift': 2 * UR},
                                   {'scale': 10, 'shift': 2 * UL},
                                   ]):
            self.play(*[FadeIn(apples_list[j][i], shift=label['shift'], run_time=0.3) for j in range(len(apples_list))])
            self.play(*[FadeOut(apples_list[j][i], run_time=0.1) for j in range(len(apples_list))])

    def zaimek(self, czasownik):
        self.strings.clear()
        self.strings.extend(czasownik)
        group, txt, box = self.create_textbox(height=1,
                                              width=6.2,
                                              fill_color=BLACK,
                                              stroke_color=WHITE,
                                              fill_opacity=1,
                                              string=czasownik[0])
        self.uis.append({'group': group, 'txt': txt, 'box': box})

        group, txt, box = self.create_textbox(height=1,
                                              width=6.2,
                                              fill_color=BLACK,
                                              stroke_color=WHITE,
                                              fill_opacity=1,
                                              string=czasownik[1])
        self.uis.append({'group': group, 'txt': txt, 'box': box})

        group, txt, box = self.create_textbox(height=1,
                                              width=6.2,
                                              fill_color=BLACK,
                                              stroke_color=WHITE,
                                              fill_opacity=1,
                                              string=czasownik[2])
        self.uis.append({'group': group, 'txt': txt, 'box': box})

        group, txt, box = self.create_textbox(height=1,
                                              width=6.2,
                                              fill_color=BLACK,
                                              stroke_color=WHITE,
                                              fill_opacity=1,
                                              string=czasownik[3])
        self.uis.append({'group': group, 'txt': txt, 'box': box})
        group, txt, box = self.create_textbox(height=1,
                                              width=4,
                                              fill_color=BLACK,
                                              stroke_color=WHITE,
                                              fill_opacity=1,
                                              string=czasownik[4])
        self.uis.append({'group': group, 'txt': txt, 'box': box})
        group, txt, box = self.create_textbox(height=1,
                                              width=4,
                                              fill_color=BLACK,
                                              stroke_color=WHITE,
                                              fill_opacity=1,
                                              string=czasownik[5])
        self.uis.append({'group': group, 'txt': txt, 'box': box})
        group, txt, box = self.create_textbox(height=1,
                                              width=4,
                                              fill_color=BLACK,
                                              stroke_color=WHITE,
                                              fill_opacity=1,
                                              string=czasownik[6])
        self.uis.append({'group': group, 'txt': txt, 'box': box})
        group, txt, box = self.create_textbox(height=1,
                                              width=6.2,
                                              fill_color=BLACK,
                                              stroke_color=WHITE,
                                              fill_opacity=1,
                                              string=czasownik[7])
        self.uis.append({'group': group, 'txt': txt, 'box': box})
        group, txt, box = self.create_textbox(height=1,
                                              width=6.2,
                                              fill_color=BLACK,
                                              stroke_color=WHITE,
                                              fill_opacity=1,
                                              string=czasownik[8])
        self.uis.append({'group': group, 'txt': txt, 'box': box})
        group, txt, box = self.create_textbox(height=1,
                                              width=12.4,
                                              fill_color=BLACK,
                                              stroke_color=BLACK,
                                              fill_opacity=0,
                                              string=czasownik[9])
        self.uis.append({'group': group, 'txt': txt, 'box': box})

        g1 = VGroup(self.uis[0]['group'], self.uis[1]['group']).arrange(RIGHT)
        g2 = VGroup(self.uis[2]['group'], self.uis[3]['group']).arrange(RIGHT)
        g3 = VGroup(self.uis[4]['group'], self.uis[5]['group'], self.uis[6]['group']).arrange(RIGHT)
        g4 = VGroup(self.uis[7]['group'], self.uis[8]['group']).arrange(RIGHT)
        gt = VGroup(self.uis[9]['group'])

        ga = VGroup(g1, g2, g3, g4, gt).arrange(UP)
        self.play(Write(ga), run_time=0.5)

    def update_zaimek(self, czasownik):
        txts = [Text(czasownik[i]).move_to(self.uis[i]['box'].get_center()) for i in range(0, 10)]
        self.play(*[Transform(self.uis[i]['txt'], target_mobject=txts[i]) for i in range(0, 10)])
