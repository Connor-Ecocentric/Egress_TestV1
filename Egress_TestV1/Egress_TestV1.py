import SSH_Comms
import os
import time
cwd = dir_path = os.path.dirname(os.path.realpath(__file__))

class Collector():
    def __init__(self):
        #self.CollectorIp = ('215.16.144.49')
        self.CollectorIp = ('10.0.0.96')
        self.LocalPath = ("%s%s") % (cwd, '\\TestOutput\\')
        self.LocalFile = ("%s%s") % (cwd,'\\egress_testing.sh')
        self.RemotePath = '/home/root'
        self.RemoteFile = '/home/root/egress.txt'
    def SendFile(self): 
        SSH_Comms.SSH().Connect(self.CollectorIp)
        SSH_Comms.SSH().SendCommand("rm egress*")
        SSH_Comms.SSH().sendSCP(self.LocalFile, self.RemotePath)
        SSH_Comms.SSH().SendCommand("tr -d '\r' <egress_testing.sh >egress_testing.sh.new && mv egress_testing.sh.new egress_testing.sh")
        SSH_Comms.SSH().SendCommand('chmod 755 egress_testing.sh')
        SSH_Comms.ssh.close()
        return;
    def GetData(self):
        SSH_Comms.SSH().Connect(self.CollectorIp)
        SSH_Comms.SSH().getSCP(self.LocalPath, self.RemoteFile)


print("Do you wish to send or recieve? (1/0)")        
TransferType = int(input())    
if TransferType == 1:
    print("Sending Files to Collector Now......")
    Collector().SendFile()
elif TransferType == 0:
    print("Recieving Files from Collector Now.....")
    Collector().GetData()

