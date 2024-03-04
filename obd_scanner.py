import obd
from dataclasses import dataclass
import time 
import threading
from queue import Queue

@dataclass
class OBDValues:
    rpm: int = 0
    speed: int = 0
    gear: int = 0
    engine_temp: int = 0
    fuel_level: int = 0
    throttle_actuator: int = 0
    throttle_pos: int = 0
    throttle_pos_b: int = 0
    oil_temp: int = 0
    oil_press: int = 0
    coolant_temp: int = 0
    fuel_press: int = 0
    battery_volt: int = 0
    engine_load: int = 0
    intake_pressure: int = 0
    intake_temperature: int = 0
    low_beam_light: bool = False
    high_beam_light: bool = False
    brakes_warn: bool = False
    low_oil_press_warn: bool = False
    low_battery_volt_warn: bool = False
    check_engine_warn: bool = False
    left_blinker: bool = False
    right_blinker: bool = False
    new_data: bool = False


connection = obd.OBD(portstr='COM15', baudrate=38400)

# queue for messages beetwen threads
message_queue = Queue()

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

get_dtc = obd.commands.GET_DTC


def request():
    while True:
        val_rpm = connection.query(rpm)
        val_speed = connection.query(speed)
        val_engine_temp = connection.query(engine_temp)
        val_throttle_actuator = connection.query(throttle_actuator)
        val_throttle_pos = connection.query(throttle_pos)
        val_throttle_pos_b = connection.query(throttle_pos_b)

        val_battery_volt = connection.query(battery_volt)

        # val_val_pids = connection.query(pids)
        val_status = connection.query(status)
        val_fuel_status = connection.query(fuel_status)
        val_engine_load = connection.query(engine_load)

        val_intake_temp = connection.query(intake_temp)
        val_intake_press = connection.query(intake_press)

        val_obd_compliance = connection.query(obd_compliance)

        # pids = val_val_pids.value

        OBDValues.rpm = round(val_rpm.value)
        OBDValues.speed ="speed: ", round(val_speed.value)
        OBDValues.engine_temp = "engine_temp: ", val_engine_temp.value
        OBDValues.throttle_actuator = "throttle_actuator: ", int(val_throttle_actuator.value)
        OBDValues.throttle_pos = "throttle_pos: ", int(val_throttle_pos.value)
        OBDValues.throttle_pos_b = "throttle_pos_b: ", int(val_throttle_pos_b.value)
        OBDValues.battery_volt = "battery_volt: ", val_battery_volt.value
        OBDValues.engine_load = "val_engine_load: ", int(val_engine_load.value)
        OBDValues.intake_temperature = "val_intake_temp: ", val_intake_temp.value
        OBDValues.intake_pressure = "val_intake_press: ", val_intake_press.value
        OBDValues.new_data = True

        time.sleep(1)

def display():
    while True:
        if OBDValues.new_data:
            OBDValues.new_data = False
            print("NEW DATA")

            print("rpm: ", round(OBDValues.rpm.m))
            print("speed: ", round(OBDValues.speed[1].m))
            print("engine_temp: ", OBDValues.engine_temp[1].m)
            print("throttle_actuator: ", int(OBDValues.throttle_actuator[1]))
            print("throttle_pos: ", int(OBDValues.throttle_pos[1]))
            print("throttle_pos_b: ", int(OBDValues.throttle_pos_b[1]))
            print("battery_volt: ", OBDValues.battery_volt[1].m)

            # print("pids: ", OBDValues.pids.value)
            print("val_engine_load: ", int(OBDValues.engine_load[1]))
            print("val_intake_temp: ", OBDValues.intake_temperature[1].m)
            print("val_intake_press: ", OBDValues.intake_pressure[1].m)
        

if __name__ == "__main__":
    t1 = threading.Thread(target = request)
    t1.start()

    t2 = threading.Thread(target = display)
    t2.start()