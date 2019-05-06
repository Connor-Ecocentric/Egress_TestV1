import SSH_Comms
import os

cwd = dir_path = os.path.dirname(os.path.realpath(__file__))

class Collector():
    def __init__(self):
        self.CollectorIp = ('215.16.144.49')
        self.Filename = ("%s%s") % (cwd,'\\egress_testing.sh')
        print(self.Filename)
    def GetData(self): 
        SSH_Comms.SSH().Connect(self.CollectorIp)
        SSH_Comms.SSH().sendSCP(self.Filename)
        Runscript = SSH_Comms.SSH().SendCommand("./egress_testing.sh")
        return Runscript;

x = Collector().GetData()

