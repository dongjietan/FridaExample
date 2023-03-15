0.安装
pip install frida-tools==1.0.0

https://github.com/frida/frida/releases
下载对应版本，比如：frida-server-12.0.3-android-arm
改名:frida-server.xz
xz -d frida-server.xz
adb push frida-server /data/local/tmp/

1.启动frida-server
adb shell
su
cd /data/local/tmp/
./frida-server &
frida-ps -U

2.关闭frida-server
ps | grep frida-server
kill -9 pid





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
