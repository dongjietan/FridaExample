frida-ps -U

adb forward tcp:27043 tcp:27043
adb forward tcp:27042 tcp:27042

/data/local/tmp/

./frida-server &

adb pull /data/data/com.example.apptobehook/lib/libhello.so /Users/jayce/Desktop/test
adb pull /data/data/com.example.apptobehook/lib/libtargetLib.so /Users/jayce/Desktop/test
