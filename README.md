# Radia-track
Este script guarda la radiación solar por hora en un archivo JSON](https://github.com/exitcas). Datos proveídos por la [Estación Meteorológica Automática
de la UNLP](https://meteo.fcaglp.unlp.edu.ar/).

**[ADVENTENCIA]**: Este script usa la hora de su dispositivo para determinar el horario.

## Instalar
### Correr en Python
1. Descargá `radiatrack.py` o cloná este repositorio con `git clone https://github.com/exitcas/radiatrack.git`.
2. Instalá dependencias con `pip install -r requirements.txt`.
3. Corré el script con `python radiatrack.py`.
### Compilar
1. Cloná este repositorio con `git clone https://github.com/exitcas/radiatrack.git`.
2. Instalá dependencias con `pip install -r requirements.txt`.
3. Instalá [PyInstaller](https://pyinstaller.org/) con `python -m pip install pyinstaller==6.1.0`.
4. Corré `pyinstaller radiatrack.py --onefile --icon sarpado.ico`.
### Usar el binario pre-compilado (solo Win x64)
1. Crea una carpeta donde colocar tu binario y tu archivo "`radiacion.json`".
2. Descargá un binario [acá](https://github.com/exitcas/radiatrack/releases).
3. Ejecutá `radiatrack64.exe`.
