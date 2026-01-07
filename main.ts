// Inputs: IOF5
// 
// -------------
// 
// Schwelle ist 803 digit
// 
// -------------
// 
// Spannung an I1 = 3,3V
// 
// Spannung an Microbit Low =  0,82V (= 254 digit)
// 
// Spannung an Microbit High = 2,6V  (= 803 digit)
// 
// --------------
// 
// --> Schaltschwelle = 1,7 V = 528 digit
I2C_LCD1602.on()
I2C_LCD1602.LcdInit(1)
I2C_LCD1602.ShowNumber(10, 0, 0)
I2C_LCD1602.ShowString("Hello", 0, 0)
basic.forever(function () {
    I2C_LCD1602.LcdInit(0)
    kitronik_VIEW128x64.refresh()
})
