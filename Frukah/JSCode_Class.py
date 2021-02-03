import random

class JSCode_Class:
    quote = ("\nCoffee doesn't care if you wear pants\nCoffee doesn't wear pants either - kk \n",
    "Not all who wander are lost.Most of them are looking for coffee. -kk\n",
    "\nIm pretty sure I just heard my coffee pot whisper, your my B - kk\n",
    "\nDinos had no coffee. How did that work out? - kk\n",
    "\nI dont bench press, I french press - kk\n",
    "\nDecaf is like a lady of the night that just cuddles - kk\n",
    "\nI dream in coffee <> eeffoc ni maerd i - kk\n",
    "\neeffoc ni maerd i, is latin for 'I dream in Coffee'- kk",
    "\nThat caffeine powers a man's mind - kk\n",
    "\nInsert coffee to begin - kk\n",
    "\nFrida works on coffee, it injects itself into the soul of that APK like it injects the caffiene into you - kk \n",
    "\nDynamic analysis is better with coffee - kk\n",
    "\nBuy me coffee -kk\n",
    "\nBe coffee - kk\n",
    "\nI pretty sure Bruce meant to say is be like coffee, become coffee. when coffee is in a coffee pot it becomes the pot - kk\n",
    "\nCoffee pot is legal - kk\n"
    "\nCoffee is a survival juice - kk\n",
    "\nUrban survival requires covfefe - kk\n",
    "\nIf i mispess is becus i had not have had any of that dark juice - kk\n",
    "\nForget the force, you should only be with coffee - kk\n"
    "\nekuse my mispeling. hve not had covfefe - kk\n",
    "\nDespite the negative covfefe, it's still better than no covfefe - kk\n",
    "\ncoffee is life - kk", "You dont have to pardon coffee after it makes you happy - kk\n",
    "\nForever(fə-ˈre-vər) n.The time it takes to brew the first cup/pot of coffee on a monday morning - kk\n",
    "\nVictory. The time it takes to brew the first cup/pot of coffee on a friday morning - kk\n",
    "\nIf you can't drink cofee on a hot day then you are weak and will never survive the apocalypse\n" )

    def __init__(self):
        a= "aa"


    def getScript(k,input,aclass):
        if input is None:
            return ""
        elif input == "ClassInfo":
            fa = """
            Java.perform(function() {
                Java.enumerateLoadedClasses({
                    onMatch: function(className) {
                        if(className.includes('"""+aclass+ """')){
                        console.log("*******"+className+"*********")
                        }
                    },
                    onComplete: function() {}
                });
            });"""
            return fa
        elif input == "DetailedClassInfo":
            fa = """
             Java.perform(function () {
             function enumMethods(targetClass)
             {
               var hook = Java.use(targetClass);
               var ownMethods = hook.class.getDeclaredMethods();
               hook.$dispose;
               return ownMethods;
             }
             var a = enumMethods('"""+aclass+"""')
                 a.forEach(function(s) {
                   send(s);
                 });
               });
            """
            return fa
        elif input == "GetMethodsFromClassName":
            fa = """
             Java.perform(function () {
             function enumMethods(targetClass)
             {
               var hook = Java.use(targetClass);
               var ownMethods = hook.class.getDeclaredMethods();
               hook.$dispose;
               return ownMethods;
             }
           Java.enumerateLoadedClasses({
              onMatch: function(className) {
                  if(className.includes('"""+aclass+ """')){

                      var a = enumMethods(className)
                            a.forEach(function(s){
                               send('M---->' + s);
                            });
                  }
               },
           onComplete: function() {}
              });
               });
            """
            return fa
        elif input == "EnumModules":
                fa = """main()
                function main(){

                       exploreSystemSSL_Cryptomodules();
                }
                function exploreSystemSSL_Cryptomodules(){

                  var modulesArray = Process.enumerateModules();

                  for(var i=0; i<modulesArray.length;i++){
                   console.log(modulesArray[i].path);
                  }
                  console.log("Total Number of Modules:" + modulesArray.length);

                }
           """
                return fa
