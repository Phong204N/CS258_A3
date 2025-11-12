##  Begin Standard Imports

##  Begin Local Imports
import model.resource
from app.model.exp1 import exp1Topo

##  Begin `mininet` Imports
from mininet.mininet.net import Mininet
from mininet.mininet.node import Node, OVSKernelSwitch, Controller, RemoteController, DefaultController
from mininet.mininet.cli import CLI
from mininet.mininet.topo import Topo
from mininet.mininet.log import setLogLevel, info

def main():
    tmp1:exp1Topo = exp1Topo()
    setLogLevel("info")
    net = Mininet(topo=exp1Topo, switch=OVSKernelSwitch, controller=DefaultController, autoSetMacs=True)
    net.start()

    

if __name__ == "__main__":
    main()