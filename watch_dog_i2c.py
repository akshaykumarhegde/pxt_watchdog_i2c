from smbus2 import SMBus

with SMBus(2) as bus:
    # Write a byte to address 80, offset 0
    data = 45
    bus.write_byte_data(0x08, 0, data)
