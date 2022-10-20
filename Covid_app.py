from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from funkcje import smierc, zycie
import pandas as pd
import pickle
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup


#### Pytania ####

## Strona pierwsza

class app(App):
    def build(self):
        self.screen_manager = ScreenManager()

        
        scroll_height = 0;
        blmain = Widget()
        blmain.add_widget(Image(source = "background.jpg", size = Window.size, allow_stretch = True, keep_ratio = False))

        screen0 = Screen(name= 'start')

        blbtns = BoxLayout(
            orientation = 'vertical'
            )
                   #size_hint = (1, None),

        blbtns.bind(minimum_height = blbtns.setter('height'))

        button0=Button(
            text='Chciałbym(abym) poznać prawdopodobieństwo, że umrę na Covid-19',background_color =(0, 0, 0,0.5 )
            )
        if (scroll_height < (Window.height / 2)):
            scroll_height = scroll_height + 40  


        button01=Button(
            text='Chciałbym(abym) poznać prawdopodobieństwo, że jestem chory(a) na Covid-19',background_color =(0, 0, 0,0.5 )
            )
        if (scroll_height < (Window.height / 2)):
            scroll_height = scroll_height + 40   

        button0.bind(on_release=self.btn00)
        button01.bind(on_release=self.btn01)

        blbtns.add_widget(button0)
        blbtns.add_widget(button01)
        

        scrlFBtns = ScrollView(effect_cls = 'ScrollEffect', pos = (0, 0), size = (Window.width, scroll_height)) 

        label = Label(text='Badanie ma dwa zastosowania. Pierwsze polega na oszacowaniu prawdopodobieństwa, \nże po ciężkim przejściu (hospitalizacji) choroby Covid-19 dana osoba umrze. \nDrugie natomiast na podstawie podanych symptomów oszacowuje prawdopodobieństwo, \nże badana osoba jest chora na Covid-19. Aby rozpocząć badanie proszę wybrać jedną z poniższych opcji.', size_hint=(1, None), halign = 'center', y = (Window.height * 0.75), width = Window.width, color=(0,0,0,1))
        label.bind(
        texture_size=lambda *x: label.setter('height')(label, label.texture_size[1]))

        scrlFBtns.add_widget(blbtns)
        lblmain = Label(text = 'Badanie ma dwa zastosowania. Pierwsze polega na oszacowaniu prawdopodobieństwa, \nże po ciężkim przejściu (hospitalizacji) choroby Covid-19  dana osoba umrze. \nDrugie natomiast na podstawie podanych symptomów oszacowuje prawdopodobieństwo, że badana osoba jest chora na Covid-19.\n Aby rozpocząć badanie proszę wybrać jedną z poniższych opcji.', text_size = blmain.size , halign = 'center', y = (Window.height * 0.75), width = Window.width, color=(0,0,0,1))

        blmain.add_widget(label)
        blmain.add_widget(scrlFBtns)
        screen0.add_widget(blmain)
        self.screen_manager.add_widget(screen0)





        #Pytania do prawdpodobieństwa śmierci
        blmain = Widget()
        blmain.add_widget(Image(source = "background.jpg", size = Window.size, allow_stretch = True, keep_ratio = False))
        screen1=Screen(name='sex')
        layout = BoxLayout(orientation='vertical',)
        button10 = Label(text="Płeć",color=(0,0,0,1))
        button11 = Button(text="Mężczyzna",background_color =(0, 0, 0, 0.5),color=(0,0,0,1))
        button12 = Button(text='Kobieta',background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        button11.bind(on_release=self.btn11)
        button12.bind(on_release=self.btn12)
        layout.add_widget(blmain)
        layout.add_widget(button10)
        layout.add_widget(button11)
        layout.add_widget(button12)
        screen1.add_widget(layout)
        self.screen_manager.add_widget(screen1)

        screen2=Screen(name='Astma')
        blmain = Widget()
        blmain.add_widget(Image(source = "background.jpg", size = Window.size, allow_stretch = True, keep_ratio = False))
        layout = BoxLayout(orientation='vertical')
        button20 = Label(text="Czy chorujesz na astmę?",color=(0,0,0,1))
        button21 = Button(text="Tak",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        button22 = Button(text="Nie",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        button21.bind(on_release=self.btn21)
        button22.bind(on_release=self.btn22)
        layout.add_widget(blmain)
        layout.add_widget(button20)
        layout.add_widget(button21)
        layout.add_widget(button22)
        screen2.add_widget(layout)
        self.screen_manager.add_widget(screen2)

        screen3=Screen(name='Cukrzyca')
        blmain = Widget()
        blmain.add_widget(Image(source = "background.jpg", size = Window.size, allow_stretch = True, keep_ratio = False))
        layout = BoxLayout(orientation='vertical')
        button30 = Label(text="Czy chorujesz na cukrzycę?",color=(0,0,0,1))
        button31 = Button(text="Tak",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        button32 = Button(text="Nie",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        button31.bind(on_release=self.btn31)
        button32.bind(on_release=self.btn32)
        layout.add_widget(blmain)
        layout.add_widget(button30)
        layout.add_widget(button31)
        layout.add_widget(button32)
        screen3.add_widget(layout)
        self.screen_manager.add_widget(screen3)

        screen4=Screen(name='Pluca')
        blmain = Widget()
        blmain.add_widget(Image(source = "background.jpg", size = Window.size, allow_stretch = True, keep_ratio = False))
        layout = BoxLayout(orientation='vertical')
        button40 = Label(text="Czy chorujesz na przewlekłą obturacyjną chorobę płuc?",color=(0,0,0,1))
        button41 = Button(text="Tak",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        button42 = Button(text="Nie",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        button41.bind(on_release=self.btn41)
        button42.bind(on_release=self.btn42)
        layout.add_widget(blmain)
        layout.add_widget(button40)
        layout.add_widget(button41)
        layout.add_widget(button42)
        screen4.add_widget(layout)
        self.screen_manager.add_widget(screen4)

        screen5=Screen(name='leki')
        blmain = Widget()
        blmain.add_widget(Image(source = "background.jpg", size = Window.size, allow_stretch = True, keep_ratio = False))
        layout = BoxLayout(orientation='vertical')
        button50 = Label(text="Czy przyjmujesz leki immunosupresyjne?",color=(0,0,0,1))
        button51 = Button(text="Tak",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        button52 = Button(text="Nie",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        button51.bind(on_release=self.btn51)
        button52.bind(on_release=self.btn52)
        layout.add_widget(blmain)
        layout.add_widget(button50)
        layout.add_widget(button51)
        layout.add_widget(button52)
        screen5.add_widget(layout)
        self.screen_manager.add_widget(screen5)

        screen6=Screen(name='tetnice')
        blmain = Widget()
        blmain.add_widget(Image(source = "background.jpg", size = Window.size, allow_stretch = True, keep_ratio = False))
        layout = BoxLayout(orientation='vertical')
        button60 =Label(text="Czy masz nadciśnienie tętnicze?",color=(0,0,0,1))
        button61 = Button(text="Tak",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        button62 = Button(text="Nie",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        button61.bind(on_release=self.btn61)
        button62.bind(on_release=self.btn62)
        layout.add_widget(blmain)
        layout.add_widget(button60)
        layout.add_widget(button61)
        layout.add_widget(button62)
        screen6.add_widget(layout)
        self.screen_manager.add_widget(screen6)

        screen7=Screen(name='nadwaga')
        blmain = Widget()
        blmain.add_widget(Image(source = "background.jpg", size = Window.size, allow_stretch = True, keep_ratio = False))
        layout = BoxLayout(orientation='vertical')
        button70 = Label(text="Czy masz nadwagę?",color=(0,0,0,1))
        button71 = Button(text="Tak",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        button72 = Button(text="Nie",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        button71.bind(on_release=self.btn71)
        button72.bind(on_release=self.btn72)
        layout.add_widget(blmain)
        layout.add_widget(button70)
        layout.add_widget(button71)
        layout.add_widget(button72)
        screen7.add_widget(layout)
        self.screen_manager.add_widget(screen7)

        screen8=Screen(name='nerki')
        blmain = Widget()
        blmain.add_widget(Image(source = "background.jpg", size = Window.size, allow_stretch = True, keep_ratio = False))
        layout = BoxLayout(orientation='vertical')
        button80 = Label(text="Czy masz przewlekłą niewydolność nerek?",color=(0,0,0,1))
        button81 = Button(text="Tak",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        button82 = Button(text="Nie",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        button81.bind(on_release=self.btn81)
        button82.bind(on_release=self.btn82)
        layout.add_widget(blmain)
        layout.add_widget(button80)
        layout.add_widget(button81)
        layout.add_widget(button82)
        screen8.add_widget(layout)
        self.screen_manager.add_widget(screen8)

        screen9=Screen(name='papierosy')
        blmain = Widget()
        blmain.add_widget(Image(source = "background.jpg", size = Window.size, allow_stretch = True, keep_ratio = False))
        layout = BoxLayout(orientation='vertical')
        button90 = Label(text="Czy jesteś palaczem?",color=(0,0,0,1))
        button91 = Button(text="Tak",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        button92 = Button(text="Nie",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        button91.bind(on_release=self.btna91)
        button92.bind(on_release=self.btna92)
        layout.add_widget(blmain)
        layout.add_widget(button90)
        layout.add_widget(button91)
        layout.add_widget(button92)
        screen9.add_widget(layout)
        self.screen_manager.add_widget(screen9)

        screena10=Screen(name='serce')
        blmain = Widget()
        blmain.add_widget(Image(source = "background.jpg", size = Window.size, allow_stretch = True, keep_ratio = False))
        layout = BoxLayout(orientation='vertical')
        buttona100 = Label(text="Czy chorujesz na choroby sercowo naczyniowe?",color=(0,0,0,1))
        buttona101 = Button(text="Tak",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        buttona102 = Button(text="Nie",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        buttona101.bind(on_release=self.btn91)
        buttona102.bind(on_release=self.btn92)
        layout.add_widget(blmain)
        layout.add_widget(buttona100)
        layout.add_widget(buttona101)
        layout.add_widget(buttona102)
        screena10.add_widget(layout)
        self.screen_manager.add_widget(screena10)

        screen10=Screen(name='inne')
        blmain = Widget()
        blmain.add_widget(Image(source = "background.jpg", size = Window.size, allow_stretch = True, keep_ratio = False))
        layout = BoxLayout(orientation='vertical')
        button100 = Label(text="Czy chorujesz na inna poważną chorobę oprócz wymienionych powyżej?",color=(0,0,0,1))
        button101 = Button(text="Tak",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        button102 = Button(text="Nie",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        button101.bind(on_release=self.btn101)
        button102.bind(on_release=self.btn102)
        layout.add_widget(blmain)
        layout.add_widget(button100)
        layout.add_widget(button101)
        layout.add_widget(button102)
        screen10.add_widget(layout)
        self.screen_manager.add_widget(screen10)

        

        screen11=Screen(name='wiek')
        blmain = Widget()
        blmain.add_widget(Image(source = "background.jpg", size = Window.size, allow_stretch = True, keep_ratio = False))
        layout = BoxLayout(orientation='vertical')
        button110 = Label(text="wiek",color=(0,0,0,1))
        textinput = TextInput(multiline=False, input_filter = "int")
        button112 = Button(text="Poznaj wynik",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        button112.bind(on_release=self.btn110)
        layout.add_widget(blmain)
        layout.add_widget(button110)
        layout.add_widget(textinput)
        layout.add_widget(button112)
        screen11.add_widget(layout)
        self.screen_manager.add_widget(screen11)


        screen12=Screen(name='koniec')
        blmain = Widget()
        blmain.add_widget(Image(source = "background.jpg", size = Window.size, allow_stretch = True, keep_ratio = False))
        layout = BoxLayout(orientation='vertical')
        button120 = Label(text="Twoje prawdopodobieństwo śmierci wynosi:",color=(0,0,0,1))
        button121 = Button(background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        self.wyniki2=button121
        button122 = Button(text="Zacznij od poczatku",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        button122.bind(on_release=self.btn120)
        layout.add_widget(blmain)
        layout.add_widget(button120)
        layout.add_widget(button121)
        layout.add_widget(button122)
        screen12.add_widget(layout)
        self.screen_manager.add_widget(screen12)

        # pytania do życia 

        screen13=Screen(name='Breathing')
        blmain = Widget()
        blmain.add_widget(Image(source = "background.jpg", size = Window.size, allow_stretch = True, keep_ratio = False))
        layout = BoxLayout(orientation='vertical')
        buttonx10 = Label(text="Czy masz problemy z oddychaniem?",color=(0,0,0,1))
        buttonx11 = Button(text="Tak",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        buttonx12 = Button(text='Nie',background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        buttonx11.bind(on_release=self.btnx11)
        buttonx12.bind(on_release=self.btnx12)
        layout.add_widget(blmain)
        layout.add_widget(buttonx10)
        layout.add_widget(buttonx11)
        layout.add_widget(buttonx12)
        screen13.add_widget(layout)
        self.screen_manager.add_widget(screen13)

        screen14=Screen(name='Cold')
        blmain = Widget()
        blmain.add_widget(Image(source = "background.jpg", size = Window.size, allow_stretch = True, keep_ratio = False))
        layout = BoxLayout(orientation='vertical')
        buttonx20 = Label(text="Czy masz gorączkę?",color=(0,0,0,1))
        buttonx21 = Button(text="Tak",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        buttonx22 = Button(text="Nie",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        buttonx21.bind(on_release=self.btnx21)
        buttonx22.bind(on_release=self.btnx22)
        layout.add_widget(blmain)
        layout.add_widget(buttonx20)
        layout.add_widget(buttonx21)
        layout.add_widget(buttonx22)
        screen14.add_widget(layout)
        self.screen_manager.add_widget(screen14)

        screen15=Screen(name='Cough')
        blmain = Widget()
        blmain.add_widget(Image(source = "background.jpg", size = Window.size, allow_stretch = True, keep_ratio = False))
        layout = BoxLayout(orientation='vertical')
        buttonx30 = Label(text="Czy masz suchy kaszel?",color=(0,0,0,1))
        buttonx31 = Button(text="Tak",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        buttonx32 = Button(text="Nie",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        buttonx31.bind(on_release=self.btnx31)
        buttonx32.bind(on_release=self.btnx32)
        layout.add_widget(blmain)
        layout.add_widget(buttonx30)
        layout.add_widget(buttonx31)
        layout.add_widget(buttonx32)
        screen15.add_widget(layout)
        self.screen_manager.add_widget(screen15)

        screen16=Screen(name='Throat')
        blmain = Widget()
        blmain.add_widget(Image(source = "background.jpg", size = Window.size, allow_stretch = True, keep_ratio = False))
        layout = BoxLayout(orientation='vertical')
        buttonx40 = Label(text="Czy boli Cię gardło?",color=(0,0,0,1))
        buttonx41 = Button(text="Tak",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        buttonx42 = Button(text="Nie",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        buttonx41.bind(on_release=self.btnx41)
        buttonx42.bind(on_release=self.btnx42)
        layout.add_widget(blmain)
        layout.add_widget(buttonx40)
        layout.add_widget(buttonx41)
        layout.add_widget(buttonx42)
        screen16.add_widget(layout)
        self.screen_manager.add_widget(screen16)

        screen17=Screen(name='Runnynose')
        blmain = Widget()
        blmain.add_widget(Image(source = "background.jpg", size = Window.size, allow_stretch = True, keep_ratio = False))
        layout = BoxLayout(orientation='vertical')
        buttonx50 = Label(text="Czy masz katar?",color=(0,0,0,1))
        buttonx51 = Button(text="Tak",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        buttonx52 = Button(text="Nie",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        buttonx51.bind(on_release=self.btnx51)
        buttonx52.bind(on_release=self.btnx52)
        layout.add_widget(blmain)
        layout.add_widget(buttonx50)
        layout.add_widget(buttonx51)
        layout.add_widget(buttonx52)
        screen17.add_widget(layout)
        self.screen_manager.add_widget(screen17)

        screen20=Screen(name='Head')
        blmain = Widget()
        blmain.add_widget(Image(source = "background.jpg", size = Window.size, allow_stretch = True, keep_ratio = False))
        layout = BoxLayout(orientation='vertical')
        buttonx80 = Label(text="Czy boli Cię głowa?",color=(0,0,0,1))
        buttonx81 = Button(text="Tak",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        buttonx82 = Button(text="Nie",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        buttonx81.bind(on_release=self.btnx81)
        buttonx82.bind(on_release=self.btnx82)
        layout.add_widget(blmain)
        layout.add_widget(buttonx80)
        layout.add_widget(buttonx81)
        layout.add_widget(buttonx82)
        screen20.add_widget(layout)
        self.screen_manager.add_widget(screen20)

        screen21=Screen(name='Heart')
        blmain = Widget()
        blmain.add_widget(Image(source = "background.jpg", size = Window.size, allow_stretch = True, keep_ratio = False))
        layout = BoxLayout(orientation='vertical')
        buttonx90 = Label(text="Czy masz chorobę serca?",color=(0,0,0,1))
        buttonx91 = Button(text="Tak",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        buttonx92 = Button(text="Nie",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        buttonx91.bind(on_release=self.btnx91)
        buttonx92.bind(on_release=self.btnx92)
        layout.add_widget(blmain)
        layout.add_widget(buttonx90)
        layout.add_widget(buttonx91)
        layout.add_widget(buttonx92)
        screen21.add_widget(layout)
        self.screen_manager.add_widget(screen21)

        screen22=Screen(name='Diabetes')
        blmain = Widget()
        blmain.add_widget(Image(source = "background.jpg", size = Window.size, allow_stretch = True, keep_ratio = False))
        layout = BoxLayout(orientation='vertical')
        buttonx100 = Label(text="Czy jesteś cukrzykiem?",color=(0,0,0,1))
        buttonx101 = Button(text="Tak",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        buttonx102 = Button(text="Nie",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        buttonx101.bind(on_release=self.btnx101)
        buttonx102.bind(on_release=self.btnx102)
        layout.add_widget(blmain)
        layout.add_widget(buttonx100)
        layout.add_widget(buttonx101)
        layout.add_widget(buttonx102)
        screen22.add_widget(layout)
        self.screen_manager.add_widget(screen22)

        screen23=Screen(name='Hypertension')
        blmain = Widget()
        blmain.add_widget(Image(source = "background.jpg", size = Window.size, allow_stretch = True, keep_ratio = False))
        layout = BoxLayout(orientation='vertical')
        buttonx110 = Label(text="Czy masz nadciśnienie tętnicze?",color=(0,0,0,1))
        buttonx111 = Button(text="Tak",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        buttonx112 = Button(text="Nie",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        buttonx111.bind(on_release=self.btnx111)
        buttonx112.bind(on_release=self.btnx112)
        layout.add_widget(blmain)
        layout.add_widget(buttonx110)
        layout.add_widget(buttonx111)
        layout.add_widget(buttonx112)
        screen23.add_widget(layout)
        self.screen_manager.add_widget(screen23)


        screen26=Screen(name='Abroad')
        blmain = Widget()
        blmain.add_widget(Image(source = "background.jpg", size = Window.size, allow_stretch = True, keep_ratio = False))
        layout = BoxLayout(orientation='vertical')
        buttonx140 = Label(text="Czy byłeś w ostatnim czasie za granicą?",color=(0,0,0,1))
        buttonx141 = Button(text="Tak",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        buttonx142 = Button(text="Nie",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        buttonx141.bind(on_release=self.btnx141)
        buttonx142.bind(on_release=self.btnx142)
        layout.add_widget(blmain)
        layout.add_widget(buttonx140)
        layout.add_widget(buttonx141)
        layout.add_widget(buttonx142)
        screen26.add_widget(layout)
        self.screen_manager.add_widget(screen26)

        screen27=Screen(name='Patient')
        blmain = Widget()
        blmain.add_widget(Image(source = "background.jpg", size = Window.size, allow_stretch = True, keep_ratio = False))
        layout = BoxLayout(orientation='vertical')
        buttonx150 = Label(text="Czy miałeś kontakt z osobą chorą na COVID-19?",color=(0,0,0,1))
        buttonx151 = Button(text="Tak",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        buttonx152 = Button(text="Nie",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        buttonx151.bind(on_release=self.btnx151)
        buttonx152.bind(on_release=self.btnx152)
        layout.add_widget(blmain)
        layout.add_widget(buttonx150)
        layout.add_widget(buttonx151)
        layout.add_widget(buttonx152)
        screen27.add_widget(layout)
        self.screen_manager.add_widget(screen27)

        screen28=Screen(name='Gathering')
        blmain = Widget()
        blmain.add_widget(Image(source = "background.jpg", size = Window.size, allow_stretch = True, keep_ratio = False))
        layout = BoxLayout(orientation='vertical')
        buttonx160 = Label(text="Czy brałeś udział w zorganizowanych zgromadzeniach w ostatnim czasie?",color=(0,0,0,1))
        buttonx161 = Button(text="Tak",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        buttonx162 = Button(text="Nie",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        buttonx161.bind(on_release=self.btnx161)
        buttonx162.bind(on_release=self.btnx162)
        layout.add_widget(blmain)
        layout.add_widget(buttonx160)
        layout.add_widget(buttonx161)
        layout.add_widget(buttonx162)
        screen28.add_widget(layout)
        self.screen_manager.add_widget(screen28)

        screen29=Screen(name='Visit')
        blmain = Widget()
        blmain.add_widget(Image(source = "background.jpg", size = Window.size, allow_stretch = True, keep_ratio = False))
        layout = BoxLayout(orientation='vertical')
        buttonx170 = Label(text="Czy przebywałeś w zatłoczonym miejscu w ostatnim czasie?",color=(0,0,0,1))
        buttonx171 = Button(text="Tak",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        buttonx172 = Button(text="Nie",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        buttonx171.bind(on_release=self.btnx171)
        buttonx172.bind(on_release=self.btnx172)
        layout.add_widget(blmain)
        layout.add_widget(buttonx170)
        layout.add_widget(buttonx171)
        layout.add_widget(buttonx172)
        screen29.add_widget(layout)
        self.screen_manager.add_widget(screen29)

        screen30=Screen(name='Family')
        blmain = Widget()
        blmain.add_widget(Image(source = "background.jpg", size = Window.size, allow_stretch = True, keep_ratio = False))
        layout = BoxLayout(orientation='vertical')
        buttonx180 = Label(text="Czy ktoś z twojej rodziny pracuje w miejscu publicznym?",color=(0,0,0,1))
        buttonx181 = Button(text="Tak",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        buttonx182 = Button(text="Nie",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        buttonx181.bind(on_release=self.btnx201)
        buttonx182.bind(on_release=self.btnx202)
        layout.add_widget(blmain)
        layout.add_widget(buttonx180)
        layout.add_widget(buttonx181)
        layout.add_widget(buttonx182)
        screen30.add_widget(layout)
        self.screen_manager.add_widget(screen30)


        screen24=Screen(name='koniec2')
        blmain = Widget()
        blmain.add_widget(Image(source = "background.jpg", size = Window.size, allow_stretch = True, keep_ratio = False))
        layout = BoxLayout(orientation='vertical')
        buttonx120 = Label(text="Prawdopodobieństwo tego, że jesteś chory na COVID-19 wynosi:",color=(0,0,0,1))
        buttonx121 = Button(background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        self.wyniki=buttonx121
        buttonx122 = Button(text="Zacznij od poczatku",background_color =(0, 0, 0,0.5 ),color=(0,0,0,1))
        buttonx122.bind(on_release=self.btn120)
        layout.add_widget(blmain)
        layout.add_widget(buttonx120)
        layout.add_widget(buttonx121)
        layout.add_widget(buttonx122)
        screen24.add_widget(layout)
        self.screen_manager.add_widget(screen24)

        return self.screen_manager


        # funkcje do zycia

    def _update_image(self,instance,value):
        self.Window.size = instance.Window.size
 

    def btn01(self, button):
        self.screen_manager.current = 'Breathing' 

    def btnx11(self, button):
        self.screen_manager.current = 'Cold'
        self.Breathing=1

    def btnx12(self, button):
        self.screen_manager.current = 'Cold' 
        self.Breathing=0

    def btnx21(self, button):
        self.screen_manager.current = 'Cough'
        self.Cold=1

    def btnx22(self, button):
        self.screen_manager.current = 'Cough' 
        self.Cold=0  

    def btnx31(self, button):
        self.screen_manager.current = 'Throat'
        self.Cough=1

    def btnx32(self, button):
        self.screen_manager.current = 'Throat' 
        self.Cough=0   

    def btnx41(self, button):
        self.screen_manager.current = 'Runnynose'
        self.Throat=1

    def btnx42(self, button):
        self.screen_manager.current = 'Runnynose' 
        self.Throat=0 

    def btnx51(self, button):
        self.screen_manager.current = 'Head'
        self.Runnynose=1

    def btnx52(self, button):
        self.screen_manager.current = 'Head' 
        self.Runnynose=0   

    def btnx81(self, button):
        self.screen_manager.current = 'Heart' 
        self.Head=1 

    def btnx82(self, button):
        self.screen_manager.current = 'Heart' 
        self.Head=0 

    def btnx91(self, button):
        self.screen_manager.current = 'Diabetes' 
        self.Heart=1  

    def btnx92(self, button):
        self.screen_manager.current = 'Diabetes' 
        self.Heart=0 

    def btnx101(self, button):
        self.screen_manager.current = 'Hypertension' 
        self.Diabetes=1

    def btnx102(self, button):
        self.screen_manager.current = 'Hypertension' 
        self.Diabetes=0 

    def btnx111(self, button):
        self.screen_manager.current = 'Abroad' 
        self.Hypertension=1  

    def btnx112(self, button):
        self.screen_manager.current = 'Abroad' 
        self.Hypertension=0  

    def btnx141(self, button):
        self.screen_manager.current = 'Patient' 
        self.Abroad=1  

    def btnx142(self, button):
        self.screen_manager.current = 'Patient' 
        self.Abroad=0  

    def btnx151(self, button):
        self.screen_manager.current = 'Gathering' 
        self.Patient=1  

    def btnx152(self, button):
        self.screen_manager.current = 'Gathering' 
        self.Patient=0  

    def btnx161(self, button):
        self.screen_manager.current = 'Visit' 
        self.Gathering=1  

    def btnx162(self, button):
        self.screen_manager.current = 'Visit' 
        self.Gathering=0  

    def btnx171(self, button):
        self.screen_manager.current = 'Family' 
        self.Visit=1  

    def btnx172(self, button):
        self.screen_manager.current = 'Family' 
        self.Visit=0  

    def btnx201(self, button):
        self.screen_manager.current = 'koniec2' 
        self.Family=1
        self.w = pd.DataFrame([self.Breathing,self.Cold,self.Cough,self.Throat,self.Runnynose,self.Head,self.Heart,self.Diabetes,self.Hypertension,self.Abroad,self.Patient,self.Gathering,self.Visit,self.Family])
        self.w = self.w.T
        self.y = zycie(self.w)
        if self.y > 0.5:
            self.popup = Popup(title='', content=Label(text="Koniecznie udaj się do lekarza!"),size_hint=(None, None), size=(400, 400))
            self.popup.open()
        self.wyniki.text = str(self.y) + "%"

    def btnx202(self, button):
        self.screen_manager.current = 'koniec2' 
        self.Family=0
        self.w = pd.DataFrame([self.Breathing,self.Cold,self.Cough,self.Throat,self.Runnynose,self.Head,self.Heart,self.Diabetes,self.Hypertension,self.Abroad,self.Patient,self.Gathering,self.Visit,self.Family])
        self.w = self.w.T
        self.y = zycie(self.w)
        if self.y > 0.5:
            self.popup = Popup(title='', content=Label(text="Koniecznie udaj się do lekarza!"),size_hint=(None, None), size=(400, 400))
            self.popup.open()
        self.wyniki.text = str(self.y) + "%"


        # funkcie do smierci


    def btn00(self, button):
        self.screen_manager.current = 'sex'



    def btn11(self, button):
        self.screen_manager.current = 'Astma'
        self.sex=1

    def btn12(self, button):
        self.screen_manager.current = 'Astma' 
        self.sex=0

    def btn21(self, button):
        self.screen_manager.current = 'Cukrzyca'
        self.astma=1

    def btn22(self, button):
        self.screen_manager.current = 'Cukrzyca' 
        self.astma=0  

    def btn31(self, button):
        self.screen_manager.current = 'Pluca'
        self.cukrzyca=1

    def btn32(self, button):
        self.screen_manager.current = 'Pluca' 
        self.cukrzyca=0

    def btn41(self, button):
        self.screen_manager.current = 'leki'
        self.pluca=1

    def btn42(self, button):
        self.screen_manager.current = 'leki' 
        self.pluca=0    

    def btn51(self, button):
        self.screen_manager.current = 'tetnice'
        self.leki=1

    def btn52(self, button):
        self.screen_manager.current = 'tetnice' 
        self.leki=0  

    def btn61(self, button):
        self.screen_manager.current = 'nadwaga'
        self.tetnice=1

    def btn62(self, button):
        self.screen_manager.current = 'nadwaga' 
        self.tetnice=0 

    def btn71(self, button):
        self.screen_manager.current = 'nerki'
        self.nadwaga=1

    def btn72(self, button):
        self.screen_manager.current = 'nerki' 
        self.nadwaga=0

    def btn81(self, button):
        self.screen_manager.current = 'papierosy' 
        self.nerki=1  

    def btn82(self, button):
        self.screen_manager.current = 'papierosy' 
        self.nerki=0  

    def btna91(self, button):
        self.screen_manager.current = 'serce' 
        self.papierosy=1

    def btna92(self, button):
        self.screen_manager.current = 'serce' 
        self.papierosy=0  

    def btn91(self, button):
        self.screen_manager.current = 'inne' 
        self.serce=1

    def btn92(self, button):
        self.screen_manager.current = 'inne' 
        self.serce=0  

    def btn101(self, button):
        self.screen_manager.current = 'wiek' 
        self.inne=1

    def btn102(self, button):
        self.screen_manager.current = 'wiek' 
        self.inne=0

    def btn110(self, textinput):
        if len(textinput.parent.children[1].text) == 0:   # if text is not empty
            pass
        else:
            self.screen_manager.current = 'koniec' 
            self.wiek=int(textinput.parent.children[1].text) 
            self.w2 = pd.DataFrame([self.sex,self.wiek,self.cukrzyca,self.pluca,self.astma,self.leki,self.tetnice,self.inne,self.serce,self.nadwaga,self.nerki,self.papierosy])
            self.w2 = self.w2.T
            self.y2 = smierc(self.w2)
            if self.y2 > 0.5:
                self.popup = Popup(title='', content=Label(text="Koniecznie udaj się do lekarza!"),size_hint=(None, None), size=(400, 400))
                self.popup.open()
            self.wyniki2.text = str(self.y2) + "%"

    def btn120(self, textinput):
        self.screen_manager.current = 'start' 
    

   






app().run()