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

Memory.readByteArray(args[0],256) 读取 const char *， 然后传递给send(message[, data])的第二个参数data
Memory.readUtf8String(args[0])
Memory.readCString(args[2])

如何将c中的字符串转成js string?
console.log('onLeave GetStringUTFChars:', ptr(retval).readCString())

function getjstring(jstr) {
        return Java.vm.getEnv().getStringUtfChars(jstr, null).readCString();
    }
let cstring = Memory.allocUtf8String("xiaoweigege");

send(retval.toInt32()); // 转到10 进制显示内容

写文件
function write_data() {
    const file = new File('/sdcard/reg.dat', 'w');
    file.write('EoPAoY62@ElRD');
    file.flush();
    file.close()

}

把C函数定义为NativaFunction来写文件
// hook libc.so 的方式来写文件
function write_data_native() {
    // 读取lic的导出函数地址
    const addr_fopen = Module.findExportByName('libc.so', 'fopen');
    const addr_fputs = Module.findExportByName('libc.so', 'fputs');
    const addr_fclose = Module.findExportByName('libc.so', 'fclose');

    console.log('fopen:', addr_fopen, 'fputs', addr_fputs, 'fclose', addr_fclose);
    // 构建函数
    const fopen = new NativeFunction(addr_fopen, 'pointer', ['pointer', 'pointer']);
    const fputs = new NativeFunction(addr_fputs, 'int', ['pointer', 'pointer']);
    const fclose = new NativeFunction(addr_fclose, 'int', ['pointer']);

    // 申请内存空间
    let file_name = Memory.allocUtf8String('/sdcard/reg.dat');
    let model = Memory.allocUtf8String('w+');
    let data = Memory.allocUtf8String('EoPAoY62@ElRD');
    let file = fopen(file_name, model);
    let ret = fputs(data, file);
    console.log('fputs ret: ', ret);
    fclose(file);

}


直接调用.so
https://blog.51cto.com/u_15057811/3385898


常用方法：
https://www.buaq.net/go-103009.html
https://kuizuo.cn/docs/frida-so-hook

操作手册：
https://github.com/hookmaster/frida-all-in-one

教程：
https://eternalsakura13.com/2020/07/04/frida/


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
