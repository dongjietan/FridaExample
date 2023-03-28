import frida  # 导入frida模块
import sys  # 导入sys模块

# 从此处开始定义用来Hook的javascript代码
js_code = """
    Java.perform(function() {
        // 获取当前安卓设备的安卓版本
        var v = Java.androidVersion;
        send('version:' + v);

        //获取该应用加载的类
        var class_names = Java.enumerateLoadedClassesSync();
        for (var i = 0; i < class_names.length; i++){
            send('class name:' + class_names[i])
        }

        var MainActivity = Java.use('com.yaotong.crackme.MainActivity'); //获得MainActivity类
        var java_string = Java.use('java.lang.String');
        MainActivity.securityCheck.implementation = function(java_string){
            send('I am here');      // 发送信息，用于回调python中的函数
            return true;            //劫持返回值，修改为我们想要返回的字符串
        }
    });
"""


def on_message_1(msg, data):
    if msg['type'] == 'send':
        print(f'[*] {msg["payload"]}')
    else:
        print(msg)


def on_message(msg, data):  # js中执行send函数后要回调的函数
    print(msg)


# 得到设备并劫持进程 com.example.testfrida
# (刚开始用get_usb_device函数用来获取设备，但是一直报错找不到设备，改用get_remote_device函数即可解决这个问题)
process = frida.get_remote_device().attach('自毁程序密码')
script = process.create_script(js_code)  # 创建js脚本
script.on('message', on_message)  # 加载回调函数，也就是js中执行send函数规定要执行的python函数
script.load()  # 加载脚本
sys.stdin.read()
