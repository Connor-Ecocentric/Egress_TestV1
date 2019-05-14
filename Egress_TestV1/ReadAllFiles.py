# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:43:23 2019

@author: conno
"""

import pandas as pd
import os
# The Read files class is now obselete.
# The class has the ability to read all files in x folder and build a DataFrame where each file is written into a new column.
# The DF is then output into a .csv file for further proccessing in excel. It was realised that processing in excel will be quite a manual proccess
# Because of the manual requirements a new class 'EgressTesting' has been created to automate the testing.
class ReadFiles():
    def __init__(self):
        self.path = ('C:\\Users\\conno\\Source\\Repos\\Connor-Ecocentric\\Egress_TestV1\\Egress_TestV1\\TestOutput\\')
    def Read(self):
        global EgressResults
        for file in os.listdir(self.path):
            filename = os.path.join(self.path, file)
            with open(filename, 'r') as file:
                 data = pd.read_csv(file, delimiter = "\n", header = None)
                 EgressResults = pd.concat([EgressResults, data], axis = 1, sort= False)
                
#ReadFiles().Read()

        return;
# The EgressTesting class is designed to read and proccess the .txt files generated from the Egress_TestV1.py script
# A unittest structure has been followed where all tests are seperated into seperate catagories (functions in the class) and a test runner can choose to activate / disable certain tests.
# If in the case a new test where to be added, a new function within the EgressTesting class would be created and the function will be called within the main loop
class EgressTesting():
    def __init__(self):
        self.path = ('C:\\Users\\conno\\Source\\Repos\\Connor-Ecocentric\\Egress_TestV1\\Egress_TestV1\\TestOutputV2\\')
        self.df = df
        self.Header = self.df.iat[0,0]
    def testSerial(self):
        # Testing df index 0:3 to ensure all serial number values match
        Serial_1 = self.df.iat[0,0]
        Serial_2 = self.df.iat[1,0] 
        Serial_3 = self.df.iat[2,0]
        Serial_4 = self.df.iat[3,0]
        #Test case 1
        if Serial_2 == Serial_1:
            Results.at[0, self.Header]=True
        else:
           Results.at[0, self.Header]=False
        #Test case 2
        if Serial_3 == Serial_1:
            Results.at[1, self.Header]=True
        else:
            Results.at[1, self.Header]=False
        #Test case 3
        if Serial_4 == Serial_1:
            Results.at[2, self.Header]=True
        else:
           Results.at[2, self.Header]=False       
    def testPartitions(self):
        EEMC = self.df.iat[4,0]
        SDCard = self.df.iat[5,0]
        #Test case 4
        if "311" in EEMC:
            Results.at[3, self.Header]=True
        else:
            Results.at[3, self.Header]=False
        #Test case 5
        if "302" in SDCard:
            Results.at[4, self.Header]=True
        else:
           Results.at[4, self.Header]=False 
    def testEcoVersion(self):
        PartA = self.df.iat[6,0]
        PartB = self.df.iat[7,0]
        #Test case 6
        if PartA == PartB:
            Results.at[5, self.Header]=True
        else:
            Results.at[5, self.Header]=False           
    def testSDType(self):
        # raw input for this varible should look like 'ext4 12.2G 1%' the below seperates into testble chunks
        Type = self.df.iat[8,0].split()[0]
        PartSize = self.df.iat[8,0].split()[1]
        FreeSpace = self.df.iat[8,0].split()[2].replace('%', '')
        #test case 7
        if "ext4" in Type:
            Results.at[6, self.Header]=True
        else:
            Results.at[6, self.Header]=False
        #Test case 8
        if "12.2" in PartSize:
            Results.at[7, self.Header]=True
        else:
           Results.at[7, self.Header]=False
        #Test case 9
        if int(FreeSpace) < 30:
            Results.at[8, self.Header]=True
        else:
           Results.at[8, self.Header]=False          
    def testVoltageCal(self):
        print('not sure what to do here just yet')
        #Test case 10
        Results.at[9, self.Header]='NaN'       
    def testRWSpeed(self):
        SDSpeed = self.df.iat[10,0]
        EEMCSpeed = self.df.iat[11,0]
        #Test case 11
        if float(SDSpeed) > 16:
            Results.at[10, self.Header]=True
        else:
            Results.at[10, self.Header]=False
        #Test case 12

        if float(EEMCSpeed) > 62:
            Results.at[11, self.Header]=True
        else:
           Results.at[11, self.Header]=False          
    def testTemp(self):
        Temp = self.df.iat[14,0]
        #Test case 14
        if int(Temp) < 65000:
            Results.at[13, self.Header]=True
        else:
            Results.at[13, self.Header]=False          
    def testWifi(self):
        Quality =  self.df.iat[15,0]
        Level =  self.df.iat[16,0].replace('level=', '')
        #Test case 14
        if float(Level) > -70:
            Results.at[14, self.Header]=True
        else:
            Results.at[14, self.Header]=False
    def testSDHealth(self):
        AveCycle = self.df.iat[30,0]
        MaxCycle = self.df.iat[31,0]
        #Test case 15
        if int(AveCycle) < 3500:
            Results.at[15, self.Header]=True
        else:
            Results.at[15, self.Header]=False
        #Test case 16
        if int(MaxCycle) < 3500:
            Results.at[16, self.Header]=True
        else:
            Results.at[16, self.Header]=False 
    def testMem(self):
        FailedResults = self.df.iat[33,0]
        #Test case 17
        if int(FailedResults) < 1:
            Results.at[17, self.Header]=True
        else:
            Results.at[17, self.Header]=False

           
#!!!!!!!!!!!!!!  ***Main()***  !!!!!!!!!!!!!!
EgressResults = pd.DataFrame()    
RawInput = pd.DataFrame()  
path = ('C:\\Users\\conno\\Source\\Repos\\Connor-Ecocentric\\Egress_TestV1\\Egress_TestV1\\TestOutputV2\\')          
for file in os.listdir(path):
    filename = os.path.join(path, file)
    with open(filename, 'r') as file:
            df = pd.read_csv(file, delimiter = "\n", header = None)
            Results = pd.DataFrame()
            #EgressTesting.df.variable = df
            EgressTesting().df = df
            EgressTesting().testSerial()
            EgressTesting().testPartitions()
            EgressTesting().testEcoVersion()
            EgressTesting().testSDType()
#           EgressTesting().testVoltageCal()
            EgressTesting().testRWSpeed()
            EgressTesting().testTemp()
            EgressTesting().testWifi()
            EgressTesting().testSDHealth()
            EgressTesting().testMem()
    RawInput = pd.concat([RawInput, df], axis = 1, sort = False)
    EgressResults = pd.concat([EgressResults, Results], axis = 1, sort= False)
    with pd.ExcelWriter('C:\\Users\\conno\\Desktop\\Output.xlsx', engine='xlsxwriter') as writer:
        EgressResults.to_excel(writer, sheet_name= 'Results', header = True)
        RawInput.to_excel(writer, sheet_name= 'Inputs', header = True)
    print(EgressResults)


