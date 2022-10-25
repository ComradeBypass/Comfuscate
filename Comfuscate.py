import base64, codecs, random, os, zlib

def setup():
    global file_to_obfuscatestr
    global curdirectory
    global a
    global imports
    global prepped

    file_to_obfuscate = input("[Comfuscate] File you want to obfuscate (needs to be in the same folder as the obfuscator): ")
    file_to_obfuscatestr = str(file_to_obfuscate)

    curdirectory = os.path.dirname(os.path.abspath(__file__))

    file_to_obfuscate_open = open(curdirectory+"\\"+file_to_obfuscatestr, "r")
    a = str(file_to_obfuscate_open.read())
    file_to_obfuscate_open.close()


    imports = """
                                            #___COMFUSCATED___#   
                                            
                                            
                                            
                                            
                                                                                  
#                                 United Forever in Friendship and Labour,                  
#                                 Our mighty Republics will ever endure.                    
#                                 The Great Soviet Union will Live through the Ages.        
#                                 The Dream of a People their fortress secure.              

#                                 Long Live our Soviet Motherland,                          
#                                 Built by the People s mighty hand.                    
#                                 Long Live our People, United and Free.                    
#                                 Strong in our Friendship tried by fire.                   
#                                 Long may our Crimson Flag Inspire,                        
#                                 Shining in Glory for all Men to see.                      

#                                 Through Days dark and stormy where Great Lenin Lead us    
#                                 Our Eyes saw the Bright Sun of Freedom above              
#                                 and Stalin our Leader with Faith in the People,           
#                                 Inspired us to Build up the Land that we Love.            

#                                 Long Live our Soviet Motherland,                          
#                                 Built by the People s mighty hand.                    
#                                 Long Live our People, United and Free.                    
#                                 Strong in our Friendship tried by fire.                   
#                                 Long may our Crimson Flag Inspire,                        
#                                 Shining in Glory for all Men to see.                      

#                                 We fought for the Future, destroyed the invaders,         
#                                 and Brought to our Homeland the Laurels of Fame.          
#                                 Our Glory will live in the Memory of Nations              
#                                 and All Generations will Honour Her Name.                 

#                                 Long Live our Soviet Motherland,                          
#                                 Built by the People s mighty hand.                    
#                                 Long Live our People, United and Free.                    
#                                 Strong in our Friendship tried by fire.                   
#                                 Long may our Crimson Flag Inspire,                        
#                                 Shining in Glory for all Men to see.

import zlib,codecs,base64
"""

    prepped = str(a.strip())

setup()


def obfuscation(contents: str) -> None:
    print("[Comfuscate] Starting obfuscation...")
    b64_content = base64.b64encode(contents.encode()).decode()

    VARIABLE_NAME = '__STAND_WITH_STALIN' * 100
    index = 0
    code = f'{VARIABLE_NAME} = ""\n'
    for _ in range(int(len(b64_content) / 10) + 1):
        _str = ''
        for char in b64_content[index:index + 10]:
            byte = str(hex(ord(char)))[2:]
            if len(byte) < 2:
                byte = '0' + byte
            _str += '\\x' + str(byte)
        code += f'{VARIABLE_NAME} += "{_str}"\n'
        index += 10
    code += f'exec(__import__("\\x62\\x61\\x73\\x65\\x36\\x34").b64decode({VARIABLE_NAME}.encode("\\x75\\x74\\x66\\x2d\\x38")).decode("\\x75\\x74\\x66\\x2d\\x38"))'
    open(curdirectory+"\\"+"Obfuscated_"+file_to_obfuscatestr,'w+').write(code)
    print("[Comfuscate] Layer 1 done!")


    bruh = codecs.encode(contents)
    a = base64.b64encode(bruh)
    b = codecs.decode(a)
    c = r"exec(codecs.decode(base64.b64decode(r'"+b+"')))"

    bruh = codecs.encode(c)
    d = base64.b32encode(bruh)
    e = codecs.decode(d)
    f = r"exec(codecs.decode(base64.b32decode(r'"+e+"')))"

    bruh = codecs.encode(f)
    g = base64.b16encode(bruh)
    h = codecs.decode(g)
    ch = r"exec(codecs.decode(base64.b16decode(r'"+h+"')))"

    bruh = codecs.encode(ch)
    i = base64.b85encode(bruh)
    j = codecs.decode(i)
    k = r"exec(codecs.decode(base64.b85decode(r'"+j+"')))"
    print("[Comfuscate] Layer 2 done!")

############################################################################ LOOPS

    bruh = codecs.encode(k)
    a = base64.b64encode(bruh)
    b = codecs.decode(a)
    c = r"exec(codecs.decode(base64.b64decode(r'"+b+"')))"

    bruh = codecs.encode(c)
    d = base64.b32encode(bruh)
    e = codecs.decode(d)
    f = r"exec(codecs.decode(base64.b32decode(r'"+e+"')))"

    bruh = codecs.encode(f)
    g = base64.b16encode(bruh)
    h = codecs.decode(g)
    ch = r"exec(codecs.decode(base64.b16decode(r'"+h+"')))"

    bruh = codecs.encode(ch)
    i = base64.b85encode(bruh)
    j = codecs.decode(i)
    k = r"exec(codecs.decode(base64.b85decode(r'"+j+"')))"

    bruh = codecs.encode(k)
    a = base64.b64encode(bruh)
    b = codecs.decode(a)
    c = r"exec(codecs.decode(base64.b64decode(r'"+b+"')))"

    bruh = codecs.encode(c)
    d = base64.b32encode(bruh)
    e = codecs.decode(d)
    f = r"exec(codecs.decode(base64.b32decode(r'"+e+"')))"

    bruh = codecs.encode(f)
    g = base64.b16encode(bruh)
    h = codecs.decode(g)
    ch = r"exec(codecs.decode(base64.b16decode(r'"+h+"')))"

    bruh = codecs.encode(ch)
    i = base64.b85encode(bruh)
    j = codecs.decode(i)
    k = r"exec(codecs.decode(base64.b85decode(r'"+j+"')))"

    bruh = codecs.encode(k)
    a = base64.b64encode(bruh)
    b = codecs.decode(a)
    c = r"exec(codecs.decode(base64.b64decode(r'"+b+"')))"

    bruh = codecs.encode(c)
    d = base64.b32encode(bruh)
    e = codecs.decode(d)
    f = r"exec(codecs.decode(base64.b32decode(r'"+e+"')))"

    bruh = codecs.encode(f)
    g = base64.b16encode(bruh)
    h = codecs.decode(g)
    ch = r"exec(codecs.decode(base64.b16decode(r'"+h+"')))"

    bruh = codecs.encode(ch)
    i = base64.b85encode(bruh)
    j = codecs.decode(i)
    k = r"exec(codecs.decode(base64.b85decode(r'"+j+"')))"

    bruh = codecs.encode(k)
    a = str(zlib.compress(bruh, 9))
    c = r"exec(codecs.decode(zlib.decompress("+"bytes("+a+")"+")))"


    W = imports+c
    print("[Comfuscate] LOOPS done!")
    
    try:
        creationoffile = open(curdirectory+"\\"+"Obfuscated_"+file_to_obfuscatestr, "x")
        creationoffile.close()
    except Exception:
        pass

    creationoffile = open(curdirectory+"\\"+"Obfuscated_"+file_to_obfuscatestr, "w")
    creationoffile.write(W)
    creationoffile.close()
    print("[Comfuscate] Comfuscate is done!")

obfuscation(prepped)
