import os,sys

cast = input("City to find Weather Forecast: ")
os.system("curl wttr.in/{0}".format(cast))
