#Arduino-Esp8266-Makefile

### English
Makefile to build arduino sketches for ESP8266 on Linux and OSX. 
Based on Martin Oldfield [Arduino Makefile](http://www.mjoldfield.com/atelier/2009/02/arduino-cli.html)

## Installation

Clone the repository:

`git clone https://github.com/jorgegarciadev/Arduino-Esp8266-Makefile.git`

Setup the enviroment with:

`python setup.py`

it downloads the last version of Arduino ESP8266 Extension (staging version) and the tools needed for building and uploading the code (Xtensa lx106 elf, mkspiffs and esptool).

In your sketch directory place a Makefile defining project specific variables. There is an example inside the example project folder.

For uploading the firmware, connect your device and use:

`make upload`

##dependencies

ard-parse-boards requires Perl's YAML module.

The makefile uses GNU grep, on OSX you can install it with:

`brew tap homebrew/dupes && brew install grep`

###Español

Makefile para compilar sketches de Arduino para ESP8266 en Liux y OSX. Basado en [Arduino Makefile](http://www.mjoldfield.com/atelier/2009/02/arduino-cli.html) de Martin Oldfield.

##Instalación

Clonar el repositorio:

`git clone https://github.com/jorgegarciadev/Arduino-Esp8266-Makefile.git`

Configurar el entorno:

`python setup.py`

Descarga la última versión de la extensión para ESP8266 de Arduino (staging version) y las herramientas necesarias para compilar y cargar el código (Xtensa lx106 elf, mkspiffs and esptool).

Coloca un Makefile en la carpeta del project y define las variables propias de éste. Hay un archivo de ejemplo dentro de la carpeta del proyecto de ejemplo.

Para cargar el firmware, connect your device and use:

`make upload`

##dependencias

ard-parse-boards necesita el modulo YAML de Perl.

El makefile usa GNU grep, en OSX puede instalarse con:

`brew tap homebrew/dupes && brew install grep`
