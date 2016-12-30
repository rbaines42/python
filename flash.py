from blinkt import set_brightness, set_pixel, clear,show
import time
while True:
    clear()
    show()
    time.sleep(1)
    set_pixel(0,255,255,255)
    show()
    time.sleep(1)
