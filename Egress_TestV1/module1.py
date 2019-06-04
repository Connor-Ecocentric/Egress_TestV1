# coding: utf-8
import unittest
import logging
import sys
import os
import subprocess
from logging.handlers import TimedRotatingFileHandler
FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
LOG_FILE = "CollectorEgressTest.log"

def Sendcmd(cmd):
    result = subprocess.check_output(cmd, shell=True)
    return result;

def get_console_handler():
   console_handler = logging.StreamHandler(sys.stdout)
   console_handler.setFormatter(FORMATTER)
   return console_handler
def get_file_handler():
   file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
   file_handler.setFormatter(FORMATTER)
   return file_handler
def get_logger(logger_name):
   logger = logging.getLogger(logger_name)
   logger.setLevel(logging.DEBUG) # better to have too much log than not enough
   logger.addHandler(get_console_handler())
   logger.addHandler(get_file_handler())
   # with this pattern, it's rarely necessary to propagate the error up to parent
   logger.propagate = False
   return logger

class SerialNumTest(unittest.TestCase):
    Host  = Sendcmd('printf $HOSTNAME')
    def testConfigini(self):
        self.assertEqual(Sendcmd("more /media/sdcard/config.ini | grep client_id | awk '{printf $3}'"),self.Host)
    def testConfigbak(self):
        self.assertEqual(Sendcmd("more /home/root/config.bak | grep client_id | awk '{printf $3}'"),self.Host)
    def testEprom(self):
        self.assertEqual(Sendcmd("eco-feature-extract -e | grep Serial | awk '{printf $4}'"),self.Host)
class EEMCTest(unittest.TestCase):
    def testPartition(self):
        self.assertIn('b311h',Sendcmd("stat / | grep Device | awk '{printf $2}'"))
    def testRWSpeed(self):
        self.assertGreater(float(Sendcmd("hdparm -t /dev/mmcblk0 | awk '{printf $11}'")),16)
class Sha1sumTest(unittest.TestCase):
    def testEcoversion(self):
        self.assertEqual(Sendcmd("sha1sum /eco-overlay.tar.gz | awk '{print $1}'"),Sendcmd("sha1sum /run/media/mmcblk1p2/eco-overlay.tar.gz | awk '{print$1}'"))
class SDCardTest(unittest.TestCase):
    SDdetail = Sendcmd("df -Th | grep mmcblk0 | grep /dev/mmcblk0p2 | awk '{print $2,$3,$6}'")
    def testType(self):
        self.assertEqual(self.SDdetail.split()[0],'ext4')
    def testSize(self):
        self.assertIn('12.2',self.SDdetail.split()[1])
    def testUsedSpace(self):
        self.assertLess(int(self.SDdetail.split()[2].replace('%', '')),30)
    def testRWspeed(self):
        self.assertGreaterEqual(float(Sendcmd("hdparm -t /dev/mmcblk1 | awk '{printf $11}'")),68)
    def testSDPart(self):
        self.assertIn('b302h',Sendcmd("stat /media/sdcard | grep Device | awk '{printf $2}'"))
    
class VoltageCalTest(unittest.TestCase):
    x = 1+1
    #tail -30 /media/sdcard/eco-feature-extract.log | grep RMS | awk '{print $39,$41,$43}'
class TempTest(unittest.TestCase):
    def testTemperature(self):
        self.assertLess(int(Sendcmd("cat /sys/class/thermal/thermal_zone0/temp")),65000
class WifiTest(unittest.TestCase):
    x = 1+1
class MemTest(unittest.TestCase):
    x = 1+1



log = get_logger("EgressLog")
log.debug("this is a test")
log.info(" another test")
if __name__ == '__main__':

    unittest.main()  