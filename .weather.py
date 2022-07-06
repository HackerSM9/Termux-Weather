import os,sys

cast = input("\n\033[1;34mCity to find Weather Forecast: ")
os.system("curl wttr.in/{0}".format(cast))
