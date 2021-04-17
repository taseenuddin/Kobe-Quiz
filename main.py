import os, sys
from kivy.resources import resource_add_path, resource_find


import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
import os.path
from kivy.resources import resource_add_path
from kivy.clock import Clock


class FrontScreen(Screen):
    pass


class Question1(Screen):
    pass

class Question2(Screen):
    pass

class Question3(Screen):
    pass

class Question4(Screen):
    pass

class Question5(Screen):
    pass

class Question6(Screen):
    pass

class Question7(Screen):
    pass

class Question8(Screen):
    pass

class Question9(Screen):
    pass

class Question10(Screen):
    pass
class Screenlist(ScreenManager):
    pass

class WrongAnswer(Screen):
    pass

class Youwon(Screen):
    pass




class MyApp(App):
    def build(self):

        self.sound = SoundLoader.load('music/Trapsax.mp3')
        self.sound.loop = True
        self.sound.play()
        return Builder.load_string(
            '''
Screenlist:
    FrontScreen:
    Question1:
    WrongAnswer:
    Question2:
    Question3:
    Question4:
    Question5:
    Question6:
    Question7:
    Question8:
    Question9:
    Question10:
    Youwon:




<FrontScreen>:
    name: "one"

    GridLayout:
        cols:1
        size: root.width, root.height


        GridLayout:
            cols:1
            Label:
                text:"Welcome to The Kobe Bryant Quiz!"
                font_size: "30"

            Button:
                text:"Begin"
                on_press:app.root.current = "second"
                font_size: "50"
                GridLayout:
                    rows:2
                    Image:

                        source: 'Images/KobeLogo.png'
                        allow_stretch: True
                        keep_ratio: True


<Question1>:
    name:"second"
    GridLayout:
        cols:2

        Label:
            text: "1.What year was Kobe Bryant Drafted?"

            font_size:20
            bold : True
        Image:
            source: 'Images/Kobe_getting_drafted.jpg'
            size: self.texture_size
            allow_stretch:True
            keep_ratio : True









            GridLayout:
                cols:4
                size:root.width ,root.height-600
                Button:
                    text:"1997"
                    on_press:app.root.current = "third"

                    on_release:
                        root.manager.transition.direction = "right"


                Button:
                    text:"1998"
                    on_press:app.root.current = "third"

                    on_release:
                        root.manager.transition.direction = "right"
                Button:
                    text:"1999"
                    on_press:app.root.current = "third"

                    on_release:
                        root.manager.transition.direction = "right"







                Button:
                    text:"1996"
                    on_press:app.root.current = "fourth"


                    on_release:
                        root.manager.transition.direction = "right"






<WrongAnswer>:
    name:"third"
    GridLayout:
        cols:1
        size: root.width, root.height-400
        Label:
            text:"Wrong Answer!"
            font_size:80


        GridLayout:
            rows:1
            size: root.width-300, root.height - 500


            Button:
                text:"Retry?"
                on_press:app.root.current = "second"

                on_release:
                    root.manager.transition.direction = "right"
            Button:
                text:"Exit Quiz?"
                on_press:app.root.current = "one"

                on_release:
                    root.manager.transition.direction = "right"


<Question2>:
    name: "fourth"
    GridLayout:
        cols:2
        size:root.width+500,root.height+500
        Label:
            text: "2. What team did rookie Kobe Bryant infamously choke against in the 1997 playoffs?"
            text_size:self.size
            font_size:20
            bold : True
        Image:
            source: 'Images/Kobe1997.jpg'

            allow_stretch:True
            keep_ratio : True










        GridLayout:
            cols:2
            Label:
                text: ""
                font_size:25
                GridLayout:
                    cols:4
                    size:root.width ,root.height-600
                    Button:
                        text:"Suns"
                        on_press:app.root.current = "third"

                        on_release:
                            root.manager.transition.direction = "right"


                    Button:
                        text:"Clippers"
                        on_press:app.root.current = "third"

                        on_release:
                            root.manager.transition.direction = "right"
                    Button:
                        text:"Jazz"
                        on_press:app.root.current = "fifth"

                        on_release:
                            root.manager.transition.direction = "left"





                    Button:
                        text:"Timberwolves"
                        on_press:app.root.current = "third"


                        on_release:
                            root.manager.transition.direction = "right"

<Question3>:
    name: "fifth"
    GridLayout:
        cols:2
        size:root.width+500,root.height+500
        Label:
            text:"3. How much points per game did Kobe Bryant average for his career?"
            text_size:self.size
            font_size:20
            bold : True

        Image:
            source: 'Images/Kobeppg.jpg'

            allow_stretch:True
            keep_ratio : True

        GridLayout:
            cols:2
            Label:
                text: ""
                font_size:25
                GridLayout:
                    cols:4
                    size:root.width ,root.height-600
                    Button:
                        text:"22"
                        on_press:app.root.current = "third"

                        on_release:
                            root.manager.transition.direction = "right"


                    Button:
                        text:"23"
                        on_press:app.root.current = "third"

                        on_release:
                            root.manager.transition.direction = "right"
                    Button:
                        text:"25"
                        on_press:app.root.current = "seventh"

                        on_release:
                            root.manager.transition.direction = "left"





                    Button:
                        text:"27"
                        on_press:app.root.current = "third"


                        on_release:
                            root.manager.transition.direction = "right"




<Question4>
    name: "seventh"
    GridLayout:
        cols:2
        size:root.width+500,root.height+500
        Label:
            text:"4. What years did Kobe commit a threepeat? (a span of 3 years with consecutive championships)"
            text_size:self.size
            font_size:20
            bold : True
        Image:
            source: 'Images/Kobeandshaq.jpg'

            allow_stretch:True
            keep_ratio : True


        GridLayout:
            cols:2
            Label:
                text: ""
                font_size:20
                GridLayout:
                    cols:4
                    size:root.width ,root.height-600
                    Button:
                        text:"2001-2003"
                        on_press:app.root.current = "eight"

                        on_release:
                            root.manager.transition.direction = "left"


                    Button:
                        text:"2004-2006"
                        on_press:app.root.current = "third"

                        on_release:
                            root.manager.transition.direction = "right"
                    Button:
                        text:"1996-1998"
                        on_press:app.root.current = "third"

                        on_release:
                            root.manager.transition.direction = "right"





                    Button:
                        text:"2000-2002"
                        on_press:app.root.current = "third"


                        on_release:
                            root.manager.transition.direction = "right"


<Question5>
    name: "eight"
    GridLayout:
        cols:2
        size:root.width+500,root.height+500

        Label:
            text:"5. What company is the shoebrand that Kobe Bryant INITIALLY signed with coming to the NBA?"
            text_size:self.size
            font_size:20
            bold : True
        Image:
            source: 'Images/Kobeshoes.jpg'

            allow_stretch:True
            keep_ratio : True


        GridLayout:
            cols:2
            Label:
                text: ""
                font_size:25
                GridLayout:
                    cols:4
                    size:root.width ,root.height-600
                    Button:
                        text:"Nike"
                        on_press:app.root.current = "eight"

                        on_release:
                            root.manager.transition.direction = "right"


                    Button:
                        text:"Reebok"
                        on_press:app.root.current = "third"

                        on_release:
                            root.manager.transition.direction = "right"
                    Button:
                        text:"Puma"
                        on_press:app.root.current = "third"

                        on_release:
                            root.manager.transition.direction = "right"





                    Button:
                        text:"Adidas"
                        on_press:app.root.current = "ninth"


                        on_release:
                            root.manager.transition.direction = "left"
<Question6>
    name: "ninth"
    GridLayout:

        cols:2
        size:root.width+500,root.height+500
        Label:
            text:"6. Who is the only player Kobe Bryant admitted he never figured out how to stop?"
            text_size:self.size
            font_size:20
            bold : True
        Image:
            source: 'Images/kobeandkd.jpg'

            allow_stretch:True
            keep_ratio : True


        GridLayout:
            cols:2
            Label:
                text: ""
                font_size:25
                GridLayout:
                    cols:4
                    size:root.width ,root.height-600
                    Button:
                        text:"Kevin Durant"
                        on_press:app.root.current = "tenth"

                        on_release:
                            root.manager.transition.direction = "right"


                    Button:
                        text:"Lebron James"
                        on_press:app.root.current = "third"

                        on_release:
                            root.manager.transition.direction = "right"
                    Button:
                        text:"Michael Jordan"
                        on_press:app.root.current = "third"

                        on_release:
                            root.manager.transition.direction = "right"





                    Button:
                        text:"Tracy Mcgrady"
                        on_press:app.root.current = "third"


                        on_release:
                            root.manager.transition.direction = "right"
<Question7>
    name: "tenth"
    GridLayout:
        cols:2
        size:root.width+500,root.height+500
        Label:
            text:"7. What is Kobe Bryants favorite sport?"
            text_size:self.size
            font_size:20
            bold : True

        Image:
            source: 'Images/Kobewatchingsoccer.jpg'

            allow_stretch:True
            keep_ratio : True


        GridLayout:
            cols:2
            Label:
                text: ""
                font_size:25
                GridLayout:
                    cols:4
                    size:root.width ,root.height-600
                    Button:
                        text:"American Football"
                        on_press:app.root.current = "third"

                        on_release:
                            root.manager.transition.direction = "right"


                    Button:
                        text:"Soccer"
                        on_press:app.root.current = "eleventh"

                        on_release:
                            root.manager.transition.direction = "left"
                    Button:
                        text:"Tennis"
                        on_press:app.root.current = "third"

                        on_release:
                            root.manager.transition.direction = "right"





                    Button:
                        text:"Golf"
                        on_press:app.root.current = "third"


                        on_release:
                            root.manager.transition.direction = "right"

<Question8>
    name: "eleventh"
    GridLayout:
        cols:2
        size:root.width+500,root.height+500
        Label:
            text:"8. Which one of these records does Kobe Bryant hold?"
            text_size:self.size
            font_size:20
            bold : True
        Image:
            source: 'Images/timmyandkobe.jpg'

            allow_stretch:True
            keep_ratio : True


        GridLayout:
            cols:2
            Label:
                text: ""
                font_size:25
                GridLayout:
                    cols:4
                    size:root.width ,root.height-600
                    Button:
                        text:"2nd highest points scored in an nba game"
                        on_press:app.root.current = "third"

                        on_release:
                            root.manager.transition.direction = "right"


                    Button:
                        text:"Youngest ever NBA all star"
                        on_press:app.root.current = "eleventh"

                        on_release:
                            root.manager.transition.direction = "right"
                    Button:
                        text:"Youngest player to be drafted to the NBA"
                        on_press:app.root.current = "third"

                        on_release:
                            root.manager.transition.direction = "right"





                    Button:
                        text:"All of the above"
                        on_press:app.root.current = "twelfth"


                        on_release:
                            root.manager.transition.direction = "left"

<Question9>
    name: "twelfth"
    GridLayout:
        cols:2
        size:root.width+500,root.height+500
        Label:
            text:"9. What year did Kobe Bryant end off his hall of fame career ?"
            text_size:self.size
            font_size:20
            bold : True

        Image:
            source: 'Images/Farewell.webp'

            allow_stretch:True
            keep_ratio : True




        GridLayout:
            cols:2
            Label:
                text: ""
                font_size:25
                GridLayout:
                    cols:4
                    size:root.width ,root.height-600
                    Button:
                        text:"2016"
                        on_press:app.root.current = "final"

                        on_release:
                            root.manager.transition.direction = "left"


                    Button:
                        text:"2013"
                        on_press:app.root.current = "third"

                        on_release:
                            root.manager.transition.direction = "right"
                    Button:
                        text:"2015"
                        on_press:app.root.current = "third"

                        on_release:
                            root.manager.transition.direction = "right"





                    Button:
                        text:"2012"
                        on_press:app.root.current = "third"


                        on_release:
                            root.manager.transition.direction = "right"




<Question10>
    name: "final"
    GridLayout:
        cols:2
        size:root.width+500,root.height+500
        Label:
            text:"10. Who is the greatest Los Angeles Laker of all time? (unanimously decided by hall of fame lakers players)"
            text_size:self.size
            font_size:20
            bold : True

        Image:
            source: 'Images/KobeandJordan.webp'

            allow_stretch:True
            keep_ratio : True


        GridLayout:
            cols:2
            Label:
                text: ""
                font_size:20
                GridLayout:
                    cols:4
                    size:root.width ,root.height-600
                    Button:
                        text:"Kobe Bryant"
                        on_press:app.root.current = "congrats"

                        on_release:
                            root.manager.transition.direction = "left"


                    Button:
                        text:"Derek Fisher"
                        on_press:app.root.current = "third"

                        on_release:
                            root.manager.transition.direction = "right"
                    Button:
                        text:"Lonzo Ball"
                        on_press:app.root.current = "third"

                        on_release:
                            root.manager.transition.direction = "right"





                    Button:
                        text:"Kyle Kuzma"
                        on_press:app.root.current = "third"


                        on_release:
                            root.manager.transition.direction = "right"

<Youwon>
    name:"congrats"
    GridLayout:
        rows:4
        Label:
            text: "Congratulations you have beaten the Kobe Quiz! Now get motivated and unleash your inner black mamba!"
            font_size: 15
        Image:
            source: 'Images/kobe-960x542.jpg'
            GridLayout:
                cols:2
                Button:
                    text:"Main Screen"
                    on_press:app.root.current = "one"
                    font_size:12
                    text_size:self.size
                Button:
                    text:"Exit App"
                    font_size:12
                    text_size:self.size
                    on_press:app.root.current = App.get_running_app().stop()


'''
        )







if __name__ == "__main__":
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    MyApp().run()
