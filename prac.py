from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivy.uix.screenmanager import ScreenManager,Screen
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window
from kivymd.uix.picker import MDDatePicker
from kivy.uix.widget import Widget
from kivy.graphics import Color,Line
from kivy.core.image import Image as CoreImage


# Below starts the signature screen contains attributes for signature canvas
kv = """
ScreenManager:
    # HomeScreen:
    # PersonalinfoScreen:
    # NDAScreen:
    SignatureScreen:
<SignatureScreen>:
    name: 'sign'
    MDLabel:
        text: '     By Signing Below You Accept the Agreement that You Read on Previous Page'
        pos_hint: {'center_y':0.90}
        halign: 'center'
        font_style: 'H6'
        italic: True
        theme_text_color: 'Custom'
        text_color: app.theme_cls.primary_color
    MDIcon:
        icon:'alert-octagon'
        pos_hint: {'center_y':0.92}
        font_size: '50sp'
        theme_text_color: 'Custom'
        text_color: (0,1,1,1)
    Sign:
        id: signature
    MDRectangleFlatButton:
        text: 'Clear Sign'
        pos_hint: {'center_x':0.1,'center_y':0.1} 
        on_press: app.clear_sign()
    
    MDFillRoundFlatIconButton:
        id: finish
        text: ' FINISH'
        icon: 'page-last'
        pos_hint: {'center_x':0.5,'center_y':0.1} 
        on_press: app.finish()
"""

class SignatureScreen(Screen):
    pass

"""Sign class that contains methods which allow user to sign on the screen"""   
class Sign(Widget):
    
    def on_touch_down(self,touch):
        with self.canvas:
            Color(1,0,0)
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self,touch):
        touch.ud['line'].points += [touch.x,touch.y]

"""Added different screens to screen manager using add_widget method"""       
sm = ScreenManager()
sm.add_widget(SignatureScreen(name='sign'))
class Main(MDApp):
    """Declare Name, Address, Email as class variables so that we can access these variables
    throughout the class inside any method"""
    Name = ''
    Address = ''
    Email = ''
    def build(self): # This method loads the kv string
        self.theme_cls.primary_palette= 'Pink'
        self.theme_cls.primary_hue= 'A200'
        self.theme_cls.theme_style= 'Dark' 
        self.screen = Builder.load_string(kv)
        return self.screen

    def clear_sign(self):
        self.screen.get_screen('sign').ids.signature.canvas.clear()

    def finish(self):
        # close = MDFlatButton(text='CLOSE',on_release=self.close)
        # try_again = MDFlatButton(text='TRY AGAIN',on_release=self.close)
        #self.over= self.screen.get_screen('sign').ids.finish
        
        # if self.screen.get_screen('sign').ids.signature.canvas == None:
        #     self.dialog = MDDialog(title='NO Signature',text='Please provide signature before clicking on Finish',
        #                            size_hint= (0.7,1), buttons=[close,try_again])
        #     self.dialog.open()
        # else:
        print('Signature is done')
        

if __name__ == '__main__':  
    Main().run()