from dataclasses import dataclass
import tkinter as tk

@dataclass
class DashValues:
    speed: int = 0
    rpm: int = 0
    gear: int = 0
    engine_temp: int = 0
    fuel_level: int = 0
    throttle_pos: int = 0
    oil_temp: int = 0
    oil_press: int = 0
    coolant_temp: int = 0
    fuel_press: int = 0
    battery_volt: int = 0
    low_beam_light: bool = False
    high_beam_light: bool = False
    breaks_warn: bool = False
    low_oil_press_warn: bool = False
    low_battery_volt_warn: bool = False
    check_engine_warn: bool = False


def draw_rpm_gauge():
    pass

def draw_speed_gauge():
    pass

def draw_speed_indicator():
    pass

def draw_fuel_level_gauge():
    pass

def draw_engine_temp_gauge():
    pass

def draw_gear_idicator():
    pass

def draw_throttle_pos_indicator():
    pass

def draw_oil_temp_indicator():
    pass

def draw_oil_press_indicator():
    pass

def draw_coolant_temp_indicator():
    pass

def draw_fuel_press_indicator():
    pass

def draw_battery_volt_indicator():
    pass

def draw_left_gauge():
    draw_rpm_gauge()
    draw_fuel_level_gauge()
    draw_engine_temp_gauge()

def draw_right_gauge():
    draw_speed_gauge()
    draw_speed_indicator()

def draw_low_beam_light():
    pass

def draw_high_beam_light():
    pass

def draw_brake_light():
    pass

def draw_oil_level_light():
    pass

def draw_battery_light():
    pass

def draw_check_engine():
    pass

def draw_warning_lights():
    draw_low_beam_light()
    draw_high_beam_light()
    draw_brake_light()
    draw_oil_level_light()
    draw_battery_light()
    draw_check_engine()

def draw_left_blinker():
    pass

def draw_right_blinker():
    pass

def draw_blinkers():
    draw_left_blinker()
    draw_right_blinker()
  
def draw_diag_idicators():
    draw_throttle_pos_indicator()
    draw_oil_temp_indicator()
    draw_oil_press_indicator()
    draw_coolant_temp_indicator()
    draw_fuel_press_indicator()
    draw_battery_volt_indicator()


def draw_dash(dash_vals: DashValues):
    pass

def main():
    root = tk.Tk()


    root.mainloop()

if __name__ == "__main__":
    main()