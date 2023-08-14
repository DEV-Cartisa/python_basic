
import speedtest
wifi = speedtest.Speedtest()
print('Wifi Donload Speed', wifi.download())
print('Wifi Upload Speed', wifi.upload())

