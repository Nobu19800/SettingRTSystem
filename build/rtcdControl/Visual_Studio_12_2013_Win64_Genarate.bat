cd /d %~dp0
cmake ../../rtcdControl/ -G "Visual Studio 12 2013 Win64" -D CMAKE_INSTALL_PREFIX="C:/OpenRTM-aist" ../../rtcdControl/
copy ..\..\rtcdControl\RTC.xml RTC.xml
