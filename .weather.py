import os,sys

cast = input("\n\033[0;34mCity to find Weather Forecast: ")
os.system("curl wttr.in/{0}".format(cast))
