# Raspberry Pi Weather Station

This code runs a basic temperature and pressure weather station using the BMP085/180 I2C sensor.



### Setup
#### Activate I2C Drivers
On your Raspberry Pi, you must first enable the I2C drivers.
1. Run `sudo raspi-config`
2. At the menu, choose option `8. Advanced Options`
3. Select `A7 I2C` and then say "Yes" to enable the I2C driver and "Yes" again to load the driver by default
4. Reboot your Raspberry Pi by running `sudo reboot` back at the command line

#### Install BMP085/180 drivers
Then, run the following commands to install the needed libraries

{% highlight bash %}
sudo apt-get update
sudo apt-get install git build-essential python-dev python-smbus
git clone https://github.com/adafruit/Adafruit_Python_BMP.git
cd Adafruit_Python_BMP
sudo python setup.py install
{% endhighlight %}

#### Install Flask Bootstrap Module
```bash
sudo pip install flask-bootstrap
```


