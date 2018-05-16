#!/usr/bin/env python
#encoding:utf-8
#20170718

import argparse
import commands
import ConfigParser
import os
import re
import sys

parser = argparse.ArgumentParser(description="get kegg annotation locals")
parser.add_argument("-reflesh", dest="reflesh", type=str, help="confirm download KEGG annotation datadases or not :T/F")
parser.add_argument("-matrix", dest="matrix", type=str, help="exp.txt or exp.list")
parser.add_argument("-org", dest="org", type=str, help="org of species:plant/animals/bacteria")
parser.add_argument("-matrix_config", dest="m_config", type=str, help="if exp.txt:m_config is needed")
parser.add_argument("-FC", dest="fc", type=str, help="if exp.txt:Fold change")
args = parser.parse_args()
