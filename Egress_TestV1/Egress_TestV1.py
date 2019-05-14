import SSH_Comms
import os
import time
cwd = dir_path = os.path.dirname(os.path.realpath(__file__))


class Collector():
    def __init__(self):
        self.CollectorIp = Host #('215.16.144.81')
        #self.CollectorIp = ('10.0.0.96')
        self.LocalPath = ("%s%s") % (cwd, '\\TestOutputV2\\')
        self.LocalFile1 = ("%s%s") % (cwd,'\\egress_testing.sh')
        self.LocalFile2 = ("%s%s") % (cwd,'\\SMART_Tool_Sample_armabihf')
        self.LocalFile3 = ("%s%s") % (cwd,'\\eco-feature-extract')
        self.RemotePath = '/home/root'
        self.RemotePath2 = '/home/root/bin'
        self.RemoteFile = '/home/root/N9C350B021801*'
    def SendFile(self): 
        SSH_Comms.SSH().Connect(self.CollectorIp)
        SSH_Comms.SSH().sendSCP(self.LocalFile1, self.RemotePath)
        SSH_Comms.SSH().sendSCP(self.LocalFile2, self.RemotePath)
        SSH_Comms.SSH().SendCommand("tr -d '\r' <egress_testing.sh >egress_testing.sh.new && mv egress_testing.sh.new egress_testing.sh")
        SSH_Comms.SSH().SendCommand('chmod 755 egress_testing.sh')
        SSH_Comms.SSH().SendCommand('chmod 777 SMART_Tool_Sample_armabihf')
        
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
    def SerialFix(self):
        SSH_Comms.SSH().Connect(self.CollectorIp)
        SSH_Comms.SSH().sendSCP(self.LocalFile3, self.RemotePath2)
        SSH_Comms.SSH().SendCommand("eco-feature-extract -s $HOSTNAME")



#HostNames = ['10.0.0.96']
HostNames = [
    '215.16.144.45',
    '215.16.144.54',
    '215.16.144.66',
    '215.16.144.72',
    '215.16.144.73',
    '215.16.144.79',
    '215.16.144.86',
    '215.16.144.89',
    '215.16.144.93',
    '215.16.144.102',
    '215.16.144.104',
    '215.16.144.107',
    '215.16.144.108',
    '215.16.144.117',
    '215.16.144.120',
    '215.16.144.97',
    '215.16.144.100',
    '215.16.144.101',
    '215.16.144.103',
    '215.16.144.106',
    '215.16.144.109',
    '215.16.144.110',
    '215.16.144.112',
    '215.16.144.115',
    '215.16.144.116',
    '215.16.144.118',
    '215.16.144.119',
    '215.16.144.121',
    '215.16.144.124',
    '215.16.144.133'
]

HostNamess = [
        '215.16.144.97',
        '215.16.144.100',
        '215.16.144.101',
        '215.16.144.103',
        '215.16.144.106',
        '215.16.144.109',
        '215.16.144.110',
        '215.16.144.112',
        '215.16.144.115',
        '215.16.144.116',
        '215.16.144.118',
        '215.16.144.119',
        '215.16.144.121',
        '215.16.144.124',
        '215.16.144.133'
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
elif TransferType == 4:
    for Host in HostNames:
        Collector().SerialFix()
