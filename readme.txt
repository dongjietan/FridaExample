0.安装tools
pip install frida-tools==1.3.2
卸载tools
pip uninstall frida-tools

查看cpu架构:
adb shell getprop ro.product.cpu.abi

https://github.com/frida/frida/releases
下载对应版本，比如：frida-server-12.4.6-android-arm
改名:frida-server.xz
xz -d frida-server.xz
adb push frida-server /data/local/tmp/

mount -o rw,remount /system
cp frida-server /system/app

1.启动frida-server
adb shell
su
cd /data/local/tmp/
./frida-server &
frida-ps -U

如果出现“frida.ServerNotRunningError: unable to connect to remote frida-server”的错误，试试端口转发：
adb forward tcp:27042 tcp:27042
adb forward tcp:27043 tcp:27043

2.关闭frida-server
ps | grep frida-server
kill -9 pid

3.删除
rm -R frida*


4.测试
frida-ps -U 查看正在运行的进程可以用
frida-ps -Ua 列出运行中的程序
frida-ps -Uai 列出安装的程序





adb pull /data/data/com.example.apptobehook/lib/libhello.so /Users/jayce/Desktop/test
adb pull /data/data/com.example.apptobehook/lib/libtargetLib.so /Users/jayce/Desktop/test



ConfigManager::LoadPlayerConfigFile(void)
CoreGlobals::GetFullScreenDisable
PlatformFileManager
MapWindowNameToRandomNumericString
PlatformFileManager::FileGetDates
AndroidResDirectoryManager::OpenResourceFile
Decompress
Decode
CoreFileManager::FileReadBytes(FlashFileString const&,void *,uint)
File
coreplayer::Surface::AddBlackHoleEdge(SPOINT &,SPOINT &,RColor *)
Scale9Info::ProcessSurface(MMgc::GCAPI::GCRef<SObject>,MATRIX const&,MATRIX const&,Scale9Info*,Scale9Info const*,double,double)
SurfaceImage::SurfaceImage(CorePlayer *,Canvas *,bool,bool)
SurfaceImage::PaletteMap(Canvas *,SRECT const&,SPOINT const&,uint *,uint *,uint *,uint *)
FlashVideo::ScreenShareAdapter::DecompressBlock(uchar *,uint *,uchar const*,uint)
BlockedCodec::DecompressIntermediateBlock(uchar *,uint *,uchar const*,uint,BitmapDataBlock
BlockedCodec::UnpackOneV2Block(BitmapDataBlock *,char,uchar *,uint,uchar *,uint *)
BitmapDataBlock::SetConvertedData(uchar *,int)
BitmapDataBlock::SetPreviousData(uchar *,int)ZLibVideoDecompressor::DecompressBlock(uchar *,uint *,uchar const*,uint)
BitmapDataBlock::SetupData(uchar *,int,uchar **,int *,int *)
BlockedCodec::DecompressBlock(uchar *,uint *,uchar const*,uint)
GIFReader::GetDataBlock(uchar *)
RTMFPUtil::AESContext::DecryptBlock(void const*,void *)
BitmapDataBlock::SetupData(uchar *,int,uchar **,int *,int *)
