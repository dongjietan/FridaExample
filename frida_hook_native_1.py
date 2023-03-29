import sys
import frida


js_code = '''
setImmediate(function(){
    var ptr_func = Module.findExportByName("libnative-lib.so","Java_com_example_frida_1native_1demo_MainActivity_resultInt");
    console.log("ptr_func", ptr_func);
    Interceptor.attach(ptr_func, {
        onEnter: function(args) {
            console.log('onEnter');
            send(args[2]);
            send(args[3]);
            send(args[4]);
        },
        onLeave: function(retval) {
            console.log('onLeave');
            console.log(retval);
            send(retval)
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
