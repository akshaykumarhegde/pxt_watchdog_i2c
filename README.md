https://pypi.org/project/smbus2/  -----> i2c lib

commands
   41  sudo i2cdetect -y 1
   42  sudo reboot
   43  sudo i2cdetect -y 1
   44  sudo i2cdetect -y 0
   45  sudo i2cdetect -y 3
   46  sudo i2cdetect -y 4
   47  sudo i2cdetect -y 3
   48  sudo i2cdetect -y 0
   49  sudo i2cdetect -y 1
   50  sudo i2cdetect -y 2
   51  sudo apt-get install python-smbus python-dev
   52  sudo nano /etc/modules
   53  sudo adduser pi i2c
   54  sudo adduser orangepi i2c
   55  sudo reboot
