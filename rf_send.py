import logging

from rpi_rf import RFDevice

logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)-15s - [%(levelname)s] %(module)s: %(message)s',)

codes = {"on": 1052693, "off": 1052692}

def control_light(code):
    rfdevice = RFDevice(17)
    rfdevice.enable_tx()

    protocol = 1
    pulselength = 380

    logging.info("code: {0}".format(code) +
                 " [protocol: " + str(protocol) +
                 ", pulselength: " + str(pulselength) + "]")

    rfdevice.tx_code(codes[code], protocol, pulselength)
    rfdevice.cleanup()
