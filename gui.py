#Author: John Marrs
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 
from random import randint
from PasswordGenerator import generate_password

class PassGenBoxLayout(BoxLayout):
	#Creates a class that extends the BoxLayout (structure defined in passgen.kv file)
	def generate_new_password(self):
		#Sets boolean values for checkboxes (used for calling the generate_password() function)
		l = self.ids.lower_box.active
		u = self.ids.upper_box.active
		n = self.ids.number_box.active
		s = self.ids.special_box.active

		#Checks to see if at least one character set has been selected, and if the the bounds logically make sense
		if (l or u or n or s) and ((self.ids.upper_slider.value - self.ids.lower_slider.value) >= 0):
			#Generates a password and prints it to the screen
			self.ids.display.text = 'Password: ' + generate_password(l, u, n, s, randint(self.ids.lower_slider.value, self.ids.upper_slider.value)) 
		else:
			#If no charset is selected, 'invalid inputs' will be displayed to the screen
			self.ids.display.text = 'Invalid Inputs'


	#Changes the display text for what the lower bound of the password's length is
	def edit_lower_bound(self, obj):
		self.ids.lower_display.text = str(obj.value)

	#Changes the display text for what the upper bound of the password's length is
	def edit_upper_bound(self, obj):
		self.ids.upper_display.text = str(obj.value)


#Creates the APP
class PassGenApp(App):
	def build(self):
		return PassGenBoxLayout()

#Runs the program
if __name__ == "__main__":
	PassGenApp().run()