import board
import pwmio
import supervisor
import time

# Analog Output to Shelly AnIn (PWM simulation)
shelly_out = pwmio.PWMOut(board.GP26, frequency=5000, duty_cycle=0)

def set_voltage(volts):
    duty = int((volts / 3.3) * 65535)
    shelly_out.duty_cycle = max(0, min(65535, duty))

# --- INITIAL POWER-ON STATE ---
# Immediately tell the Shelly we are booting. 
# Do NOT enforce a timeout yet.
current_state = "INITIAL_BOOT"
set_voltage(1.0) 

watchdog_active = False
last_heartbeat = time.monotonic()
TIMEOUT_SECONDS = 6.0

print("RP2040 Active. Initial Boot state holding. Waiting for Linux host...")

while True:
    # Look for the first (and subsequent) signals from the Linux host
    if supervisor.runtime.serial_bytes_available:
        line = supervisor.runtime.readline().decode().strip()
        
        # Once Linux sends its first signal, we arm the watchdog permanently
        if not watchdog_active:
            watchdog_active = True
            print("First handshake received! Watchdog armed.")

        last_heartbeat = time.monotonic()
        
        if line == "BOOTING":
            current_state = "BOOTING"
            set_voltage(1.0)
        elif line == "READY":
            current_state = "READY"
            set_voltage(2.0)
        elif line == "PRINTING":
            current_state = "PRINTING"
            set_voltage(3.0)

    # --- WATCHDOG EXECUTION ---
    # Only evaluate timeouts if the Linux host has successfully checked in at least once
    if watchdog_active:
        if time.monotonic() - last_heartbeat > TIMEOUT_SECONDS:
            current_state = "DEAD"
            set_voltage(0.0) # Drop voltage to 0V → Shelly will cut AC power