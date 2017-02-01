#!/usr/bin/python
# -*- coding: utf-8 -*-

fd = open("/etc/passwd", "r")

lineas = fd.readlines()
fd.close()

for linea in lineas:
	trozos = linea.split(':')
	usuario = trozos[0]
	shell = trozos[-1]
	print 'usuario:'+ usuario, 'shell:'+ shell,

print '\nnumero de usuarios:', len(lineas)
