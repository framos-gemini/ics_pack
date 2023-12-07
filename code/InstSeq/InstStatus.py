# -*- coding: utf-8 -*-
"""
Created on Feb 15, 2023

Modified on Nov 9, 2023

@author: hilee
"""

import os, sys
import threading

import time as ti
import datetime
from distutils.util import strtobool


sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from InstSeq_def import *

import svc_process
from add_wcs_header import update_header2

import astropy.io.fits as pyfits
import numpy as np

import Libs.SetConfig as sc
from Libs.MsgMiddleware import *
from Libs.logger import *

import FITSHD_v3 as LFHD

import cppyy, time
giapi_root=os.environ.get("GIAPI_ROOT")
#giapi_root="/home/ics/giapi-glue-cc"
cppyy.add_include_path(f"{giapi_root}/install/include")
cppyy.add_library_path(f"{giapi_root}/install/lib")
cppyy.include("giapi/EpicsStatusHandler.h")
cppyy.include("giapi/GeminiUtil.h")
cppyy.include("giapi/GiapiUtil.h")
cppyy.include("giapi/EpicsStatusHandler.h")
cppyy.include("giapi/GiapiUtil.h")
cppyy.load_library("libgiapi-glue-cc")
cppyy.add_include_path(f"{giapi_root}/src/examples/InstrumentDummyPython")
#cppyy.include("InstCmdHandler.h")
cppyy.include("InstStatusHandler.h")

from cppyy.gbl import giapi
from cppyy.gbl import instDummy

def callbackStatus(t, statusItem):
    print (f'Recieved the message type is: {t}')
    if  giapi.type.BOOLEAN == t:
        print (f'{statusItem.getDataAsInt(0)}')
    elif giapi.type.INT == t:
        print (f'{statusItem.getDataAsInt(0)}')
    elif giapi.type.DOUBLE == t:
        print (f'{statusItem.getDataAsDouble(0)}')
    elif giapi.type.STRING == t:
        print (f'{statusItem.getDataAsString(0)}')
    elif giapi.type.BYTE == t:
        print (f'{statusItem.getDataAsByte(0)}')
    else:
            print (f'Not defined, it is an error')


handler = instDummy.InstStatusHandler.create(callbackStatus)
giapi.GeminiUtil.subscribeEpicsStatus("tc1:sad:instrPA", handler)


while True:
    #print(f'Father sleeping')
    pStatus =  giapi.GeminiUtil.getChannel("tc1:sad:parAngle", 5);
    print (f'The parAngle is: {pStatus.getDataAsDouble(0)}')
    time.sleep(5)
