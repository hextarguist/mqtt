#python3
import paho.mqtt.publish as publish
import time
import sys

while True:
   print("Sending 1...")
   publish.single("led1", "1", hostname="10.181.1.1")
   publish.single("led2", "1", hostname="10.181.1.1")
   publish.single("led3", "1", hostname="10.181.1.1")
   time.sleep(10)

   print("Sending 0...")
   publish.single("led1", "0", hostname="10.181.1.1")
   publish.single("led2", "0", hostname="10.181.1.1")
   publish.single("led3", "0", hostname="10.181.1.1")
   time.sleep(10)

         
try:
  while True:
       print("Heavy task!")
except KeyboardInterrupt:
       print("KeyboardInterrupt has been caught.")
