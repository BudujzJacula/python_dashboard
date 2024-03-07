import obd
import pygame
from dataclasses import dataclass
import config
import threading
import time
import logging
import sys

# logging_level = logging.DEBUG
# logger = logging.getLogger(__name__)
# logger = logging.basicConfig(format = 'log_dashboard:%(levelname)s:%(filename)s:%(funcName)s:%(message)s',
                            # level=logging_level)
# obd.logger.setLevel(obd.logging.DEBUG)

connection_obj = None

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1024

rpm = obd.commands.RPM
speed = obd.commands.SPEED
engine_temp = obd.commands.COOLANT_TEMP
fuel_level = obd.commands.FUEL_LEVEL

throttle_actuator = obd.commands.THROTTLE_ACTUATOR
throttle_pos = obd.commands.THROTTLE_POS
throttle_pos_b = obd.commands.THROTTLE_POS_B
throttle_pos_c = obd.commands.THROTTLE_POS_C

accelerator_pos_d = obd.commands.ACCELERATOR_POS_D
accelerator_pos_e = obd.commands.ACCELERATOR_POS_E
accelerator_pos_f = obd.commands.ACCELERATOR_POS_F

oil_temp = obd.commands.OIL_TEMP
fuel_press = obd.commands.FUEL_PRESSURE
battery_volt = obd.commands.ELM_VOLTAGE

pids = obd.commands.PIDS_A
status = obd.commands.STATUS
freeze_dtc = obd.commands.FREEZE_DTC
fuel_status = obd.commands.FUEL_STATUS
engine_load = obd.commands.ENGINE_LOAD

intake_temp = obd.commands.INTAKE_TEMP
intake_press = obd.commands.INTAKE_PRESSURE

obd_compliance = obd.commands.OBD_COMPLIANCE
fuel_rail_press = obd.commands.FUEL_RAIL_PRESSURE_VAC

@dataclass
class DashValues:
    rpm: int = 4400
    speed: int = 0
    gear: int = 0
    # engine_temp: int = 0 # engine temp is coolant temp
    fuel_level: int = 0
    throttle_actuator: int = 0
    throttle_pos: int = 0
    throttle_pos_b: int = 0
    coolant_temp: int = 0
    engine_load: int = 0
    intake_temp: int = 0
    intake_press: int = 0
    battery_volt: int = 0
    intake_temp: int = 0
    intake_press: int = 0
    engine_load: int = 0
    low_beam_light: bool = False
    high_beam_light: bool = False
    brakes_warn: bool = False
    low_oil_press_warn: bool = False
    low_battery_volt_warn: bool = False
    check_engine_warn: bool = False
    left_blinker: bool = False
    right_blinker: bool = False
    new_data: bool = False

class DashboardGUI():
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("OBD2 Dashboard")
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

    def _check_quit(self):
        if event.type == pygame.QUIT:
            pygame.quit()
            print("Quitting...")
            # BUG: sys.exit() doesn't work
            sys.exit()
            # quit()
    
    def _print_background(self):
        # black background
        self.window.fill((0, 0, 0))

        font = pygame.font.Font(config.FONT_NAME, 16)

        text = font.render(str(config.GEAR_TXT), 0, "white")
        self.window.blit(text, (512, 150))

        text = font.render(str(config.THRTTL_POS_TXT), 0, "white")
        self.window.blit(text, (35, 500))

        text = font.render(str(config.THROTTLE_POS), 0, "white")
        self.window.blit(text, (205, 500))

        text = font.render(str(config.ENGINE_LOAD), 0, "white")
        self.window.blit(text, (375, 500))

        text = font.render(str(config.COOLANT_TEMP_TXT), 0, "white")
        self.window.blit(text, (545, 500))

        text = font.render(str(config.INTAKE_TEMP), 0, "white")
        self.window.blit(text, (735, 500))
        
        text = font.render(str(config.INTAKE_PRESS), 0, "white")
        self.window.blit(text, (735, 545))

        text = font.render(str(config.BATT_VLTG_TXT), 0, "white")
        self.window.blit(text, (895, 500))

    def rotatePivoted(self, image, angle, pivot):
        rotated_image = pygame.transform.rotate(image, angle)
        rect = rotated_image.get_rect()
        rect.center = pivot
        return rotated_image, rect

    def _draw_rpm_gauge(self, rpm: DashValues.rpm):
        rpm_gauge_cords = (80, 90)
        rpm_needle_cords = (260, 280)
        rpm_zero_offset = 193
        rpm_angle = rpm_zero_offset - (rpm / 30)

        image = pygame.image.load(config.RPM_GAUGE_PATH)
        self.window.blit(image, rpm_gauge_cords)

        image = pygame.image.load(config.RPM_NEEDLE_PATH)
        rotated_image, rect = self.rotatePivoted(image, rpm_angle, rpm_needle_cords)
        self.window.blit(rotated_image, rect)
    
    def _draw_speed_gauge(self, speed: DashValues.speed):
        speed_gauge_cords = (600, 90)
        speed_needle_cords = (782, 268)
        speed_zero_offset = -131
        speed_angle = speed_zero_offset - (speed * 1.5)

        image = pygame.image.load(config.SPEED_GAUGE_PATH)
        self.window.blit(image, speed_gauge_cords)

        image = pygame.image.load(config.SPEED_NEEDLE_PATH)
        rotated_image, rect = self.rotatePivoted(image, speed_angle, speed_needle_cords)
        self.window.blit(rotated_image, rect)

    def _draw_speed_indicator(self, speed: DashValues.speed):
        font = pygame.font.Font(config.FONT_NAME, 36)

        speed_text = str(speed)
        text = font.render(speed_text, 0, "black")
        if speed < 100:
            self.window.blit(text, (760, 330))
        else:
            self.window.blit(text, (750, 330))

    def draw_gear_idicator(self, gear: DashValues.gear):
        font = pygame.font.Font(config.FONT_NAME, 100)
        if gear:
            gear_text = str(gear)
        else:
            gear_text = "N"

        text = font.render(gear_text, 0, "white")
        self.window.blit(text, (500, 200))
    
    def _draw_engine_temp_gauge(self, engine_temp: DashValues.intake_temp):
        # needle cords on the gauge = (106, 104)
        # temp range: 70 - 130 (70, 85, 100, 115, 130)
        temp_gauge_cords = (200, 370)
        temp_needle_cords = (53+200, 62+370)
        temp_zero_offset = 45

        if engine_temp < 70:
            temp_angle = temp_zero_offset
        else:
            temp_angle = temp_zero_offset - 1.7 * (engine_temp - 70)

        image = pygame.image.load(config.TEMP_GAUGE_PATH)
        self.window.blit(image, temp_gauge_cords)

        image = pygame.image.load(config.TEMP_NEEDLE_PATH)
        rotated_image, rect = self.rotatePivoted(image, -temp_angle, temp_needle_cords)
        self.window.blit(rotated_image, rect)
    
    def _draw_fuel_level_gauge(self, fuel_level: DashValues.fuel_level):
        pass
    
    def _draw_throttle_actuator_indicator(self, throttle_pos: DashValues.throttle_actuator):
        throttle_pos_text = str(throttle_pos)

        font = pygame.font.Font(config.FONT_NAME, 36)
        text = font.render(throttle_pos_text, 0, "white")
        self.window.blit(text, (65, 530))

    def _draw_throttle_pos_indicator(self, oil_temp: DashValues.throttle_pos):
        oil_temp_text = str(oil_temp)

        font = pygame.font.Font(config.FONT_NAME, 36)
        text = font.render(oil_temp_text, 0, "white")
        self.window.blit(text, (235, 530))

    def _draw_engine_load_indicator(self, oil_press: DashValues.engine_load):
        oil_press_text = str(oil_press)

        font = pygame.font.Font(config.FONT_NAME, 36)
        text = font.render(oil_press_text, 0, "white")
        self.window.blit(text, (391, 530))

    def _draw_coolant_temp_indicator(self, coolant_temp: DashValues.intake_temp):
        coolant_temp_text = str(coolant_temp)

        font = pygame.font.Font(config.FONT_NAME, 36)
        text = font.render(coolant_temp_text, 0, "white")
        self.window.blit(text, (590, 530))

    def _draw_intake_temp_indicator(self, intake_temp: DashValues.intake_temp):
        intake_temp_text = str(intake_temp)

        font = pygame.font.Font(config.FONT_NAME, 36)
        text = font.render(intake_temp_text, 0, "white")
        self.window.blit(text, (755, 511))

    def _draw_intake_press_indicator(self, fuel_press: DashValues.intake_press):
        fuel_press_text = str(fuel_press)

        font = pygame.font.Font(config.FONT_NAME, 36)
        text = font.render(fuel_press_text, 0, "white")
        self.window.blit(text, (755, 556))

    def _draw_battery_volt_indicator(self, battery_volt: DashValues.battery_volt):
        battery_volt_text = str(battery_volt)

        font = pygame.font.Font(config.FONT_NAME, 36)
        text = font.render(battery_volt_text, 0, "white")
        self.window.blit(text, (910, 530))

    def draw_left_gauge(self, dash_vals: DashValues):
        self._draw_rpm_gauge(dash_vals.rpm)
        self._draw_fuel_level_gauge(dash_vals.fuel_level)
        self._draw_engine_temp_gauge(dash_vals.coolant_temp)

    def draw_right_gauge(self, dash_vals: DashValues):
        self._draw_speed_gauge(dash_vals.speed)
        self._draw_speed_indicator(dash_vals.speed)

    def _draw_low_beam_light(self, low_beam_light: DashValues.low_beam_light):
        if low_beam_light:
            image = pygame.image.load(config.LOW_BEAM_PATH)
        else:
            image = pygame.image.load(config.NO_LIGHT_PATH)
        self.window.blit(image, (470, 320))

    def _draw_high_beam_light(self, high_beam_light: DashValues.high_beam_light):
        if high_beam_light:
            image = pygame.image.load(config.HIGH_BEAM_PATH)
        else:
            image = pygame.image.load(config.NO_LIGHT_PATH)
        self.window.blit(image, (530, 320))

    def _draw_brake_light(self, brakes_warn: DashValues.brakes_warn):
        if brakes_warn:
            image = pygame.image.load(config.BRAKE_PATH)
        else:
            image = pygame.image.load(config.NO_LIGHT_PATH)
        self.window.blit(image, (470, 360))

    def _draw_oil_level_light(self, low_oil_press_warn: DashValues.low_oil_press_warn):
        if low_oil_press_warn:
            image = pygame.image.load(config.OIL_LEVEL_PATH)
        else:
            image = pygame.image.load(config.NO_LIGHT_PATH)
        self.window.blit(image, (530, 360))

    def _draw_battery_light(self, battery_volt_warn: DashValues.low_battery_volt_warn):
        if battery_volt_warn:
            image = pygame.image.load(config.BATTERY_PATH)
        else:
            image = pygame.image.load(config.NO_LIGHT_PATH)
        self.window.blit(image, (470, 400))

    def _draw_check_engine(self, check_engine_warn: DashValues.check_engine_warn):
        if check_engine_warn:
            image = pygame.image.load(config.CHECK_ENGINE_PATH)
        else:
            image = pygame.image.load(config.NO_LIGHT_PATH)
        self.window.blit(image, (530, 400))

    def draw_warning_lights(self, dash_vals: DashValues):
        self._draw_low_beam_light(dash_vals.low_beam_light)
        self._draw_high_beam_light(dash_vals.high_beam_light)
        self._draw_brake_light(dash_vals.brakes_warn)
        self._draw_oil_level_light(dash_vals.low_oil_press_warn)
        self._draw_battery_light(dash_vals.low_battery_volt_warn)
        self._draw_check_engine(dash_vals.check_engine_warn)

    def _draw_left_blinker(self, left_blinker: DashValues.left_blinker):
        left_blinker_offset = 30
        if left_blinker:
            image = pygame.image.load(config.LEFT_BLINKER_PATH)
        else:
            image = pygame.image.load(config.NO_LIGHT_PATH)
        self.window.blit(image, (512 - left_blinker_offset, 100))

    def _draw_right_blinker(self, right_blinker: DashValues.right_blinker):
        right_blinker_offset = 30
        if right_blinker:
            image = pygame.image.load(config.RIGHT_BLINKER_PATH)
        else:
            image = pygame.image.load(config.NO_LIGHT_PATH)
        self.window.blit(image, (512 + right_blinker_offset, 100))

    def draw_blinkers(self, dash_vals: DashValues):
        self._draw_left_blinker(dash_vals.left_blinker)
        self._draw_right_blinker(dash_vals.right_blinker)
    
    def draw_diag_idicators(self, dash_vals: DashValues):
        # throttle actuator, throttle position, engine load, 
        # coolant temp, intake temp/intake pressure, battery voltage
        self._draw_throttle_actuator_indicator(dash_vals.throttle_actuator)
        self._draw_throttle_pos_indicator(dash_vals.throttle_pos)
        self._draw_engine_load_indicator(dash_vals.engine_load)
        self._draw_coolant_temp_indicator(dash_vals.coolant_temp)
        self._draw_intake_temp_indicator(dash_vals.intake_temp)
        self._draw_intake_press_indicator(dash_vals.intake_press)
        self._draw_battery_volt_indicator(dash_vals.battery_volt)

    def _rpm_to_lights(self, rpm: DashValues.rpm):
        greens = min(max((rpm - 4000) // 400, 0), 3)
        oranges = min(max((rpm - 5000) // 400, 0), 3)
        reds = min(max((rpm - 6000) // 400, 0), 3)

        return greens, oranges, reds

    def _turn_on_light(self, lights, start_cords, image):
        # print(lights)
        for i in range(1, lights + 1):
            self.window.blit(image, (start_cords[0] + (i*40), start_cords[1]))
            self.window.blit(image, (SCREEN_WIDTH - (start_cords[0] + (i*40)), start_cords[1]))

    def draw_limiter_lights(self, rpm: DashValues.rpm):
        nr_of_limit_lights = 19
        light_spacing = 40
        offset = 150

        grey_light = pygame.image.load(config.LIMIT_LIGHT_GREY)
        green_light = pygame.image.load(config.LIMIT_LIGHT_GREEN)
        orange_light = pygame.image.load(config.LIMIT_LIGHT_ORANGE)
        red_light = pygame.image.load(config.LIMIT_LIGHT_RED)

        # limit lights steps:
        # green: 4400, 4800, 5200
        # orange: 5600, 6000, 6400
        # red: 6800, 7200, 7600
        greens, oranges, reds = self._rpm_to_lights(rpm)

        # print("lights: ", greens, " ", oranges, " ", "rpm: ", reds, rpm, "angle: ", rpm / 50)

        # zero out the lights
        # for i in range(nr_of_limit_lights):
        #     self.window.blit(grey_light, (i*light_spacing + offset, 10))

        # draw the lights
        if not(greens):
            return
        else:
            self._turn_on_light(greens, config.GREEN_CORDS, green_light)

        if not(oranges):
            return
        else:
            self._turn_on_light(oranges, config.ORANGE_CORDS, orange_light)

        if not(reds):
            return
        else:
            self._turn_on_light(reds, config.RED_CORDS, red_light)

    def draw_dash(self, dash_vals: DashValues):
        self.draw_limiter_lights(dash_vals.rpm)
        self.draw_gear_idicator(dash_vals.gear)
        self.draw_left_gauge(dash_vals)
        self.draw_right_gauge(dash_vals)
        self.draw_diag_idicators(dash_vals)
        self.draw_blinkers(dash_vals)
        self.draw_warning_lights(dash_vals)

def request():
    while True:
        # TODO: wrzucic gotowe komendy do listy albo do dataclassy i loopowac po niej zamiast pisac wszystko na piechote
        val_rpm = connection_obj.query(rpm)
        val_speed = connection_obj.query(speed)
        val_engine_temp = connection_obj.query(engine_temp)
        val_throttle_actuator = connection_obj.query(throttle_actuator)
        val_throttle_pos = connection_obj.query(throttle_pos)
        val_throttle_pos_b = connection_obj.query(throttle_pos_b)

        val_battery_volt = connection_obj.query(battery_volt)

        # val_val_pids = connection.query(pids)
        val_status = connection_obj.query(status)
        val_fuel_status = connection_obj.query(fuel_status)
        val_engine_load = connection_obj.query(engine_load)

        val_intake_temp = connection_obj.query(intake_temp)
        val_intake_press = connection_obj.query(intake_press)

        val_obd_compliance = connection_obj.query(obd_compliance)

        # pids = val_val_pids.value

        DashValues.rpm = round(val_rpm.value.m)
        DashValues.speed = round(val_speed.value.m)
        DashValues.coolant_temp = val_engine_temp.value.m
        DashValues.throttle_actuator = int(val_throttle_actuator.value)
        DashValues.throttle_pos = int(val_throttle_pos.value)
        DashValues.throttle_pos_b = int(val_throttle_pos_b.value)
        DashValues.battery_volt = val_battery_volt.value.m
        DashValues.engine_load = int(val_engine_load.value)
        DashValues.intake_temp = val_intake_temp.value.m
        DashValues.intake_press = val_intake_press.value.m
        DashValues.new_data = True

        # TODO dodac mierzenie czasu petli i wyswietlanie czestotliwosci odswiezania
        time.sleep(0.1)

def connect():
    print("Connecting...")
    global connection_obj
    connection_obj = obd.OBD(portstr='COM15', baudrate=38400)

if __name__ == "__main__":
    t_conn = threading.Thread(target = connect)
    t_conn.start()
    t_conn.join(timeout=15)
    if connection_obj:
        print("connection: ", connection_obj)
    else:
        print("Connection failed")

    dashboard = DashboardGUI()

    t1 = threading.Thread(target = request)
    t1.start()

    while True:
        for event in pygame.event.get():
            dashboard._check_quit()
            # dashboard._check_arrow_keys()
            # dashboard._check_keyboard()

        if DashValues.new_data:
            DashValues.new_data = False
            dashboard._print_background()
            dashboard.draw_dash(DashValues)
            pygame.display.update()
            dashboard.clock.tick(30)