import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM)  

# Configurando pino como input de borda de decida
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  
  
# GPIO 24 set up as an input, pulled down, connected to 3V3 on button press  
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  
  
# threaded de callback
# Chama a função quando callback quando um evento é detectado
def my_callback(channel):  
    print ("Faz o que tu quiser")  


# Adicionando evento referente ao pino selecionado
GPIO.add_event_detect(17, GPIO.FALLING, callback=my_callback, bouncetime=300)  


# Esperando o acontecimento de um evento para que o programa nao pare
try:  
    print "Waiting for rising edge on port 24"  
    GPIO.wait_for_edge(24, GPIO.RISING)  
    print "Rising edge detected on port 24. Here endeth the third lesson."  
  
except KeyboardInterrupt:  
    pass