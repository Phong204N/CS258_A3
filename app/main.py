##  Begin Standard Imports

##  Begin Local Imports
from model.exp1 import exp1Topo

##  Begin `mininet` Imports
from mininet.net import Mininet
from mininet.node import Node, OVSKernelSwitch, Controller, RemoteController, DefaultController
from mininet.cli import CLI
from mininet.log import setLogLevel

def main(**kwargs):
    tmp1:exp1Topo = exp1Topo()
    setLogLevel("info")
    net = Mininet(topo=tmp1, switch=OVSKernelSwitch, controller=DefaultController, autoSetMacs=True)
    # net = Mininet(topo=tmp1)
    net.start()
    
    # net["r1"].cmd("ip addr add 10.0.0.3/24 dev r1-eth0")
    # net["r1"].cmd("ip addr add 10.0.3.4/24 dev r1-eth1")
    # net["r1"].cmd("ip addr add 10.0.1.1/24 dev r1-eth2")
    
    # net["r2"].cmd("ip addr add 10.0.1.2/24 dev r2-eth0")
    # net["r2"].cmd("ip addr add 10.0.2.1/24 dev r2-eth1")

    net["h1"].cmd("ip route add default via 10.0.0.3")
    net["h2"].cmd("ip route add default via 10.0.3.4")
    net["h3"].cmd("ip route add default via 10.0.2.1")

    net["r1"].cmd("ip route add to 10.0.2.0/24 via 10.0.1.2 dev r1-eth2")
    net["r2"].cmd("ip route add to 10.0.0.0/24 via 10.0.1.1 dev r2-eth0")
    net["r2"].cmd("ip route add to 10.0.3.0/24 via 10.0.1.1 dev r2-eth0")

    CLI(net)
    input("Network running. Press Enter to stop...")
    net.stop()

if __name__ == "__main__":
    main()