class CreateCode:
    def __init__(self):
        a= "aa"
    def getScript(k,counter):
        if ') throws ' in k:
            k = k[0: k.index(')')+1]
        param = k.index(')') - k.index('(') # check if parameters are empty 1= yes more than one than nono
        start_param = k.index('(')
        end_param = k.index(')')
        full_class_name = k.split(' ')
        class_len = len(full_class_name)
        parameters = full_class_name[class_len-1].split('(')[1][0:-1]
        class_name = full_class_name[class_len-1].split('(')[0]
        method = full_class_name[class_len-1].split('(')[0]
        class_name = class_name[0:class_name.rindex('.')]
        method = method[method.rindex('.')+1:]
        inp = ""
        count_parameters = parameters.count(',')
        commas = parameters.count(',')
        for x in range(0,count_parameters+1):
            if x == 0:
                inp += "a" + str(x)
            else:
                inp += ",a" + str(x)
        jscode = ""
        jscode += "var x"+counter+" = Java.use('"+class_name+"');\n"
        jscode += "var y"+counter+" = x"+counter+"."+method+";\n"
        if param > 1:
            jscode += "y"+counter+".implementation = function("+inp+"){\n"
        else:
            jscode += "y"+counter+".implementation = function(){\n"
        if count_parameters > 0 or param > 1:
            jscode += "var result = y"+counter+".call(this,"+inp+");\n"
        else:
            jscode += "var result = y"+counter+".call(this);\n"
        jscode += "    console.log('---->"+class_name+"."+method+"');\n"
        jscode += "return result;\n"
        jscode += "};\n"
        return(jscode)


#CreateCode.getScript("public void jakhar.aseem.diva.NotesProvider$DBHelper.onCreate(android.database.sqlite.SQLiteDatabase)",str(1))
#CreateCode.getScript("public void jakhar.aseem.diva.NotesProvider$DBHelper.onUpgrade(android.database.sqlite.SQLiteDatabase,int,int)",str(2))
#CreateCode.getScript("protected void jakhar.aseem.diva.InsecureDataStorage1Activity.onCreate(android.os.Bundle)",str(3))
#CreateCode.getScript("public void jakhar.aseem.diva.InsecureDataStorage1Activity.saveCredentials(android.view.View)",str(4))
#CreateCode.getScript("private void jakhar.aseem.diva.LogActivity.processCC(java.lang.String,int)",str(5))
#CreateCode.getScript("public void jakhar.aseem.diva.LogActivity.checkout(android.view.View)",str(6))
#CreateCode.getScript("protected void jakhar.aseem.diva.LogActivity.onCreate(android.os.Bundle)",str(7))
#CreateCode.getScript("public boolean jakhar.aseem.diva.NotesProvider.onCreate()",str(8))
#CreateCode.getScript("protected void jakhar.aseem.diva.MainActivity.onCreate(android.os.Bundle)",str(9))
#CreateCode.getScript("public boolean jakhar.aseem.diva.MainActivity.onCreateOptionsMenu(android.view.Menu)",str(10))
##CreateCode.getScript("public boolean jakhar.aseem.diva.MainActivity.onOptionsItemSelected(android.view.MenuItem)",str(11))
#CreateCode.getScript("public void jakhar.aseem.diva.MainActivity.startChallenge(android.view.View)",str(12))
#CreateCode.getScript("protected void jakhar.aseem.diva.SQLInjectionActivity.onCreate(android.os.Bundle)",str(13))
#CreateCode.getScript("public void jakhar.aseem.diva.SQLInjectionActivity.search(android.view.View)",str(14))
#CreateCode.getScript("public native int jakhar.aseem.diva.DivaJni.access(java.lang.String)",str(14))
