#!/usr/bin/python
# -*- coding: utf-8 -*-

from sylabledivider import SyllableDivider
import sys


if len(sys.argv) != 2:
   print('need filename to read')
   sys.exit()

#path = sys.argv[1]
#input_text = open(path).read().replace('\n', '').lower()
zmienna = "Ala ma kota a kot ma ale"
zmienna = zmienna.lower()


print(SyllableDivider(zmienna).divide())

