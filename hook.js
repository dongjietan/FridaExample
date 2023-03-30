Java.performNow(function(){
    // 遍历模块, 找基址
    Process.enumerateModules({
        onMatch:function(exp){
            if(exp.name == "libhello.so"){
                send("enumerateModules find");
                send(exp);
                return "stop";
            }
        },
        onComplete:function(){
            send("enumerateModules stop");
        }
    });

    // // hook 导出函数
    // var exports = Module.enumerateExportsSync("libhello.so");
    // for (var i = 0; i < exports.length; i++){
    //     send("name:" + exports[i].name + "    address:" + exports[i].address);
    // }
    //
    // // 通过模块名直接查找基址
    // var baseAddress = Module.findBaseAddress("libhello.so");
    // console.log("baseAddress", baseAddress);

    var ptr_func = Module.findExportByName("libhello.so","createHello") //对函数名hook
    console.log("ptr_func", ptr_func);

    const newStr = "some strings 111";
    const newStrAddr = Memory.allocUtf8String(newStr);

    Interceptor.attach(ptr_func,{
        onEnter: function(args) {
            send("Hook start");
        },
        onLeave: function(retval){
            console.log('onLeave');
            console.log('return pointer: ' + retval);
            console.log('return: ' + Memory.readCString(retval));

            // var env = Java.vm.getEnv();
            // var jstrings = env.newStringUtf('fuck').readCString();
            // retval.replace(ptr(jstrings));

            // var aes_value = Java.vm.getEnv().getStringUtfChars(jstrings, null).readCString();
            // var jstrings = Memory.allocUtf8String('fuck');

            // var newStr = "new String";
            // var newstraddr = Memory.allocUtf8String(newStr);//写入内存，返回字符串第一个字符的地址
            retval.replace(newStrAddr);

            // return jstrings

            // var env = Java.vm.getEnv();
            // var jstrings = env.newStringUtf('fuck');
            // retval.replace(jstrings);
        }
    });
});
