import board
import digitalio
print("BEGIN INIT")
# Setup address lines
addressLinesPinNums = [board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15]
addressLinesPinObjects = []
for pin in addressLinesPinNums:
    pin = digitalio.DigitalInOut(pin)
    pin.direction = digitalio.Direction.INPUT
    addressLinesPinObjects.append(pin)
    print("Setup address line")
print("END INIT")

# Read & Loop
while True:
    # Collect values
    pinValues = []
    for pin in addressLinesPinObjects:
        if pin.value:
            pinValues.append(1)
        else:
            pinValues.append(0)
    # Display
    text = ""
    for pin in pinValues:
        text = text + str(pin)
    print(text)