#!/usr/bin/env python

import sys
import os

def cetak(objek, variabel=False):
  if variabel:
    dir(objek)
  else:
    print(objek)

arg = sys.argv
arg_jlh = len(arg)

if arg_jlh < 2:
  cetak('Tentukan direktori tujuan !!!')
  exit
else:
  dir_tujuan = os.path.realpath(arg[1])
  dir_sekarang = os.path.realpath('./')
  cetak('sekarang di => ' + dir_sekarang)
  cetak('bandingkan dengan => ' +  dir_tujuan)

  
