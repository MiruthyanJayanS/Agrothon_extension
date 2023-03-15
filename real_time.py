def real_time():
    import serial
    # ser = serial.Serial('/dev/cu.usbmodem101', 9800, timeout=1)
    try:
        try:
            ser = serial.Serial('/dev/cu.usbmodem1101', 9800, timeout=3)
            humidity, temperature, moisture = ser.readline().decode().split()[1],ser.readline().decode().split()[1],ser.readline().decode().split()[1]
        except:
            # ser = serial.Serial('/dev/cu.usbmodem101', 9800, timeout=5)
            ser = serial.Serial('/dev/cu.usbmodem1101', 9800, timeout=5)
            humidity, temperature, moisture = ser.readline().decode().split()[1],ser.readline().decode().split()[1],ser.readline().decode().split()[1]
        return [humidity, temperature, moisture]
    except:
        try:
            ser = serial.Serial('/dev/cu.usbmodem101', 9800, timeout=3)
            humidity, temperature, moisture = ser.readline().decode().split()[1],ser.readline().decode().split()[1],ser.readline().decode().split()[1]
        except:
            ser = serial.Serial('/dev/cu.usbmodem101', 9800, timeout=5)
            humidity, temperature, moisture = ser.readline().decode().split()[1],ser.readline().decode().split()[1],ser.readline().decode().split()[1]
    return [humidity, temperature, moisture]
#     print("Humidity: ", humidity,"%")
#     print("Temperature: ", temperature,"C")
#     print("Moisture: ", moisture,"%")

# real_time()