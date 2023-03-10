# comfortblink
Simple comfortblink for a Raspberry Pi Pico, this was made for a VW Lupo.
You MUST absolutely obtain a relay board and attach it to the pins assigned leftblink and rightblink. I am not responsible for your pico, if you do not. It will fry the board. You also need a 5 volt source wether you use a usb charger or make your own 5 volt power supply is up to you.

You must also attach some relays to your stalk wires, so a relay is closed when chosing direction. The relays are connected to a ground on the pico and the pins assigned for listenleft and listenright. The relays are only to be activated (closed connection), when a direction is chosen. One relay per direction.

Again I am NOT responsible for anything you do to your car, this code is only for your Pico anything beyond the code is not my responsibility.


The following settings can be changed to suit your needs

timeActivated: is the duration in microseconds for which the comfort mode should be on, this all depends on your blinker relay. My value is 3000
checkperiod: Is the check period in microseconds for which the logic checks for a short blink. If you keep the blinker on for more than this value, the blinker is considered permanently on and the timers are disabled.

leftblink: The pin chosen on the board for left side output
rightblink: The pin chosen on the board for right side output
listenleft: The pin chosen on the board for left side input
listenright: The pin chosen on the board for right side input
