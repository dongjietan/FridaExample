import frida
import sys

jscode = """
Java.performNow(function(){

    var modules = Process.enumerateModules();
    for (var i in modules){
        var module = modules[i];
        console.log(module.name);
    }

    /*
    var str_name_so = "libhello.so";    //需要hook的so名
    var n_addr_func_offset = 0x00000F1C;         //需要hook的函数的偏移
    var n_addr_so = Module.findBaseAddress(str_name_so); //加载到内存后 函数地址 = so地址 + 函数偏移
    console.log("n_addr_so", n_addr_so);
    var n_addr_func = parseInt(n_addr_so, 16) + n_addr_func_offset;
    var ptr_func = new NativePointer(n_addr_func);
    */
    var ptr_func = Module.findExportByName("libhello.so","createHello") //对函数名hook
    console.log("ptr_func", ptr_func);
    var String = Java.use('java.lang.String');
    Interceptor.attach(ptr_func,{
        //onEnter: 进入该函数前要执行的代码，其中args是传入的参数，一般so层函数第一个参数都是JniEnv，第二个参数是jclass，从第三个参数开始是我们java层传入的参数
        onEnter: function(args) {
            send("Hook start");
        },
        onLeave: function(retval){ //onLeave: 该函数执行结束要执行的代码，其中retval参数即是返回值
            console.log('onLeave');
            console.log('return pointer: ' + retval);
            console.log('return: ' + Memory.readCString(retval));
            //var bbbbb = Memory.allocUtf8String('BBBBB');
            //retval.replace(bbbbb);
        }
    });
});
"""
def printMessage(message,data):
    if message['type'] == 'send':
        print('[*] {0}'.format(message['payload']))
    else:
        print(message)

process = frida.get_remote_device().attach('com.example.apptobehook') #进程名
script = process.create_script(jscode)
script.on('message',printMessage)
script.load()
sys.stdin.read()
