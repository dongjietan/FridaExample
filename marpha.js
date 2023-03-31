Java.performNow(function(){
    // 遍历模块, 找基址
    Process.enumerateModules({
        onMatch:function(exp){
            if(exp.name == "libCore.so"){
                send("enumerateModules find");
                send(exp);
                return "stop";
            }
        },
        onComplete:function(){
            send("enumerateModules stop");
        }
    });

    var ptr_func = Module.findExportByName("libCore.so","_ZN19PlatformFileManager23GetOffsetToResourcePathEPKc") //对函数名hook
    console.log("ptr_func", ptr_func);

    Interceptor.attach(ptr_func,{
        onEnter: function(args) {
            send("Hook start");
            // console.log(hexdump(args[1]));
            var path = Memory.readCString(args[1]);
            console.log(path);
            if (path.includes("map1051_20_31.bin")) {
                console.log("path includes map1051_20_31.bin");
            }
        },
        onLeave: function(retval){
            console.log('onLeave');
            // console.log('return pointer: ' + retval);
        }
    });
});
