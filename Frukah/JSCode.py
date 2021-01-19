class JSCode:


    def __init__(self):
        a= "aa"

    def getScript(k,input):
        if input is None:
            return ""
        elif input == "FileAccess":
            fa = """Interceptor.attach(Module.findExportByName("/system/lib/libc.so", "open"), {
             onEnter: function(args) {
                var filename = Memory.readCString(ptr(args[0]));
                var x = Memory.readCString(ptr(args[1]));
                console.log('filename =', filename)
                console.log('filename =', x)
              },
              onLeave: function(retval) {
              }
            });"""
            return fa
        elif input == "SharedPrefAccess":
            sp="""Java.perform(function () {
                    var sp = Java.use("android.app.SharedPreferencesImpl$EditorImpl");
                    sp.putString.overload('java.lang.String', 'java.lang.String').implementation = function (k, v) {
                       console.log('SP-> key=' + k+ ", value=" + v);
                      return this.putString(k, v);
                    };

                });"""
            return sp
        elif input == "DBAccess":
            db="""
            Interceptor.attach(Module.findExportByName('libsqlite.so', 'sqlite3_prepare16_v2'), {
                  onEnter: function(args) {
                      console.log('DB: ' + Memory.readUtf16String(args[0]) + '\tSQL: ' + Memory.readUtf16String(args[1]));
                  }
            });
            """
            return db
        elif input == "ListModules":
            lm="""Process.enumerateModulesSync()
                .filter(function(m){ return m['path'].toLowerCase().indexOf('app') !=-1 ; })
                .forEach(function(m) {
                    console.log(JSON.stringify(m, null, '  '));
                    // to list exports use Module.enumerateExportsSync(m.name)
                });
            """
            return lm
        elif input == "DumpStrings":
            ds="""'use strict';
              rpc.exports = {
              enumerateRanges: function (prot) {
              return Process.enumerateRangesSync(prot);
              },
          readMemory: function (address, size) {
          console.log('???????????????')
           return Memory.readByteArray(ptr(address), size);
        }
       };
            """
            return ds
        elif input == "HTTP":
             http="""Java.perform(function() {
             var res2 = Java.use('com.android.okhttp.Response$Builder');
                 res2.build.implementation = function() {

                     var response = this.build();


                     console.log(response.headers())
                     //console.log(response.message())
                     var rBody = response.body();
                     //console.log(rBody.source())
                     console.log("## REQ ### ");
                     console.log(response.request());
                     console.log(response.request().headers());

                     console.log("## -REQ- ### ");
                     return response;
                 };
               var base64 = Java.use('android.util.Base64');
                 var RealResponseBody = Java.use('com.android.okhttp.internal.http.RealResponseBody');
                 RealResponseBody.$init.overload('com.android.okhttp.Headers', 'com.android.okhttp.okio.BufferedSource').implementation = function(par1, par2) {
                     console.log("ResponseBody");

                     //breaks app, because readByteArray function clears input stream
                     var body = par2.readByteArray() //Comment this line if you want app to process request
                     console.log(base64.encodeToString(body, 0)); //Comment this line if you want app to process request

                     this.$init(par1, par2);
                 }

             });"""
             return http



class Script:
    FileAcess = """
    Interceptor.attach(Module.findExportByName("/system/lib/libc.so", "open"), {
     onEnter: function(args) {
        var filename = Memory.readCString(ptr(args[0]));
        var x = Memory.readCString(ptr(args[1]));
        console.log('filename =', filename)
        console.log('filename =', x)
      },
      onLeave: function(retval) {
      }
    });
    """
    DBAccess = """
    Interceptor.attach(Module.findExportByName('libsqlite.so', 'sqlite3_prepare16_v2'), {
          onEnter: function(args) {
              console.log('DB: ' + Memory.readUtf16String(args[0]) + '\tSQL: ' + Memory.readUtf16String(args[1]));
          }
    });
    """

    SharedPrefAccess = """
    Java.perform(function () {
        var sp = Java.use("android.app.SharedPreferencesImpl$EditorImpl");
        sp.putString.overload('java.lang.String', 'java.lang.String').implementation = function (k, v) {
           console.log('SP-> key=' + k+ ", value=" + v);
          return this.putString(k, v);
        };

    });
    """

    LoadedClasses= """

    Java.perform(function() {
        Java.enumerateLoadedClasses({
            "onMatch": function(c) {
                if (c.includes("aseem")) {
                    console.log(c);
                }
            },
            onComplete: function() {}
        });
    });

    """

    ListModules= """

        Process.enumerateModulesSync()
            .filter(function(m){ return m['path'].toLowerCase().indexOf('app') !=-1 ; })
            .forEach(function(m) {
                console.log(JSON.stringify(m, null, '  '));
                // to list exports use Module.enumerateExportsSync(m.name)
            });

        """

    ListNativeModules="""
    Process.enumerateModules()
        .filter(function(m) {
            return m["path"].toLowerCase().indexOf("libnative") != -1;
        })
        .forEach(function(mod) {
            console.log(JSON.stringify(mod));
            mod.enumerateExports().forEach(function(exp) {
                if (exp.name.indexOf("fopen") != -1) {
                    console.log("fopen found!");
                }
            })
        });

        """

    jscode = """
    Interceptor.attach(Module.findExportByName("/system/lib/libc.so", "open"), {
     onEnter: function(args) {
        var filename = Memory.readCString(ptr(args[0]));
        var x = Memory.readCString(ptr(args[1]));
        console.log('filename =', filename)
        console.log('filename =', x)
      },
      onLeave: function(retval) {
        console.log(".....");
      }
    });

    Interceptor.attach(Module.findExportByName('libsqlite.so', 'sqlite3_prepare16_v2'), {
          onEnter: function(args) {
              console.log('DB: ' + Memory.readUtf16String(args[0]) + '\tSQL: ' + Memory.readUtf16String(args[1]));
          }
    });

    Java.perform(function () {

        var sp = Java.use("android.app.SharedPreferencesImpl$EditorImpl");
        sp.putString.overload('java.lang.String', 'java.lang.String').implementation = function (k, v) {
           console.log('SP-> key=' + k+ ", value=" + v);
          return this.putString(k, v);
        };

    });
    """
