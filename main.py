"""

Inputs: IOF5

-------------

Schwelle ist 803 digit

-------------

Spannung an I1 = 3,3V

Spannung an Microbit Low =  0,82V (= 254 digit)

Spannung an Microbit High = 2,6V  (= 803 digit)

--------------

--> Schaltschwelle = 1,7 V = 528 digit

"""

def on_forever():
    if pins.analog_read_pin(AnalogReadWritePin.P1) > 500:
        pins.digital_write_pin(DigitalPin.P16, 1)
    else:
        pins.digital_write_pin(DigitalPin.P16, 0)
    if pins.digital_read_pin(DigitalPin.P1) > 0:
        led.plot(0, 0)
    else:
        led.unplot(0, 0)
    if pins.digital_read_pin(DigitalPin.P1) == 1:
        led.plot(0, 1)
    else:
        led.unplot(0, 1)
    if (0) > (2000):
        led.plot(0, 2)
    else:
        led.unplot(0, 2)
    kitronik_VIEW128x64.show(pins.analog_read_pin(AnalogReadWritePin.P1),
        1,
        kitronik_VIEW128x64.ShowAlign.LEFT)
basic.forever(on_forever)
