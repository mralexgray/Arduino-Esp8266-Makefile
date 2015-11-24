#!/usr/bin/env python

import json, sys, urllib, zipfile, tarfile, os, time

arduino_esp8266_manager_link = "http://arduino.esp8266.com/staging/package_esp8266com_index.json"

if not os.path.exists("downloads"):
  os.mkdir("downloads")

if not os.path.exists("tools"):
  os.mkdir("tools")


def defineHost():
  sys_platform = sys.platform
  sys_arch = 64 if sys.maxsize > 2**32 else 32

  if "linux" in sys_platform:
    if sys_arch > 32:
      host = "x86_64-pc-linux-gnu"
    else:
      host = "i686-pc-linux-gnu"
  elif "darwin" in sys_platform:
    if sys_arch > 32:
      host = "x86_64-apple-darwin"
    else:
      host = "i386-apple-darwin"
  else:
    host = None
  return host

def downloadTools(host):
  arduino_esp8266_json = json.loads(urllib.urlopen(arduino_esp8266_manager_link).read())
  download_path = "downloads/"
  tools_path = "tools/"

  platform = arduino_esp8266_json['packages'][0]['platforms'][0]
  xtensa = arduino_esp8266_json['packages'][0]['tools'][0]
  esptool = arduino_esp8266_json['packages'][0]['tools'][1]
  mkspiffs = arduino_esp8266_json['packages'][0]['tools'][3]

  urllib.urlretrieve(platform['url'], download_path + platform['archiveFileName'])
  with zipfile.ZipFile(download_path + platform['archiveFileName'], "r") as z:
      z.extractall(tools_path)
  os.rename(tools_path + platform['archiveFileName'][:-4], tools_path + "Arduino-Esp8266")
  print("Arduino ESP8266 Extension downloaded...")
  for item in xtensa['systems']:
    if host in item['host']:
      urllib.urlretrieve(item['url'], download_path + item['archiveFileName'])
      tfile = tarfile.open(download_path + item['archiveFileName'], 'r:gz')
      tfile.extractall(tools_path)
      print("Xtensa lx106 elf tools downloaded...")
      break

  for item in esptool['systems']:
    if host in item['host']:
      urllib.urlretrieve(item['url'], download_path + item['archiveFileName'])
      tfile = tarfile.open(download_path + item['archiveFileName'], 'r:gz')
      tf = tfile.getmembers()[1:]

      tfile.extractall(tools_path, tf)
      os.rename(tools_path + item['archiveFileName'][:-7], tools_path + "esptool")
      print("esptool downloaded...")
      break

  for item in mkspiffs['systems']:
    if host in item['host']:
      urllib.urlretrieve(item['url'], download_path + item['archiveFileName'])
      tfile = tarfile.open(download_path + item['archiveFileName'], 'r:gz')
      tf = tfile.getmembers()[1:]

      tfile.extractall(tools_path, tf)
      os.rename(tools_path + item['archiveFileName'][:-7], tools_path + "mkspiffs")
      print("mkspiffs downloaded...")
      break

def main():
  host = defineHost()
  print("System Host: " + host)
  if host:
    print("Downloading...")
    downloadTools(host)
    print("Done!")
  else:
    print("Not supported OS!")

if __name__ == '__main__':
  main()