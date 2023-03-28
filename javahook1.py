import sys
import frida


js_code = '''
Java.perform(function(){
    console.log("[*] START...")
    var mClass = Java.use("sg.vantagepoint.uncrackable1.MainActivity$1")
    mClass.onClick.implementation=function() {
        console.log("[*] Clicked ")
    }
});
'''


def on_message(msg, data):  # js中执行 send 函数后要回调的函数
    if msg['type'] == 'send':
        print(f'[*] {msg["payload"]}')
    else:
        print(msg)


if __name__ == '__main__':
    # get_remote_device 获取远程设备　(get_usb_device)　　attach 附加进程
    process = frida.get_remote_device().attach('uncrackable1')
    script = process.create_script(js_code)
    script.on('message', on_message)  # 绑定一个事件
    script.load()
    sys.stdin.read()
    pass
