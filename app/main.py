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
    setLogLevel("debug")
    net = Mininet(topo=tmp1, switch=OVSKernelSwitch, controller=DefaultController, autoSetMacs=True)
    # net = Mininet(topo=tmp1)
    net.start()

    print("r1 ifindex list:", net['r1'].cmd('ip -o link show'))
    print("r2 ifindex list:", net['r2'].cmd('ip -o link show'))
    print("r1 ip addr before:", net['r1'].cmd('ip -4 addr show'))
    print("r2 ip addr before:", net['r2'].cmd('ip -4 addr show'))

    print("r1 add0:", net['r1'].cmd('ip addr add 10.0.0.3/24 dev r1-eth0 2>&1; echo EXIT:$?'))
    print("r1 add1:", net['r1'].cmd('ip addr add 10.0.3.4/24 dev r1-eth1 2>&1; echo EXIT:$?'))
    print("r1 add2:", net['r1'].cmd('ip addr add 10.0.1.1/24 dev r1-eth2 2>&1; echo EXIT:$?'))

    print("r2 add0:", net['r2'].cmd('ip addr add 10.0.1.2/24 dev r2-eth0 2>&1; echo EXIT:$?'))
    print("r2 add1:", net['r2'].cmd('ip addr add 10.0.2.1/24 dev r2-eth1 2>&1; echo EXIT:$?'))

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