##  Begin Standard Imports

##  Begin Local Imports

##  Begin `mininet` Imports
from mininet.node import Node
from mininet.topo import Topo
from mininet.log import info

class exp2Topo(Topo):
    def __init__(self, **kwargs) -> None:
        super(exp2Topo, self).__init__(**kwargs)

        h1 = self.addHost(
            "h1", 
        )
        h2 = self.addHost(
            "h2", 
        )
        h3 = self.addHost(
            "h3", 
        )

        s1 = self.addSwitch(
            "s1"
        )

        s2 = self.addSwitch(
            "s2"
        )

        self.addLink(
            h1, s1,
            intfName1="h1-eth0",
            intfName2="s1-eth1"
        )
        self.addLink(
            h2, s1,
            intfName1="h2-eth0",
            intfName2="s1-eth2"
        )
        self.addLink(
            s1, s2,
            intfName1="s1-eth3",
            intfName2="s2-eth1"
        )
        self.addLink(
            s2, h3,
            intfName1="s2-eth2",
            intfName2="h3-eth0"
        )