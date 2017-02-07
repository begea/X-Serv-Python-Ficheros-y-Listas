#!/usr/bin/python3

fd = open("/etc/passwd", "r")

lineas = fd.readlines()
fd.close()

for linea in lineas:
  posicion1 = linea.find(":")
  posicion2 = linea.rfind(":")
  print(linea[: posicion1] + " " + linea[posicion2+1 :-1]);
