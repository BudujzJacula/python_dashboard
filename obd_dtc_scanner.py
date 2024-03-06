import obd

connection = obd.OBD(portstr='COM15', baudrate=38400)

def main():
    cmd = obd.commands.GET_DTC
    val_cmd = connection.query(cmd)
    print("DTCs: ", val_cmd)

if __name__ == "__main__":
    main()