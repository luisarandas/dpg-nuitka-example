
# dpg-nuitka-example <br>

simple cross platform dpg app compiling with nuitka <br>
running on MacOS 12.2<br>

## macos installation <br>
python3 -m venv venv && source venv/bin/activate<br>
pip3 install dearpygui<br>
pip3 install Nuitka<br>
// pip3 install pyinstaller<br>
// wget http://nuitka.net/releases/Nuitka-0.7.6.tar.gz<br>
// tar -xf Nuitka-0.7.6.tar.gz<br>
// cd Nuitka-0.7.6 && python3 setup.py install<br>
// pyinstaller --onefile --icon=./images/icons/appstore.icns --name=dpgnuitkaexample main.py<br>
python3 -m nuitka --macos-create-app-bundle --macos-disable-console --macos-app-icon=./images/icons/appstore.icns --output-dir=./dist/ main.py

## linux installation <br>

python3 -m venv venv && source venv/bin/activate<br>
pip3 install dearpygui<br>
pip3 install Nuitka<br>
python3 -m nuitka --standalone --output-dir=./dist/ main.py<br>
./dist/main.dist/main.bin<br>

## windows installation <br>

pip3 install virtualenv<br>
virtualenv venv && .\venv\Scripts\activate<br>
pip3 install dearpygui<br>
pip3 install Nuitka<br>
nuitka --windows-disable-console --windows-icon-from-ico=./images/icons/appstore.ico --standalone --output-dir=./dist/ main.py