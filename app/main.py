##  Begin Standard Imports
import sys
from pathlib import Path

##  Begin Local Imports
import model.resource as resources
from model.exp1 import exp1Topo
from model.exp2 import exp2Topo

##  Begin `mininet` Imports
from mininet.net import Mininet
from mininet.node import Node, OVSKernelSwitch, Controller, RemoteController, DefaultController
from mininet.cli import CLI
from mininet.log import setLogLevel

def main(**kwargs):
    expNum:int = 0
    try:
        expNum = int(sys.argv[1])
    except Exception as e:
        raise(e)
    
    if expNum == 1:
        exp1Run(kwargs=kwargs)
    elif expNum == 2:
        exp2Run(kwargs=kwargs)

def exp1Run(**kwargs) -> Path:
    tmp1:exp1Topo = exp1Topo()
    setLogLevel("info")
    net = Mininet(topo=tmp1, controller=DefaultController, autoSetMacs=True)
    # net = Mininet(topo=tmp1)
    net.start()

    net["h1"].cmd("ip route add default via 10.0.0.3")
    net["h2"].cmd("ip route add default via 10.0.3.4")
    net["h3"].cmd("ip route add default via 10.0.2.1")

    net["r1"].cmd("ip route add to 10.0.2.0/24 via 10.0.1.2 dev r1-eth2")
    net["r2"].cmd("ip route add to 10.0.0.0/24 via 10.0.1.1 dev r2-eth0")
    net["r2"].cmd("ip route add to 10.0.3.0/24 via 10.0.1.1 dev r2-eth0")

    ##  Begin `exp1` Logging
    outputPath:Path = Path.joinpath(resources.CONST_OUTPUT_DIR, "result1.txt")
    output:str = ""
    output += f"--[[H1 -> H3]]--\n{net['h1'].cmd('ping -c 1 10.0.2.2')}\n"
    output += f"--[[H1 -> H3]]--\n{net['h2'].cmd('ping -c 1 10.0.2.2')}\n"
    output += f"--[[H1 -> H3]]--\n{net['h3'].cmd('ping -c 1 10.0.0.1')}\n"
    output += f"--[[H1 -> H3]]--\n{net['h3'].cmd('ping -c 1 10.0.3.2')}\n"
    output += f"--[[PINGALL]]--\nPacket Loss: {net.pingAll()}%\n"
    with open(outputPath, "w") as f:
        f.write(output)

    CLI(net)
    input("Network running. Press Enter to stop...")
    net.stop()

    return outputPath

def exp2Run(**kwargs) -> None:
    tmp2:exp2Topo = exp2Topo()
    setLogLevel("info")
    net = Mininet(topo=tmp2, switch=OVSKernelSwitch, controller=DefaultController, autoSetMacs=True)
    net.start()

    CLI(net)
    input("Network running. Press Enter to stop...")
    net.stop()

if __name__ == "__main__":
    main()