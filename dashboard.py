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
    brakes_warn: bool = False
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

    def _check_keyboard(self):
        '''
        DashValues.rpm = 0
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
        DashValues.brakes_warn = True
        DashValues.low_oil_press_warn = True
        DashValues.low_battery_volt_warn = True
        DashValues.check_engine_warn = True
        DashValues.left_blinker = True
        DashValues.right_blinker = True
        '''
        if event.type == pygame.KEYDOWN:
            # numbers:
            if event.key == pygame.K_a:
                DashValues.rpm += 400
                if DashValues.rpm > 8000:
                    DashValues.rpm = 8000
                print("rpm: ", DashValues.rpm)
            if event.key == pygame.K_z:
                DashValues.rpm -= 400
                if DashValues.rpm < 0:
                    DashValues.rpm = 0
                print("rpm: ", DashValues.rpm)

            if event.key == pygame.K_s:
                DashValues.speed += 10
                if DashValues.speed > 200:
                    DashValues.speed = 200
                print("speed: ", DashValues.speed)
            if event.key == pygame.K_x:
                DashValues.speed -= 10
                if DashValues.speed < 0:
                    DashValues.speed = 0
                print("speed: ", DashValues.speed)

            if event.key == pygame.K_d:
                DashValues.gear += 1
                if DashValues.gear > 6:
                    DashValues.gear = 6
                print("gear: ", DashValues.gear)
            if event.key == pygame.K_c:
                DashValues.gear -= 1
                if DashValues.gear < 0:
                    DashValues.gear = 0
                print("gear: ", DashValues.gear)
            
            if event.key == pygame.K_f:
                DashValues.engine_temp += 10
                if DashValues.engine_temp > 130:
                    DashValues.engine_temp = 130
                print("engine_temp: ", DashValues.engine_temp)
            if event.key == pygame.K_v:
                DashValues.engine_temp-= 10
                if DashValues.engine_temp < 0:
                    DashValues.engine_temp= 0
                print("engine_temp: ", DashValues.engine_temp)
            
            if event.key == pygame.K_g:
                DashValues.fuel_level += 10
                if DashValues.fuel_level > 100:
                    DashValues.fuel_level = 100
                print("fuel_level: ", DashValues.fuel_level)
            if event.key == pygame.K_b:
                DashValues.fuel_level -= 10
                if DashValues.fuel_level < 0:
                    DashValues.fuel_level = 0
                print("fuel_level: ", DashValues.fuel_level)
            
            if event.key == pygame.K_h:
                DashValues.oil_press += 10
                if DashValues.oil_press > 100:
                    DashValues.oil_press = 100
                print("oil_press: ", DashValues.oil_press)
            if event.key == pygame.K_n:
                DashValues.oil_press -= 10
                if DashValues.oil_press < 0:
                    DashValues.oil_press = 0
                print("oil_press: ", DashValues.oil_press)

            if event.key == pygame.K_j:
                DashValues.coolant_temp += 10
                if DashValues.coolant_temp > 150:
                    DashValues.coolant_temp = 150
                print("coolant_temp: ", DashValues.coolant_temp)
            if event.key == pygame.K_m:
                DashValues.coolant_temp -= 10
                if DashValues.coolant_temp < 0:
                    DashValues.coolant_temp = 0
                print("coolant_temp: ", DashValues.coolant_temp)
            
            if event.key == pygame.K_k:
                DashValues.fuel_press += 10
                if DashValues.fuel_press > 100:
                    DashValues.fuel_press = 100
                print("fuel_press: ", DashValues.fuel_press)
            if event.key == pygame.K_COMMA:
                DashValues.fuel_press -= 10
                if DashValues.fuel_press < 0:
                    DashValues.fuel_press = 0
                print("fuel_press: ", DashValues.fuel_press)
            
            if event.key == pygame.K_l:
                DashValues.battery_volt += 1
                if DashValues.battery_volt > 15:
                    DashValues.battery_volt = 15
                print("battery_volt: ", DashValues.battery_volt)
            if event.key == pygame.K_PERIOD:
                DashValues.battery_volt -= 1
                if DashValues.battery_volt < 0:
                    DashValues.battery_volt = 0
                print("battery_volt: ", DashValues.battery_volt)

            # bools:
            if event.key == pygame.K_q:
                DashValues.low_beam_light = not(DashValues.low_beam_light)
            if event.key == pygame.K_w:
                DashValues.high_beam_light = not(DashValues.high_beam_light)
            if event.key == pygame.K_e:
                DashValues.brakes_warn = not(DashValues.brakes_warn)
            if event.key == pygame.K_r:
                DashValues.low_oil_press_warn = not(DashValues.low_oil_press_warn)
            if event.key == pygame.K_t:
                DashValues.low_battery_volt_warn = not(DashValues.low_battery_volt_warn)
            if event.key == pygame.K_y:
                DashValues.check_engine_warn = not(DashValues.check_engine_warn)
            if event.key == pygame.K_u:
                DashValues.left_blinker = not(DashValues.left_blinker)
            if event.key == pygame.K_i:
                DashValues.right_blinker = not(DashValues.right_blinker)

    
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
        speed_angle = speed_zero_offset - (speed / 26.6)
        
        image = pygame.image.load(config.SPEED_GAUGE_PATH)
        self.window.blit(image, speed_gauge_cords)

        image = pygame.image.load(config.SPEED_NEEDLE_PATH)
        rotated_image, rect = self.rotatePivoted(image, speed_angle, speed_needle_cords)
        self.window.blit(rotated_image, rect)
    
    def _draw_speed_indicator(self, speed: DashValues.speed):
        pass
    
    def draw_gear_idicator(self, gear: DashValues.gear):
        font = pygame.font.Font(config.FONT_NAME, 100)

        gear_text = str(DashValues.gear)
        text = font.render(gear_text, 0, "white")
        self.window.blit(text, (500, 200))
    
    def _draw_engine_temp_gauge(self, engine_temp: DashValues.engine_temp):
        pass
    
    def _draw_fuel_level_gauge(self, fuel_level: DashValues.fuel_level):
        pass
    
    def _draw_throttle_pos_indicator(self, throttle_pos: DashValues.throttle_pos):
        throttle_pos_text = str(throttle_pos)

        font = pygame.font.Font(config.FONT_NAME, 36)
        text = font.render(throttle_pos_text, 0, "white")
        self.window.blit(text, (65, 530))

    def _draw_oil_temp_indicator(self, oil_temp: DashValues.oil_temp):
        oil_temp_text = str(oil_temp)

        font = pygame.font.Font(config.FONT_NAME, 36)
        text = font.render(oil_temp_text, 0, "white")
        self.window.blit(text, (235, 530))

    def _draw_oil_press_indicator(self, oil_press: DashValues.oil_press):
        oil_press_text = str(oil_press)

        font = pygame.font.Font(config.FONT_NAME, 36)
        text = font.render(oil_press_text, 0, "white")
        self.window.blit(text, (391, 530))

    def _draw_coolant_temp_indicator(self, coolant_temp: DashValues.coolant_temp):
        coolant_temp_text = str(coolant_temp)

        font = pygame.font.Font(config.FONT_NAME, 36)
        text = font.render(coolant_temp_text, 0, "white")
        self.window.blit(text, (590, 530))

    def _draw_fuel_press_indicator(self, fuel_press: DashValues.fuel_press):
        fuel_press_text = str(fuel_press)

        font = pygame.font.Font(config.FONT_NAME, 36)
        text = font.render(fuel_press_text, 0, "white")
        self.window.blit(text, (755, 530))

    def _draw_battery_volt_indicator(self, battery_volt: DashValues.battery_volt):
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
        self._draw_throttle_pos_indicator(dash_vals.throttle_pos)
        self._draw_oil_temp_indicator(dash_vals.oil_temp)
        self._draw_oil_press_indicator(dash_vals.oil_press)
        self._draw_coolant_temp_indicator(dash_vals.coolant_temp)
        self._draw_fuel_press_indicator(dash_vals.fuel_press)
        self._draw_battery_volt_indicator(dash_vals.battery_volt)

    def _rpm_to_lights(self, rpm: DashValues.rpm):
        greens = min(max((rpm - 4000) // 400, 0), 3)
        oranges = min(max((rpm - 5000) // 400, 0), 3)
        reds = min(max((rpm - 6000) // 400, 0), 3)

        return greens, oranges, reds

    def _turn_on_light(self, lights, start_cords, image):
        print(lights)
        for i in range(1, lights + 1):
            self.window.blit(image, (start_cords[0] + (i*40), start_cords[1]))

    def draw_limiter_lights(self, rpm: DashValues.rpm):
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
        greens, oranges, reds = self._rpm_to_lights(rpm)

        # print("lights: ", greens, " ", oranges, " ", "rpm: ", reds, rpm, "angle: ", rpm / 50)

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
        self.draw_limiter_lights(dash_vals.rpm)
        self.draw_gear_idicator(dash_vals.gear)
        self.draw_left_gauge(dash_vals)
        self.draw_right_gauge(dash_vals)
        self.draw_diag_idicators(dash_vals)
        self.draw_blinkers(dash_vals)
        self.draw_warning_lights(dash_vals)


class OBDInterface:
    def __init__(self) -> None:
        # DashValues.rpm = 0
        # DashValues.speed = 69
        # DashValues.gear = 5
        # DashValues.engine_temp = 85
        # DashValues.fuel_level = 80
        # DashValues.throttle_pos = 100
        # DashValues.oil_temp = 90
        # DashValues.oil_press = 60
        # DashValues.coolant_temp = 86
        # DashValues.fuel_press = 55
        # DashValues.battery_volt = 14.5
        # DashValues.low_beam_light = True
        # DashValues.high_beam_light = True
        # DashValues.brakes_warn = True
        # DashValues.low_oil_press_warn = True
        # DashValues.low_battery_volt_warn = True
        # DashValues.check_engine_warn = True
        # DashValues.left_blinker = True
        # DashValues.right_blinker = True
        pass

if __name__ == "__main__":
    dashboard = DashboardGUI()
    obd = OBDInterface()

    while True:
        for event in pygame.event.get():
            dashboard._check_quit()
            dashboard._check_arrow_keys()
            dashboard._check_keyboard()
        dashboard._print_background()
        dashboard.draw_dash(DashValues)
        pygame.display.update()
        dashboard.clock.tick(30)