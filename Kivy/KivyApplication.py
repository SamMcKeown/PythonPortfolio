import os
from typing import KeysView, Text
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class HolaPuggle(App):

    def build(self):
        '''
        Initializes the application
        
        Returns
        -------
        kivy.uix.gridlayout.GridLayout
            Returns the application window as the root widget
        '''

        # Window 
        self.window = GridLayout(size_hint=(None, None), width=300, height=300)
        self.window.cols = 1 
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        
        # Image
        self.image = Image(source='images/image_1.png', allow_stretch=True, 
                           size_hint_y=None, height=600)
        self.window.add_widget(self.image)

        # Label
        self.greeting = Label(text='¿Cómo te llamas?', font_size='20sp')
        self.window.add_widget(self.greeting) 

        # User Input
        self.user =  TextInput(multiline=False, hint_text='¡Introduzca su nombre aquí!', 
                               padding_y=(20, 20), size_hint=(1, .6), 
                               halign='center', font_size='12sp')
        self.window.add_widget(self.user)

        # Button
        self.button = Button(text='¡HOLA PUGGLE!', size_hint=(1, .5),
                             bold=True, font_size='14sp', 
                             background_color='#FF0000')

        # Button events
        self.button.bind(on_press=self.clear_input)
        self.button.bind(on_press=self.clear_input_2)
        self.button.bind(on_press=self.callback)
        self.button.bind(on_press=self.change_image)

        # Adds button to window
        self.window.add_widget(self.button)

        return self.window

    def callback(self, instance):
        '''Returns message containing user input or alternative message without user input'''
        if self.user.text != '' and not self.user.text.isspace(): 
            self.greeting.text = '¡Hola %s! \n¡Dame tu comida!' % self.user.text.capitalize()
        else:
            self.greeting.text = '¡¿donde esta tu nombre?!'

    def clear_input(self, instance):
        '''Clears user input'''
        self.user.text = ''

    def change_image(self, instance):
        '''Changes the intitial image'''
        if self.user.text != '' and not self.user.text.isspace():
            self.image.source='images/image_3.png'
        else:
            self.image.source='images/image_2.png'

    def clear_input_2(self, instance):
        '''Clears hint text'''
        if self.user.text != '':
            self.user.hint_text = '¿introduce otro nombre?'
        else:
            self.user.hint_text = '¡Por favor introduzca su nombre aquí!'

# Runs applicaiton
if __name__ == '__main__':
    HolaPuggle().run()