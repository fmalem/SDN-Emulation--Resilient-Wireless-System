from mininet.net import Mininet
from mininet.node import  Controller, OVSKernelSwitch, Node, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink, Link
from mininet.wifi import station
from mininet.wifiAssociationControl import associationControl
import time

def topo():
	
#	for i in range(0,1):
#	 num=input("number")
  	
#	 if num==1:
# 		print("yes")
		net=Mininet(controller=RemoteController, link=TCLink, switch=OVSKernelSwitch)
		h1=net.addStation('h1', ip='10.0.1.1/24')
		h2=net.addStation('h2', ip='10.0.1.2/24')
		h3=net.addStation('h3', ip='10.0.1.3/24')
		h4=net.addStation('h4', ip='10.0.1.4/24')
		attacker=net.addStation('attacker', ip='10.0.1.200/24')
		ap1=net.addBaseStation('ap1',ssid='firas_1', mode='g',channel=1, position='15,30,10')
		ap2=net.addBaseStation('ap2',ssid='firas_2', mode='g', channel=2, position='15,40,10')
		ap3=net.addBaseStation('ap3',ssid='firas_3',mode='g',channel=5, position='15,30,20')	
		ap4=net.addBaseStation('ap4',ssid='firas_4',mode='g',channel=3, position='15,40,20')	
		ap5=net.addBaseStation('ap5',ssid='attacker',mode='g',channel=5, position='15,30,20')	
		c0=net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6633)	
		
		net.addLink(ap1,ap2)
		net.addLink(ap1,h1)
		net.addLink(ap1,h2)
		net.addLink(ap2,h3)
		net.addLink(ap2,h4)
		net.addLink(ap5,attacker)					
		net.start()
		result=h1.cmd('iwconfig')
		print result
		result6=h1.cmd('ifconfig')
		print result6
		h1.config(ip='10.0.1.5/24')
		h2.config(ip='10.0.1.6/24')
		h3.config(ip='10.0.1.7/24')
		h4.config(ip='10.0.1.8/24')
		h1.cmd('iw dev h1-wlan0 disconnect')
		h1.cmd('iw dev h1-wlan0 connect firas_3')
		h2.cmd('iw dev h2-wlan0 disconnect')
		h2.cmd('iw dev h2-wlan0 connect firas_3')
		h3.cmd('iw dev h3-wlan0 disconnect')
		h3.cmd('iw dev h3-wlan0 connect firas_4')
		h4.cmd('iw dev h4-wlan0 disconnect')
		h4.cmd('iw dev h4-wlan0 connect firas_4')
		ap1.cmd('ip link delete ap1-eth1')
		ap2.cmd('ip link delete ap2-eth1')
		net.addLink(ap3,ap4)
		time.sleep(5)
		result=h1.cmd('iwconfig')
		print result
		result2=h1.cmd('ifconfig')
		print result2	
		result3=h2.cmd('iwconfig')
		print result3
		result4=h2.cmd('ifconfig')
		print result4
		result8=h4.cmd('iwconfig')
		print result8
		time.sleep(5)
		h1.cmd('route add default gw 10.0.1.10')
		h2.cmd('route add default gw 10.0.1.10')
		h3.cmd('route add default gw 10.0.1.20')
		h4.cmd('route add default gw 10.0.1.20')
		time.sleep(1)
		CLI(net)
		net.stop()

if __name__== '__main__':
	setLogLevel('info')
	topo()
