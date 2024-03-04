import obd
from dataclasses import dataclass
from time import sleep
import threading
from queue import Queue

@dataclass
class OBDValues:
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


connection = obd.OBD(portstr='COM15', baudrate=38400)



rpm = obd.commands.RPM
speed = obd.commands.SPEED
# gear
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
# oil_press = obd.commands.OIL_PRESS
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

get_dtc = obd.commands.GET_DTC

# val_fuel_level = connection.query(fuel_level) # not supported
# val_throttle_pos_c = connection.query(throttle_pos_c) # not supported

# val_accelerator_pos_d = connection.query(accelerator_pos_d) # not supported
# val_accelerator_pos_e = connection.query(accelerator_pos_e) # not supported
# val_accelerator_pos_f = connection.query(accelerator_pos_f) # not supported

# val_oil_temp = connection.query(oil_temp)
# val_oil_press = connection.query(oil_press) # not supported
# val_fuel_press = connection.query(fuel_press) # not supportedv

# val_freeze_dtc = connection.query(freeze_dtc)
# val_fuel_rail_press = connection.query(fuel_rail_press)

while True:
    val_rpm = connection.query(rpm)
    val_speed = connection.query(speed)
    val_engine_temp = connection.query(engine_temp)
    val_throttle_actuator = connection.query(throttle_actuator)
    val_throttle_pos = connection.query(throttle_pos)
    val_throttle_pos_b = connection.query(throttle_pos_b)

    val_battery_volt = connection.query(battery_volt)

    val_val_pids = connection.query(pids)
    val_status = connection.query(status)
    val_fuel_status = connection.query(fuel_status)
    val_engine_load = connection.query(engine_load)

    val_intake_temp = connection.query(intake_temp)
    val_intake_press = connection.query(intake_press)

    val_obd_compliance = connection.query(obd_compliance)

    print("rpm: ", round(val_rpm.value))
    print("speed: ", round(val_speed.value))
    print("engine_temp: ", val_engine_temp.value)
    print("throttle_actuator: ", int(val_throttle_actuator.value))
    print("throttle_pos: ", int(val_throttle_pos.value))
    print("throttle_pos_b: ", int(val_throttle_pos_b.value))
    print("battery_volt: ", val_battery_volt.value)

    print("pids: ", val_val_pids.value)
    print("val_engine_load: ", int(val_engine_load.value))
    print("val_intake_temp: ", val_intake_temp.value)
    print("val_intake_press: ", val_intake_press.value)

    sleep(1)


print("done")
#print(response.value.to())
