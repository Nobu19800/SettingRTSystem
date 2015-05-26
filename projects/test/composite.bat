cmd /c rtcomp /localhost/test.rtc -a /localhost/MyFirstComponent0.rtc -a /localhost/MySecondComponent0.rtc
cmd /c rtconf /localhost/test.rtc set exported_ports MySecondComponent0.out,MyFirstComponent0.in
