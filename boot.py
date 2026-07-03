import supervisor
import usb_cdc

# Customize how the board reports its identity to Linux
supervisor.set_usb_identification(
    manufacturer="Vylyne",
    product="Host-Watchdog"
)

# Optional: Disable the standard CIRCUITPY storage drive showing up on the printer host
# storage.disable_usb_drive() 

# Ensure the standard serial port interface remains enabled
usb_cdc.enable(console=True, data=False)