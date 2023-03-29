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

    var ptr_func = Module.findExportByName("libhello.so","Java_com_example_apptobehook_MainActivity_hello") //对函数名hook
    console.log("ptr_func", ptr_func);
    Interceptor.attach(ptr_func,{
        onEnter: function(args) {
            send("Hook start");
        },
        onLeave: function(retval){
            console.log('onLeave');
            console.log('return pointer: ' + retval);
            // console.log('return: ' + Memory.readCString(retval));
            // var bbbbb = Memory.allocUtf8String('BBBBB');
            // retval.replace(bbbbb);
            var env = Java.vm.getEnv();
            var jstrings = env.newStringUtf('fuck');
            retval.replace(jstrings);
        }
    });
});
