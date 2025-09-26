from gpiozero import OutputDevice
from time import sleep

RELAY_PIN = 17 

# Initialize the OutputDevice for the relay
relay = OutputDevice(RELAY_PIN, initial_value=False)

def turn_on_relay():
    print("Relay ON")
    relay.on()  # Turn the relay on

def turn_off_relay():
    print("Relay OFF")
    relay.off()  # Turn the relay off

try:
    while True:
        command = input("Enter command ('on' to turn on, 'off' to turn off, 'exit' to quit): ").strip().lower()

        if command == 'on':
            turn_on_relay()
        elif command == 'off':
            turn_off_relay()
        elif command == 'exit':
            print("Exiting program.")
            break 
        else:
            print("Invalid command. Please enter 'on', 'off', or 'exit'.")
        
except KeyboardInterrupt:
    print("\nProgram interrupted. Turning relay off.")
    relay.off()  # Ensure the relay is turned off when interrupted
