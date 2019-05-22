import bluetooth 

nearby_devices = bluetooth.discover_devices(lookup_names=True)
def connect():
    print("Working...")
    for name, addr in nearby_devices:
        print (" %s - %s" % (addr, name))
        
        if (name == "BC:B8:63:1E:97:5E"):
            port = 1
            
            sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            
            try:
                sock.connect((name, port))
                print("connected")
                sock.close()
            except:
                print("not connected")