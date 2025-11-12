##  Begin Standard Imports

##  Begin Local Imports
from model.exp1 import exp1Topo

##  Begin `mininet` Imports
from mininet.net import Mininet
from mininet.node import Node, OVSKernelSwitch, Controller, RemoteController, DefaultController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def main(**kwargs):
    tmp1:exp1Topo = exp1Topo()
    setLogLevel("info")
    net = Mininet(topo=tmp1, switch=OVSKernelSwitch, controller=DefaultController, autoSetMacs=True)
    net.start()
    
    net["h1"].cmd("/usr/sbin/sshd")
    net["h2"].cmd("/usr/sbin/sshd")
    net["h3"].cmd("/usr/sbin/sshd")

    net["h1"].cmd("ip route add default via 10.0.0.254")
    net["h2"].cmd("ip route add default via 10.0.3.254")
    net["h3"].cmd("ip route add default via 10.0.2.254")

    CLI(net)
    net.stop()

if __name__ == "__main__":
    main()