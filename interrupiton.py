import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM)  


# Setando GPIO 17 como input em borda de decida (apenas quando é pressionado)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# função de Callback
def my_callback(channel):
    print("falling edge detected on 17")

GPIO.add_event_detect(17, GPIO.FALLING, callback=my_callback, boucetime=300)

try:
    print("Iniciou")
except KeyboardInterrupt:
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
GPIO.cleanup()           # clean up GPIO on normal exit  