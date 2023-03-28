import sys
import frida


js_code = '''
setImmediate(function(){
    send("start");
    // 遍历模块，找基址
    Process.enumerateModules({
        onMatch:function(exp){
            if(exp.name == "libnative-lib.so"){
                send("enumerateModules find");
                send(exp.name + "|" + exp.base + "|" + exp.size + "|" + exp.path);
                send(exp);
                return "stop";
            }
        },
        onComplete:function(){
            send("enumerateModules stop");
        }
    });

    // hook 导出函数
    var exports = Module.enumerateExportsSync("libnative-lib.so");
    for (var i = 0; i < exports.length; i++){
        send("name:" + exports[i].name + "    address:" + exports[i].address);
    }

    // 通过模块名直接查找基址
    var baseAddress = Module.findBaseAddress("libnative-lib.so");
    Interceptor.attach(baseAddress.add(0x0000F7F0), {
        onEnter:function(args){
            send(args[2]);
            send(args[3]);
            send(args[4]);
            //send(Memory.readCString(args[2]));
            //send(Memory.readCString(args[3]));
            //send(Memory.readCString(args[4]));
        },
        onLeave:function(ret_val){
            console.log(ret_val);
            send(ret_val)
        }
    });
})
'''


def message(msg, data):
    if msg['type'] == 'send':
        print(f'[*] {msg["payload"]}')
    else:
        print(msg)


if __name__ == '__main__':
    # get_remote_device 获取远程设备　(get_usb_device)　　attach 附加进程
    process = frida.get_remote_device().attach('frida_native_demo')
    script = process.create_script(js_code)
    script.on('message', message)  # 绑定一个事件
    script.load()
    sys.stdin.read()
    pass
