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
import mysql.connector
import gmail_otp


Window.size= (550,600) # This sets the default screen size of the application

"""Below is the string which contains kivymd attributes and this string is loaded in the builder method 
below in Main class"""

kv = """
ScreenManager:
    HomeScreen:
    PersonalinfoScreen:
    NDAScreen:
    SignatureScreen:
<HomeScreen>:
    name: 'home'
    MDLabel:
        text: 'Welcome to Cinegence Media'
        halign: 'center'
        pos_hint: {'center_y':0.85}
        font_style: 'H3'
        theme_text_color: 'Custom'
        text_color: app.theme_cls.primary_color
    Image:
        source: 'cine_og.jpg'
        size_hint: (0.5,0.5)
        pos_hint: {'center_x':0.5,'center_y':0.50}
    MDFloatingActionButton:
        icon: 'account-arrow-right'
        user_font_size: '50sp'
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.5,'center_y':0.10}
        on_press:
            root.manager.current = 'personal'
            root.manager.transition.direction = 'left'
    MDProgressBar:
        value: 25
        pos_hint: {'center_y':0.01}

<PersonalinfoScreen>:
    name: 'personal'
    Image:
        source: 'cine.jpg'
        pos_hint: {'center_x':0.5,'center_y':0.88}
        size_hint: (None,None)
        height: 100
        width: 100
    MDLabel:
        text: 'CINEGENCE'
        font_style:'H4'
        pos_hint: {'center_x':0.50,'center_y':0.76}
        size_hint_x: None
        width:184
        theme_text_color: 'Hint'
    MDTextField:
        id: name_text
        hint_text:'Enter your Name'
        helper_text:'Enter in UpperCase'
        helper_text_mode: 'on_focus'
        pos_hint: {'center_x':0.50,'center_y':0.60}
        size_hint_x: None
        width: 320
        font_size: '20sp'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
    MDTextField:
        id: address_text
        hint_text:'Enter your Address'
        helper_text:'Enter in UpperCase'
        helper_text_mode: 'on_focus'
        font_size: '20sp'
        pos_hint: {'center_x':0.50,'center_y':0.48}
        size_hint_x: None
        width: 320
        icon_right: 'clipboard-text'
        icon_right_color: app.theme_cls.primary_color
    MDTextField:
        id: email_text
        hint_text:'Enter your Email'
        helper_text:'Example: abc@gmail.com'
        helper_text_mode: 'on_focus'
        font_size: '20sp'
        pos_hint: {'center_x':0.50,'center_y':0.36}
        size_hint_x: None
        width: 320
        icon_right: 'email'
        icon_right_color: app.theme_cls.primary_color
    MDRectangleFlatButton:
        id: otp
        text:'Send OTP'
        pos_hint: {'center_x':0.30,'center_y':0.26}
        on_press: app.send_otp()
    MDFillRoundFlatIconButton:
        id: save
        text:'  Submit'
        icon:'content-save-outline'
        pos_hint: {'center_x':0.5,'center_y':0.11}
        on_press: app.submit()
    MDFloatingActionButton:
        icon: 'arrow-left'
        user_font_size: '40sp'
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.1,'center_y':0.1}
        on_press:
            root.manager.current = 'home'
            root.manager.transition.direction = 'right'
    MDFloatingActionButton:
        id: disabled_button
        disabled: True
        icon: 'arrow-right'
        user_font_size: '40sp'
        md_bg_color: app.theme_cls.primary_color
        pos_hint: {'center_x':0.9,'center_y':0.1}
        on_press:
            root.manager.current = 'nda'
            root.manager.transition.direction = 'left'
    MDTextFieldRound:
        id: enter_otp
        hint_text: 'Enter OTP'
        icon_right: 'onepassword'
        normal_color: app.theme_cls.primary_color
        color_active: (153/255,102/255,1,1)
        pos_hint: {'center_x':0.75,'center_y':0.26}
        size_hint_x: None
        width: 130
        
    MDProgressBar:
        value: 50
        pos_hint: {'center_y':0.01}
<NDAScreen>:
    name: 'nda'
    ScrollView:
        FloatLayout:
            MDLabel:
                text: 'CINEGENCE NDA'
                halign: 'center'
                pos_hint:{'center_y':0.97}
                theme_text_color: 'Custom'
                text_color: app.theme_cls.primary_color
                font_style: 'H5'
            Image
                source: 'nda.png'
                size_hint_y: None
                height:500
                pos_hint:{'center_y':0.52}
            MDFillRoundFlatIconButton:
                text: 'Click to Sign on Next page'
                icon: 'arrow-bottom-right-thick'
                pos_hint: {'center_x':0.5,'center_y':0.055}
                size_hint_y: None
                height: 40
                on_press:
                    root.manager.current = 'sign'
                    root.manager.transition.direction = 'left'
            
            # MDRaisedButton:
            #     #disabled: True
            #     id: date_pick
            #     text: 'Select date'
            #     pos_hint: {'center_x':0.15,'center_y':0.045}
            #     on_press: app.show_date()
            #     size_hint_x: None
            #     width: 40
            MDFloatingActionButton:
                icon: 'arrow-left'
                user_font_size: '30sp'
                md_bg_color: app.theme_cls.primary_color
                pos_hint: {'center_x':0.05,'center_y':0.5}
                on_press:
                    root.manager.current = 'personal'
                    root.manager.transition.direction = 'right'
            MDProgressBar:
                value: 75
                pos_hint: {'center_y':0.01}

# Below starts the signature screen contains attributes for signature canvas

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
""" Classes defined for inheriting the Screen class"""
class HomeScreen(Screen):
    pass
class PersonalinfoScreen(Screen):
    pass
class NDAScreen(Screen):
    pass
class SignatureScreen(Screen):
    pass

"""Sign class that contains methods which allow user to sign on the screen"""   
class Sign(Widget):
    count = 0
    def on_touch_down(self,touch):
        with self.canvas:
            Color(1,0,0)
            touch.ud['line'] = Line(points=(touch.x, touch.y))
            self.count += 1

    def on_touch_move(self,touch):
        touch.ud['line'].points += [touch.x,touch.y]
    

"""Added different screens to screen manager using add_widget method""" 
    
sm = ScreenManager()
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(PersonalinfoScreen(name='personal'))
sm.add_widget(NDAScreen(name='nda'))
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

    def submit(self): # This method gets called when we click on submit button
        close = MDFlatButton(text='CLOSE',on_release=self.close)
        try_again = MDFlatButton(text='TRY AGAIN',on_release=self.close)
        self.Name= self.screen.get_screen('personal').ids.name_text.text
        self.Address= self.screen.get_screen('personal').ids.address_text.text
        self.Email= self.screen.get_screen('personal').ids.email_text.text
        
        if self.Name.isdigit()==True or self.Name.split()==[]:
            self.dialog = MDDialog(title='INVALID NAME',text='Enter a Valid Name',
                                   size_hint= (0.7,1), buttons=[close,try_again])
            self.dialog.open()
        elif self.Address.isdigit()==True or self.Address.split()==[]:
            self.dialog = MDDialog(title='INVALID ADDRESS',text='Enter a Valid Address',
                                   size_hint= (0.7,1), buttons=[close,try_again])
            self.dialog.open()
        elif self.Email.isdigit()==True or self.Email.split()==[] :
            self.dialog = MDDialog(title='INVALID EMAIL',text='Enter a valid email(check example for reference)',
                                   size_hint= (0.7,1), buttons=[close,try_again])
            self.dialog.open()
        # Below is the snippet for storing variables data(Name, Address and Email) on mysql server
        else:
            mydb = mysql.connector.connect(host= 'localhost', user= 'root', passwd= 'lolo123', database= 'test')
            my_cursor = mydb.cursor()
            sqlstuff = "INSERT INTO info(name, address, email)VALUES(%s, %s, %s)"
            v_name = self.Name
            v_address = self.Address
            v_email = self.Email
            record = (v_name, v_address, v_email)
            my_cursor.execute(sqlstuff, record)
            mydb.commit()
            self.screen.get_screen('personal').ids.disabled_button.disabled= False

    def close(self,obj):
        self.dialog.dismiss()

    # def show_date(self):
    #     date_dialog = MDDatePicker(callback= self.get_date)
    #     date_dialog.open()
    # def get_date(self,date):
    #     self.today = date
    #     self.screen.get_screen('nda').ids.date_pick.text = str(self.today)
    
    def clear_sign(self):
        self.screen.get_screen('sign').ids.signature.canvas.clear()
        

    def send_otp(self):
        self.Email = self.screen.get_screen('personal').ids.email_text.text
        gmail_otp.otp_protocol(self.Email)


    def finish(self):
        close = MDFlatButton(text='CLOSE',on_release=self.close)
        try_again = MDFlatButton(text='TRY AGAIN',on_release=self.close)
        # Unable to access the count variable here to include it in if statement
        
        if Sign.children == None:
            self.dialog = MDDialog(title='NO Signature',text='Please provide signature before clicking on Finish',
                                   size_hint= (0.7,1), buttons=[close,try_again])
            self.dialog.open()
        else:
            print('Signature is done')
        

    
            


if __name__ == '__main__':  
    Main().run()

