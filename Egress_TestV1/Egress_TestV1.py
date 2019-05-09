import SSH_Comms
import os
import time
cwd = dir_path = os.path.dirname(os.path.realpath(__file__))


class Collector():
    def __init__(self):
        self.CollectorIp = Host #('215.16.144.81')
        #self.CollectorIp = ('10.0.0.96')
        self.LocalPath = ("%s%s") % (cwd, '\\TestOutput\\')
        self.LocalFile = ("%s%s") % (cwd,'\\egress_testing.sh')
        self.RemotePath = '/home/root'
        self.RemoteFile = '/home/root/N9C350B021801*'
    def SendFile(self): 
        SSH_Comms.SSH().Connect(self.CollectorIp)
        SSH_Comms.SSH().sendSCP(self.LocalFile, self.RemotePath)
        SSH_Comms.SSH().SendCommand("tr -d '\r' <egress_testing.sh >egress_testing.sh.new && mv egress_testing.sh.new egress_testing.sh")
        SSH_Comms.SSH().SendCommand('chmod 755 egress_testing.sh')
        SSH_Comms.ssh.close()
        return;
    def GetData(self):
        SSH_Comms.SSH().Connect(self.CollectorIp)
        SSH_Comms.SSH().getSCP(self.LocalPath, self.RemoteFile)
        SSH_Comms.SSH().SendCommand("rm egress*")
        SSH_Comms.SSH().SendCommand("rm N9C350B0218*")
    def ShutDown(self):
        SSH_Comms.SSH().Connect(self.CollectorIp)
        SSH_Comms.SSH().SendCommand("./mcu-disable-always-on.sh")
        SSH_Comms.SSH().SendCommand("sync; shutdown -P -t now")




HostNames = [
        '215.16.144.68',
        '215.16.144.90',
        '215.16.144.112',
        '215.16.144.70',
        '215.16.144.77',
        '215.16.144.97',
        '215.16.144.116',
        '215.16.144.78',
        '215.16.144.94',
        '215.16.144.127',
        '215.16.144.133',
        '215.16.144.141',
        '215.16.144.144',
        '215.16.144.140',
        '215.16.144.132'
]

# Main loop, Depending on user input the scrip will either send or recieve a egress testing file. 
print("Do you wish to send or recieve? (1/0) And press 3 if you want to shutdown all collectors")        
TransferType = int(input())    
if TransferType == 1:
    print("Sending Files to Collector Now......")
    for Host in HostNames:
        Collector().SendFile()
elif TransferType == 0:
    for Host in HostNames:
        print("Recieving Files from Collector Now.....")
        Collector().GetData()
elif TransferType == 3:
    for Host in HostNames:
        print("Bye Bye")
        Collector().ShutDown()
        