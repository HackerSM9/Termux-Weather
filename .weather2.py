import os,sys

cast = input("\nCity to find Weather Forecast: ")
os.system("curl v2.wttr.in/{0}".format(cast))
