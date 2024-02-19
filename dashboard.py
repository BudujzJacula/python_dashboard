from dataclasses import dataclass
import pygame
import config

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1024

@dataclass
class DashValues:
    rpm: int = 0
    speed: int = 0
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
    left_blinker: bool = False
    right_blinker: bool = False

class DashboardGUI():
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("OBD2 Dashboard")
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

    def _check_quit(self):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    def _print_background(self):
        font = pygame.font.Font(config.FONT_NAME, 16)
        text = font.render(str(config.THRTTL_POS_TXT), 0, "white")
        self.window.blit(text, (35, 500))

        text = font.render(str(config.OIL_TEMP_TXT), 0, "white")
        self.window.blit(text, (205, 500))

        text = font.render(str(config.OIL_PRESS_TXT), 0, "white")
        self.window.blit(text, (375, 500))

        text = font.render(str(config.COOLANT_TEMP_TXT), 0, "white")
        self.window.blit(text, (545, 500))

        text = font.render(str(config.FUEL_PRESS_TXT), 0, "white")
        self.window.blit(text, (735, 500))

        text = font.render(str(config.BATT_VLTG_TXT), 0, "white")
        self.window.blit(text, (895, 500))

    def _draw_rpm_gauge(self):
        pass
    
    def _draw_speed_gauge(self):
        pass
    
    def _draw_speed_indicator(self):
        pass
    
    def _draw_gear_idicator(self):
        pass
    
    def _draw_engine_temp_gauge(self):
        pass
    
    def _draw_fuel_level_gauge(self):
        pass
    
    def _draw_throttle_pos_indicator(self):
        throttle_pos_text = str(DashValues.throttle_pos)

        font = pygame.font.Font(config.FONT_NAME, 36)
        text = font.render(throttle_pos_text, 0, "white")
        self.window.blit(text, (65, 530))

    def _draw_oil_temp_indicator(self):
        oil_temp_text = str(DashValues.oil_temp)

        font = pygame.font.Font(config.FONT_NAME, 36)
        text = font.render(oil_temp_text, 0, "white")
        self.window.blit(text, (235, 530))

    def _draw_oil_press_indicator(self):
        oil_press_text = str(DashValues.oil_press)

        font = pygame.font.Font(config.FONT_NAME, 36)
        text = font.render(oil_press_text, 0, "white")
        self.window.blit(text, (391, 530))

    def _draw_coolant_temp_indicator(self):
        coolant_temp_text = str(DashValues.coolant_temp)

        font = pygame.font.Font(config.FONT_NAME, 36)
        text = font.render(coolant_temp_text, 0, "white")
        self.window.blit(text, (590, 530))

    def _draw_fuel_press_indicator(self):
        fuel_press_text = str(DashValues.fuel_press)

        font = pygame.font.Font(config.FONT_NAME, 36)
        text = font.render(fuel_press_text, 0, "white")
        self.window.blit(text, (755, 530))

    def _draw_battery_volt_indicator(self):
        battery_volt_text = str(DashValues.battery_volt)

        font = pygame.font.Font(config.FONT_NAME, 36)
        text = font.render(battery_volt_text, 0, "white")
        self.window.blit(text, (910, 530))

    def draw_left_gauge(self):
        self._draw_rpm_gauge()
        self._draw_fuel_level_gauge()
        self._draw_engine_temp_gauge()

    def draw_right_gauge(self):
        self._draw_speed_gauge()
        self._draw_speed_indicator()

    def _draw_low_beam_light(self):
        if DashValues.low_beam_light:
            image = pygame.image.load(config.LOW_BEAM_PATH)
        else:
            image = pygame.image.load(config.NO_LIGHT)
        self.window.blit(image, (0, 0))

    def _draw_high_beam_light(self):
        if DashValues.high_beam_light:
            image = pygame.image.load(config.HIGH_BEAM_PATH)
        else:
            image = pygame.image.load(config.NO_LIGHT)
        self.window.blit(image, (100, 0))

    def _draw_brake_light(self):
        if DashValues.breaks_warn:
            image = pygame.image.load(config.BRAKE_PATH)
        else:
            image = pygame.image.load(config.NO_LIGHT)
        self.window.blit(image, (200, 0))

    def _draw_oil_level_light(self):
        if DashValues.low_oil_press_warn:
            image = pygame.image.load(config.OIL_LEVEL_PATH)
        else:
            image = pygame.image.load(config.NO_LIGHT)
        self.window.blit(image, (300, 0))

    def _draw_battery_light(self):
        if DashValues.battery_volt:
            image = pygame.image.load(config.BATTERY_PATH)
        else:
            image = pygame.image.load(config.NO_LIGHT)
        self.window.blit(image, (400, 0))

    def _draw_check_engine(self):
        if DashValues.check_engine_warn:
            image = pygame.image.load(config.CHECK_ENGINE_PATH)
        else:
            image = pygame.image.load(config.NO_LIGHT)
        self.window.blit(image, (500, 0))

    def draw_warning_lights(self):
        self._draw_low_beam_light()
        self._draw_high_beam_light()
        self._draw_brake_light()
        self._draw_oil_level_light()
        self._draw_battery_light()
        self._draw_check_engine()

    def _draw_left_blinker(self):
        if DashValues.left_blinker:
            image = pygame.image.load(config.LEFT_BLINKER_PATH)
        else:
            image = pygame.image.load(config.NO_LIGHT)
        self.window.blit(image, (100, 100))

    def _draw_right_blinker(self):
        if DashValues.right_blinker:
            image = pygame.image.load(config.RIGHT_BLINKER_PATH)
        else:
            image = pygame.image.load(config.NO_LIGHT)
        self.window.blit(image, (200, 100))

    def draw_blinkers(self):
        self._draw_left_blinker()
        self._draw_right_blinker()
    
    def draw_diag_idicators(self):
        self._draw_throttle_pos_indicator()
        self._draw_oil_temp_indicator()
        self._draw_oil_press_indicator()
        self._draw_coolant_temp_indicator()
        self._draw_fuel_press_indicator()
        self._draw_battery_volt_indicator()

    def draw_limiter_lights(self):
        pass

    def draw_dash(self, dash_vals):
        self.draw_left_gauge()
        self.draw_right_gauge()
        self.draw_diag_idicators()
        self.draw_blinkers()
        self.draw_warning_lights()
        self.draw_limiter_lights()

class OBDInterface:
    def __init__(self) -> None:
        DashValues.rpm = 1337
        DashValues.speed = 69
        DashValues.gear = 5
        DashValues.engine_temp = 85
        DashValues.fuel_level = 80
        DashValues.throttle_pos = 100
        DashValues.oil_temp = 90
        DashValues.oil_press = 60
        DashValues.coolant_temp = 86
        DashValues.fuel_press = 55
        DashValues.battery_volt = 14.5
        DashValues.low_beam_light = True
        DashValues.high_beam_light = True
        DashValues.breaks_warn = True
        DashValues.low_oil_press_warn = True
        DashValues.low_battery_volt_warn = True
        DashValues.check_engine_warn = True
        DashValues.left_blinker = True
        DashValues.right_blinker = True

if __name__ == "__main__":
    dashboard = DashboardGUI()
    obd = OBDInterface()

    while True:
        for event in pygame.event.get():
            dashboard._check_quit()
        dashboard._print_background()
        dashboard.draw_dash(DashValues)
        pygame.display.update()
        dashboard.clock.tick(30)