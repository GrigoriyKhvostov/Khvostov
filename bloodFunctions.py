import spidev

########################################
#   Open, use and close SPI ADC
########################################

########################################
# Do not forget to setup GPIO pins to SPI functions!
#
# Enter the followig commands into RPi terminal:
#
# raspi-gpio get
# raspi-gpio set 9 a0
# raspi-gpio set 10 a0
# raspi-gpio set 11 a0
# raspi-gpio get
########################################

spi = spidev.SpiDev()

def initSpiAdc():
    spi.open(0, 0)
    spi.max_speed_hz = 1600000
    print ("SPI for ADC have been initialized")

def deinitSpiAdc():
    spi.close()
    print ("SPI cleanup finished")

def getAdc():
    adcResponse = spi.xfer2([0, 0])
    return ((adcResponse[0] & 0x1F) << 8 | adcResponse[1]) >> 1