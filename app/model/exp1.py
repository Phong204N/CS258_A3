##  Begin Standard Imports

##  Begin Local Imports

##  Begin `mininet` Imports
from mininet.node import Node
from mininet.topo import Topo
from mininet.log import info

class exp1Topo(Topo):
    def __init__(self, **kwargs) -> None:
        super(exp1Topo, self).__init__(**kwargs)
        # for key in kwargs:
        #     if key == "N": N=kwargs[key]

        h1_ports:list[str, int] = ["h1-eth", 0]
        h2_ports:list[str, int] = ["h2-eth", 0]
        h3_ports:list[str, int] = ["h3-eth", 0]
        r1_ports:list[str, int] = ["r1-eth", 0]
        r2_ports:list[str, int] = ["r2-eth", 0]

        # h1 = self.addHost("h1", ip="10.0.0.1/24")
        # h2 = self.addHost("h2", ip="10.0.3.2/24")
        # h3 = self.addHost("h3", ip="10.0.2.2/24")
        
        h1 = self.addHost("h1")
        h2 = self.addHost("h2")
        h3 = self.addHost("h3")

        r1 = self.addHost("r1", cls=LinuxRouter)
        r2 = self.addHost("r2", cls=LinuxRouter)

        # r1.setIP("10.0.0.3/24", intf=f"{r1_ports[0]}0")
        # r1.setIP("10.0.3.4/24", intf=f"{r1_ports[0]}1")
        # r1.setIP("10.0.0.3/24", intf=f"{r1_ports[0]}2")
        # r2.setIP("10.0.1.2/24", intf=f"{r2_ports[0]}0")
        # r2.setIP("10.0.2.1/24", intf=f"{r2_ports[0]}1")

        self.addLink(h1, r1, intfName1=exp1Topo.addNewInterfaceName(h1_ports), intfName2=exp1Topo.addNewInterfaceName(r1_ports),
                     params1={"ip":"10.0.0.1/24"},
                     params2={"ip":"10.0.0.3/24"}
                     )
        self.addLink(h2, r1, intfName1=exp1Topo.addNewInterfaceName(h2_ports), intfName2=exp1Topo.addNewInterfaceName(r1_ports),
                     params1={"ip":"10.0.3.2/24"},
                     params2={"ip":"10.0.3.4/24"}
                     )
        self.addLink(r1, r2, intfName1=exp1Topo.addNewInterfaceName(r1_ports), intfName2=exp1Topo.addNewInterfaceName(r2_ports),
                     params1={"ip":"10.0.1.1/24"},
                     params2={"ip":"10.0.1.2/24"}
                     )
        self.addLink(r2, h3, intfName1=exp1Topo.addNewInterfaceName(r2_ports), intfName2=exp1Topo.addNewInterfaceName(h3_ports),
                     params1={"ip":"10.0.2.1/24"},
                     params2={"ip":"10.0.2.2/24"}
                     ) 

    def addNewInterfaceName(intfValues:list[str, int]) -> str:
        intfValues[1] += 1
        result:str = f"{intfValues[0]}{intfValues[1]}"

class LinuxRouter(Node):
    def config(self, **params):
        super(LinuxRouter, self).config(**params)
        info("enabling forwarding on ", self)
        self.cmd("sysctl net.ipv4.ip_forward=1")

    def terminate(self):
        self.cmd("sysctl net.ipv4.ip_forward=0")
        super(LinuxRouter, self).terminate()