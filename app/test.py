from mininet.net import Mininet
from mininet.topo import SingleSwitchTopo
from mininet.cli import CLI
from mininet.log import setLogLevel

def runNetwork():
    topo = SingleSwitchTopo(k=2)
    net = Mininet(topo=topo)
    net.start()
    print("Hosts in network:", topo.hosts())
    net.pingAll()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    runNetwork()
