
# dpg-nuitka-example <br>

simple cross platform dpg app compiling with nuitka <br>
running on MacOS 12.2, Windows 10 and Ubuntu 22.04<br>

## windows installation <br>

```
pip3 install virtualenv
virtualenv venv && .\venv\Scripts\activate
pip3 install dearpygui
pip3 install Nuitka
nuitka --windows-disable-console --windows-icon-from-ico=./images/icons/appstore.ico --standalone --output-dir=./dist/ main.py
```

## linux installation <br>

```
python3 -m venv venv && source venv/bin/activate
pip3 install dearpygui
pip3 install Nuitka
mkdir dist
sudo apt-get install -y patchelf
python3 -m nuitka --standalone --output-dir=./dist/ main.py
./dist/main.dist/main.bin
```

## macos installation <br>

```
python3 -m venv venv && source venv/bin/activate
pip3 install dearpygui
pip3 install Nuitka
// pip3 install pyinstaller
// wget http://nuitka.net/releases/Nuitka-0.7.6.tar.gz
// tar -xf Nuitka-0.7.6.tar.gz
// cd Nuitka-0.7.6 && python3 setup.py install
// pyinstaller --onefile --icon=./images/icons/appstore.icns --name=dpgnuitkaexample main.py
python3 -m nuitka --macos-create-app-bundle --macos-disable-console --macos-app-icon=./images/icons/appstore.icns --output-dir=./dist/ main.py
```