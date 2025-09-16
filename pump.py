#from AI value 
import os
#import needed files and API 


def pump():
    pump =  int(os.getenv("PUMP_PIN")) #fetch data from AI
    print("Pump activated")
    #GPIO code to activate pump for 'amount' duration
    # Your pump activation logic here