cd ..\..\Manager
start C++\rtcd_p\Release\rtcd_p.exe -f ../projects/test/C++/rtc.conf
start python Python\rtcd.py -f ../projects/test/Python/rtc.conf
cd ..\projects\test
sleep 5
cmd /c composite.bat
cmd /c rtsystem.bat
