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

    def _check_arrow_keys(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                DashValues.rpm += 400
                if DashValues.rpm > 8000:
                    DashValues.rpm = 8000
            if event.key == pygame.K_DOWN:
                DashValues.rpm -= 400
                if DashValues.rpm < 0:
                    DashValues.rpm = 0
    
    def _print_background(self):
        font = pygame.font.Font(config.FONT_NAME, 16)

        text = font.render(str(config.GEAR_TXT), 0, "white")
        self.window.blit(text, (512, 150))

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

    def rotatePivoted(self, image, angle, pivot):
    # rotate the leg image around the pivot
        rotated_image = pygame.transform.rotate(image, angle)
        rect = rotated_image.get_rect()
        rect.center = pivot
        return rotated_image, rect

    def _draw_rpm_gauge(self, rpm: DashValues):
        rpm_gauge_cords = (80, 90)
        rpm_needle_cords = (80 + 155, 90 + 120)
        rpm_zero_offset = 193
        rpm_angle = rpm_zero_offset - (rpm / 30)
        rpm_zero_pivot = (260, 280)
        # rpm_zero_pivot = (512, 256)

        image = pygame.image.load(config.RPM_GAUGE_PATH)
        self.window.blit(image, rpm_gauge_cords)

        image = pygame.image.load(config.RPM_NEEDLE_PATH)
        # image = pygame.transform.rotate(image, rpm_zero_offset)
        # image_rect = image.get_rect(topleft=rpm_needle_cords)
        rotated_image, rect = self.rotatePivoted(image, rpm_angle, rpm_zero_pivot)
        self.window.blit(rotated_image, rect)
    
    def _draw_speed_gauge(self, dash_vals: DashValues):
        speed_gauge_cords = (600, 90)
        speed_needle_cords = (590 + 165, 90 + 150)
        
        image = pygame.image.load(config.SPEED_GAUGE_PATH)
        self.window.blit(image, speed_gauge_cords)

        image = pygame.image.load(config.SPEED_NEEDLE_PATH)
        self.window.blit(image, speed_needle_cords)
    
    def _draw_speed_indicator(self, dash_vals: DashValues):
        pass
    
    def draw_gear_idicator(self, dash_vals: DashValues):
        font = pygame.font.Font(config.FONT_NAME, 100)

        gear_text = str(DashValues.gear)
        text = font.render(gear_text, 0, "white")
        self.window.blit(text, (500, 200))
    
    def _draw_engine_temp_gauge(self, dash_vals: DashValues):
        pass
    
    def _draw_fuel_level_gauge(self, dash_vals: DashValues):
        pass
    
    def _draw_throttle_pos_indicator(self, throttle_pos: int):
        throttle_pos_text = str(throttle_pos)

        font = pygame.font.Font(config.FONT_NAME, 36)
        text = font.render(throttle_pos_text, 0, "white")
        self.window.blit(text, (65, 530))

    def _draw_oil_temp_indicator(self, oil_temp: int):
        oil_temp_text = str(oil_temp)

        font = pygame.font.Font(config.FONT_NAME, 36)
        text = font.render(oil_temp_text, 0, "white")
        self.window.blit(text, (235, 530))

    def _draw_oil_press_indicator(self, oil_press: int):
        oil_press_text = str(oil_press)

        font = pygame.font.Font(config.FONT_NAME, 36)
        text = font.render(oil_press_text, 0, "white")
        self.window.blit(text, (391, 530))

    def _draw_coolant_temp_indicator(self, coolant_temp: int):
        coolant_temp_text = str(coolant_temp)

        font = pygame.font.Font(config.FONT_NAME, 36)
        text = font.render(coolant_temp_text, 0, "white")
        self.window.blit(text, (590, 530))

    def _draw_fuel_press_indicator(self, fuel_press: int):
        fuel_press_text = str(fuel_press)

        font = pygame.font.Font(config.FONT_NAME, 36)
        text = font.render(fuel_press_text, 0, "white")
        self.window.blit(text, (755, 530))

    def _draw_battery_volt_indicator(self, battery_volt: float):
        battery_volt_text = str(battery_volt)

        font = pygame.font.Font(config.FONT_NAME, 36)
        text = font.render(battery_volt_text, 0, "white")
        self.window.blit(text, (910, 530))

    def draw_left_gauge(self, dash_vals: DashValues):
        self._draw_rpm_gauge(dash_vals.rpm)
        self._draw_fuel_level_gauge(dash_vals.fuel_level)
        self._draw_engine_temp_gauge(dash_vals.engine_temp)

    def draw_right_gauge(self, dash_vals: DashValues):
        self._draw_speed_gauge(dash_vals.speed)
        self._draw_speed_indicator(dash_vals.speed)

    def _draw_low_beam_light(self, low_beam_light: bool):
        if low_beam_light:
            image = pygame.image.load(config.LOW_BEAM_PATH)
        else:
            image = pygame.image.load(config.NO_LIGHT)
        self.window.blit(image, (470, 320))

    def _draw_high_beam_light(self, high_beam_light: bool):
        if high_beam_light:
            image = pygame.image.load(config.HIGH_BEAM_PATH)
        else:
            image = pygame.image.load(config.NO_LIGHT)
        self.window.blit(image, (530, 320))

    def _draw_brake_light(self, brakes_warn: bool):
        if brakes_warn:
            image = pygame.image.load(config.BRAKE_PATH)
        else:
            image = pygame.image.load(config.NO_LIGHT)
        self.window.blit(image, (470, 360))

    def _draw_oil_level_light(self, low_oil_press_warn: bool):
        if low_oil_press_warn:
            image = pygame.image.load(config.OIL_LEVEL_PATH)
        else:
            image = pygame.image.load(config.NO_LIGHT)
        self.window.blit(image, (530, 360))

    def _draw_battery_light(self, battery_volt_warn: bool):
        if battery_volt_warn:
            image = pygame.image.load(config.BATTERY_PATH)
        else:
            image = pygame.image.load(config.NO_LIGHT)
        self.window.blit(image, (470, 400))

    def _draw_check_engine(self, check_engine_warn: bool):
        if check_engine_warn:
            image = pygame.image.load(config.CHECK_ENGINE_PATH)
        else:
            image = pygame.image.load(config.NO_LIGHT)
        self.window.blit(image, (530, 400))

    def draw_warning_lights(self, dash_vals: DashValues):
        self._draw_low_beam_light(dash_vals.low_beam_light)
        self._draw_high_beam_light(dash_vals.high_beam_light)
        self._draw_brake_light(dash_vals.breaks_warn)
        self._draw_oil_level_light(dash_vals.low_oil_press_warn)
        self._draw_battery_light(dash_vals.low_battery_volt_warn)
        self._draw_check_engine(dash_vals.check_engine_warn)

    def _draw_left_blinker(self, left_blinker: bool):
        if left_blinker:
            image = pygame.image.load(config.LEFT_BLINKER_PATH)
        else:
            image = pygame.image.load(config.NO_LIGHT)
        self.window.blit(image, (512-30, 100))

    def _draw_right_blinker(self, right_blinker: bool):
        if right_blinker:
            image = pygame.image.load(config.RIGHT_BLINKER_PATH)
        else:
            image = pygame.image.load(config.NO_LIGHT)
        self.window.blit(image, (512+30, 100))

    def draw_blinkers(self, dash_vals: DashValues):
        self._draw_left_blinker(dash_vals.left_blinker)
        self._draw_right_blinker(dash_vals.right_blinker)
    
    def draw_diag_idicators(self, dash_vals: DashValues):
        self._draw_throttle_pos_indicator(dash_vals.throttle_pos)
        self._draw_oil_temp_indicator(dash_vals.oil_temp)
        self._draw_oil_press_indicator(dash_vals.oil_press)
        self._draw_coolant_temp_indicator(dash_vals.coolant_temp)
        self._draw_fuel_press_indicator(dash_vals.fuel_press)
        self._draw_battery_volt_indicator(dash_vals.battery_volt)

    def _rpm_to_lights(self, rpm):
        greens = min(max((rpm - 4000) // 400, 0), 3)
        oranges = min(max((rpm - 5000) // 400, 0), 3)
        reds = min(max((rpm - 6000) // 400, 0), 3)

        return greens, oranges, reds

    def _turn_on_light(self, lights, start_cords, image):
        print(lights)
        for i in range(1, lights + 1):
            self.window.blit(image, (start_cords[0] + (i*40), start_cords[1]))

    def draw_limiter_lights(self, dash_vals: DashValues):
        nr_of_limit_lights = 18
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
        greens, oranges, reds = self._rpm_to_lights(dash_vals.rpm)

        print("lights: ", greens, " ", oranges, " ", "rpm: ", reds, dash_vals.rpm, "angle: ", dash_vals.rpm / 50)

        # zero out the lights
        for i in range(nr_of_limit_lights):
            self.window.blit(grey_light, (i*light_spacing + offset, 10))

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
        # TODO: dodac mirror() do limit lights

    def draw_dash(self, dash_vals: DashValues):
        self.draw_limiter_lights(dash_vals)
        self.draw_gear_idicator(dash_vals)
        self.draw_left_gauge(dash_vals)
        self.draw_right_gauge(dash_vals)
        self.draw_diag_idicators(dash_vals)
        self.draw_blinkers(dash_vals)
        self.draw_warning_lights(dash_vals)


class OBDInterface:
    def __init__(self) -> None:
        DashValues.rpm = 8000
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
            dashboard._check_arrow_keys()
        dashboard._print_background()
        dashboard.draw_dash(DashValues)
        pygame.display.update()
        dashboard.clock.tick(30)