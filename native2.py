import frida
import sys

jscode = """
Java.perform(function(){
    var modules = Process.enumerateModules();
    for (var i in modules){
        var module = modules[i];
        console.log(module.name);
    }

    //对函数名hook
    //var ptr_func = Module.findExportByName("libnative2.so","Java_com_example_apptobehook_MainActivity_checkifstream");
    var ptr_func = Module.findExportByName("","dlopen");
    console.log("ptr_func", ptr_func);
    Interceptor.attach(ptr_func, {
        //onEnter: 进入该函数前要执行的代码，其中args是传入的参数，一般so层函数第一个参数都是JniEnv，第二个参数是jclass，从第三个参数开始是我们java层传入的参数
        onEnter: function(args) {
            send("onEnter");
            this.path = Memory.readUtf8String(args[0]);
            console.log(this.path);
        },
        onLeave: function(retval) { //onLeave: 该函数执行结束要执行的代码，其中retval参数即是返回值
            console.log('onLeave');
            if (!retval.isNull() && this.path.indexOf(libnative2.so) != -1 && didHookApis) {
                didHookApis = true;
                console.log("File loaded hooking");
                hooknative2();
            }
        }
    });

    function hooknative2() {
        var ptr_func = Module.findExportByName("libnative2.so","Java_com_example_apptobehook_MainActivity_checkifstream");
        console.log("ptr_func", ptr_func);
        Interceptor.attach(ptr_func, {
            onLeave: function(retval) {
                console.log('onLeave');
                if (!retval.isNull() && this.path.indexOf(libnative2.so) != -1 && didHookApis) {
                    retval.replace(0);
                }
            }
        });
    }
});
"""

def printMessage(message,data):
    if message['type'] == 'send':
        print('[*] {0}'.format(message['payload']))
    else:
        print(message)

process = frida.get_remote_device().attach('apptobehook') #进程名
script = process.create_script(jscode)
script.on('message',printMessage)
script.load()
sys.stdin.read()
