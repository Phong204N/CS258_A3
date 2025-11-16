##  Begin Standard Imports

##  Begin Local Imports

##  Begin `mininet` Imports
from mininet.topo import Topo

class exp2Topo(Topo):
    def __init__(self, **kwargs) -> None:
        super(exp2Topo, self).__init__(**kwargs)

        ##  Add the hosts themselves with the preset IP.  
        h1 = self.addHost(
            "h1", 
        )
        h2 = self.addHost(
            "h2", 
        )
        h3 = self.addHost(
            "h3", 
        )

        ##  Add the switches themselves.  
        s1 = self.addSwitch(
            "s1"
        )

        s2 = self.addSwitch(
            "s2"
        )

        ##  Add each link between devices.  Specify the interface name. 
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