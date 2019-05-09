import pandas as pd
import numpy
import os
EgressResults = pd.DataFrame()
data = []
class ReadFiles():
    def __init__(self):
        self.path = ('C:\\Users\\conno\\Source\\Repos\\Connor-Ecocentric\\Egress_TestV1\\Egress_TestV1\\TestOutput\\')
    def Read(self):
        for file in os.path.listdir(self.path):
            filename = os.path.join(path, file)
            with open(filename, 'r') as file:
                print(file)
                data.append(file)
ReadFiles().Read()





#    testdf = pd.DataFrame(columns = ['command', 'output'])
#    df = []
#    connect()
    #outputs = ["sha1sum /usr/bin/ct-toggler","sha1sum /usr/bin/eco-feature-extract"]
#    for output in outputs:
#        out = sendcommand(output)
#        df.append({'command':output, 'output':out})
#        df1 = testdf.append(df)
    #output = sendcommand("sha1sum /usr/bin/ct-toggler")   
    #output = sendcommand("sha1sum /usr/bin/eco-feature-extract") 
#    print ("Command done, closing SSH connection")
#    ssh.close()
#%%
#    dfx = pd.DataFrame()
#    path = ('C:/Users/conno/Desktop/Ecocentric_Files/Numen9/Numen Release/v3.50.04.02/signatures/')
#    print (str(len(os.listdir(path))) + ' Files found in Path')
#    for filedir in os.listdir(path):
#        filename = os.path.join(path, filedir)
#        with open(filename, 'r') as file:
#               data = pd.read_csv(file, header = None)
#                dfx = dfx.append(data, ignore_index = True) 
#    df2 = df1.join(dfx)
    
