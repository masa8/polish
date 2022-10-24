from manim import *
import yaml




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

        data = {}

        # czasownik_list = []
        # czasownik = {'words':['ja', 'my', 'ty', 'wy', 'on', 'ono', 'ona', 'oni', 'one', ''], 'indicate':None, 'fadeout':None}
        # czasownik2 = {'words':['ja', 'my', 'ty', 'wy', 'on', 'ono', 'ona', 'oni', 'one', 'Ja jem jabłka.'], 'indicate':9,'fadeout':None}
        # czasownik3 = {'words':['Ja', 'my', 'ty', 'wy', 'on', 'ono', 'ona', 'oni', 'one', 'Ja jem jabłka.'], 'indicate':0,'fadeout':None}
        # czasownik4 = {'words':['jem', 'jemy', 'jesz', 'jecie', 'je', 'je', 'je', 'jedzą', 'jedzą', 'Ja jem jabłka.'], 'indicate':0,'fadeout':None}
        # czasownik5 = {'words':['', '', '', '', '', 'jabłko', '', '', 'jabłka', 'Ja jem jabłka.'], 'indicate':None,'fadeout':[5,8]}
        # czasownik_list.append(czasownik)
        # czasownik_list.append(czasownik2)
        # czasownik_list.append(czasownik3)
        # czasownik_list.append(czasownik4)
        # czasownik_list.append(czasownik5)
        # data['pages']=czasownik_list
        #
        # apple = []
        # czasownik_apple = {'czasownik':['jabłko', 'jabłka', 'jabłku', 'jabłko', 'jabłkiem', 'jabłku', 'jabłko'], 'location':5, 'indicate':None}
        # czasownik_apples = {'czasownik':['jabłka', 'jabłek', 'jabłkom', 'jabłka', 'jabłkami', 'jabłkach', 'jabłka'], 'location':8, 'indicate':True}
        # apple.append(czasownik_apple)
        # apple.append(czasownik_apples)
        # data['changes'] = apple
        give_file = input("enter a file name: ")

        with open(give_file, 'r') as stream:
            data = yaml.safe_load(stream)

        czasowniks, locations = [], []
        czasowniks.extend([list(i['czasownik'].values()) for i in data['changes']])
        locations.extend([i['location'] for i in data['changes']])

        for i, page in enumerate(data['pages']):
            if i == 0:
                self.zaimek(page['words'])
                if page['indicate'] is not None:
                    self.play(Indicate(self.uis[page['indicate']]['txt'], scale_factor=3),
                              Flash(self.uis[page['indicate']]['txt'], num_lines=12, color=YELLOW))
                if page['fadeout'] is not None:
                    self.play(*[FadeOut(self.uis[ind]['txt']) for ind in page['fadeout']])
            else:

                self.update_zaimek(page['words'])
                if page['indicate'] is not None:
                    self.play(Indicate(self.uis[page['indicate']]['txt'], scale_factor=3),
                              Flash(self.uis[page['indicate']]['txt'], num_lines=12, color=YELLOW))
                if page['fadeout'] is not None:
                    self.play(*[FadeOut(self.uis[ind]['txt']) for ind in page['fadeout']])

        self.czasownik(czasowniks, locations)

        fadeins, indflush = [],[]
        for li in data['changes']:
            if li['indicate'] is not None:

                direction: np.array = self.resolve_direction(li['indicate'] )
                print(direction, self.uis[li['location']]['txt'])
                fadeins.append(FadeIn(self.uis[li['location']]['txt'], shift=5*direction))
                indflush.append(Indicate(self.uis[li['location']]['txt'], scale_factor=3))
                indflush.append(Flash(self.uis[li['location']]['txt'], num_lines=12, color=YELLOW))
            else:
                FadeIn(self.uis[li['location']]['txt'])
        self.play(*fadeins)

        self.play(*indflush)

    def czasownik(self, czasowniks, locations):

        apples_list = []
        for item, location in zip(czasowniks, locations):
            apples = [Text(item[i]).move_to(self.uis[location]['box'].get_center()) for i in range(7)]
            apples_list.append(apples)

        effects = [{'scale': 1, 'shift': 5 * DL},
                   {'scale': 1, 'shift': 5 * DOWN},
                   {'scale': 1, 'shift': 5 * RIGHT},
                   {'scale': 1, 'shift': 5 * LEFT},
                   {'scale': 1, 'shift': 5 * UP},
                   {'scale': 1, 'shift': 5 * UR},
                   {'scale': 1, 'shift': 5 * UL},
                   ]
        for i, label in enumerate(effects):
            self.play(AnimationGroup(
                *[FadeIn(apples_list[j][i], scale=label['scale'], shift=label['shift'], run_time=0.3) for j in
                  range(len(apples_list))], lag_ratio=0.2))

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

    def resolve_direction(self, direction_string) -> np.ndarray:
        direct_dict = {'mianownik': DL, "dopełniacz": DOWN, "celownik": RIGHT, "biernik": LEFT, "narzędnik": UP, "miejscownik": UR, "wołacz": UL}
        return direct_dict[direction_string]
    def update_zaimek(self, czasownik):
        txts = [Text(czasownik[i]).move_to(self.uis[i]['box'].get_center()) for i in range(0, 10)]
        self.play(*[Transform(self.uis[i]['txt'], target_mobject=txts[i]) for i in range(0, 10)])
