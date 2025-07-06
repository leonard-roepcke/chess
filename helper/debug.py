import pygame
import helper.input as inp

class Debuger:
    def __init__(self):
        self.enabled = True


        self.tweak_var = 0
        self.tweak_min = 0
        self.tweak_max = 0
        self.tweak_step = 0

    def start_log(self):
        self.enabled = True

    def stop_log(self):
        self.enabled = False

    def log(self, typ, text):
        if self.enabled:
            print(f"Log: {typ} = {text}")

    def log_force(self, typ, text): 
        print(f"Log: {typ} = {text}")


    def tweak_setup(self, min, max):
        self.tweak_var = min + (max-min)/2
        self.tweak_min = min
        self.tweak_max = max
        self.tweak_step = (max-min)/200

    def tweak(self):
        if inp.get_keys("+"):
            self.tweak_var += self.tweak_step
        
        if inp.get_keys("-"):
            self.tweak_var -= self.tweak_step

        if self.tweak_var < self.tweak_min:
            self.tweak_var = self.tweak_min

        if self.tweak_var > self.tweak_max:
            self.tweak_var = self.tweak_max

        self.tweak_var = round(self.tweak_var, 2)

        self.log_force("tweak var", self.tweak_var)
        return self.tweak_var

    def get_tweak(self):
        return self.tweak_var