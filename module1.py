# coding: utf-8
import unittest
import logging
import sys
import os
from logging.handlers import TimedRotatingFileHandler
FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
LOG_FILE = "CollectorEgressTest.log"

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
    Host  = os.system('more /etc/hostname')
    def testConfigini(self):
        self.assertEqual(os.system("more /media/sdcard/config.ini | grep client_id | awk '{print $3}'"),self.Host)
    def testConfigbak(self):
        self.assertEqual(os.system("more /home/root/config.bak | grep client_id | awk '{print $3}'"),self.Host)
    def testEprom(self):
        self.assertEqual(os.system("eco-feature-extract -e | grep Serial | awk '{print $4}'"),self.Host)

    #def testConfigbak(self):

    #def testEprom(self):


class PartitionTest(unittest.TestCase):
    x = 1+1
class Sha1sumTest(unittest.TestCase):
    x = 1+1
class SDCardTest(unittest.TestCase):
    x = 1+1
class VoltageCalTest(unittest.TestCase):
    x = 1+1
class TempTest(unittest.TestCase):
    x = 1+1
class WifiTest(unittest.TestCase):
    x = 1+1
class MemTest(unittest.TestCase):
    x = 1+1



log = get_logger("EgressLog")
log.debug("this is a test")
log.info(" another test")
if __name__ == '__main__':

    unittest.main()  