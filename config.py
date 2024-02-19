# dashboard's config

# font name
FONT_NAME = "Lato-Regular.ttf"

FUEL_LVL_TXT = "Fuel Level"
ENGINE_TEMP_TXT = "Engine Temperature"
GEAR_TXT = "Gear"
SPEED_TXT = "Speed"

THRTTL_POS_TXT = "Throttle Position"
OIL_TEMP_TXT = "Oil Temperature"
OIL_PRESS_TXT = "Oil Pressure"
COOLANT_TEMP_TXT = "Coolant Temperature"
FUEL_PRESS_TXT = "Fuel Pressure"
BATT_VLTG_TXT = "Battery Voltage"

GRAPHICS_PATH = "graphics/"

NO_LIGHT = GRAPHICS_PATH + "no_light.png"

RPM_GAUGE = GRAPHICS_PATH + "rpm_gauge.png" # not existing at the moment
SPEED_GAUGE = GRAPHICS_PATH + "speed_gauge.png" # not existing at the moment 

LEFT_BLINKER_PATH = GRAPHICS_PATH + "blinker_left.png"
RIGHT_BLINKER_PATH = GRAPHICS_PATH + "blinker_right.png"

FUEL_LVL_PATH = GRAPHICS_PATH + "fuel_level.png"
ENGINE_TEMP_PATH = GRAPHICS_PATH + "engine_temp.png"

LOW_BEAM_PATH = GRAPHICS_PATH + "low_beams.png"
HIGH_BEAM_PATH = GRAPHICS_PATH + "high_beams.png"
BRAKE_PATH = GRAPHICS_PATH + "brakes.png"
OIL_LEVEL_PATH = GRAPHICS_PATH + "oil_level.png"
BATTERY_PATH = GRAPHICS_PATH + "battery.png"
CHECK_ENGINE_PATH = GRAPHICS_PATH + "check_engine.png"

'''
features:
- two radial gauges: speed and rpm,
- fuel and  temperature radial gauges inside rpm gauge,
- gear idndicator,
- speed indicator inside speed gauge,
- digital gauges: throttle possition, oil temperature, oil pressure, coolant temperaturek, fuel pressure, battery voltage,
- rpm limiter lights,
- warning light: low oil pressure, low battery voltage, check engine, parking brake,
- low beam indicator,
- high beam indicator
'''