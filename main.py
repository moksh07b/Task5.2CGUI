import tkinter as tk
import time
import RPi.GPIO as GPIO



class App():
    def __init__(self):
        #Declaring the variables and setting out pinmodes the pins
        GPIO.setmode(GPIO.BOARD)
        
        self.red_led = 12
        self.blue_led = 16
        self.yellow_led = 18
        
        GPIO.setup(self.red_led, GPIO.OUT)
        GPIO.setup(self.blue_led, GPIO.OUT)
        GPIO.setup(self.yellow_led, GPIO.OUT)
        
        # MAking the GUI for the user and placing it on the window.
        self.main_window = tk.Tk()
        self.main_window.geometry('400x400')
        self.main_window.title('Raspberry GUI')
        
        #Initially everything at the start is at 0 value
        self.var1 = tk.DoubleVar()
        self.var1.trace_add('write', lambda var_name, index, mode: self.change_light_intensity(1, self.var1))
        self.pwm1 = GPIO.PWM(self.red_led, 1000)
        self.pwm1.start(0)

        self.var2 = tk.DoubleVar()
        self.var2.trace_add('write', lambda var_name, index, mode: self.change_light_intensity(2, self.var2))
        self.pwm2 = GPIO.PWM(self.yellow_led, 1000)
        self.pwm2.start(0)

        self.var3 = tk.DoubleVar()
        self.var3.trace_add('write', lambda var_name, index, mode: self.change_light_intensity(3, self.var3))
        self.pwm3 = GPIO.PWM(self.blue_led, 1000)
        self.pwm3.start(0)     
      
        self.slider1 = self.get_slider(self.main_window, self.var1)
        self.slider1.place(x=100, y=40, width= 200)
        
        self.slider2 = self.get_slider(self.main_window, self.var2)
        self.slider2.place(x=100, y=140, width= 200)
        
        self.slider3 = self.get_slider(self.main_window, self.var3)
        self.slider3.place(x=100, y=240, width= 200)
        
        self.exit_button = self.get_button(self.main_window, "Exit", "green", self.exit)
        self.exit_button.place(x=100, y=300, width=200, height=60)
        
    def exit(self):
        #Stop everything and destroy at the end
        self.pwm1.stop()
        self.pwm2.stop()
        self.pwm3.stop()
        self.main_window.destroy()
        
    def change_light_intensity(self, slider_val, var):
        #Change duty cycle based on the slider value change
        value = var.get() / 255
        value = value * 100
        
        if slider_val == 1:
            self.pwm1.ChangeDutyCycle(value)
        elif slider_val == 2:
            self.pwm2.ChangeDutyCycle(value)
        elif slider_val == 3:
            self.pwm3.ChangeDutyCycle(value)        
        
    def get_slider(self, window, var):
        slider = tk.Scale(
            window, 
            bg="white",
            orient="horizontal",
            from_=0,    #Lower limit
            to=255,     #Upper Limit
            variable=var
        )
        return slider
    
    def get_text_label(window, text):
        label = tk.Label(window, text=text)
        label.config(font=("sans-serif", 21), justify="left")
        return label
    
    def get_button(self, window, text, color, command, fg="white"):
        button = tk.Button(
            window,
            text=text,
            activebackground="black",
            activeforeground="white",
            fg=fg,
            bg=color,
            command=command,
            font=("Helvetica bold", 20)
        )
        return button
        
    def start(self):
        self.main_window.mainloop()

if __name__ == "__main__":
    app = App()
    app.start()
