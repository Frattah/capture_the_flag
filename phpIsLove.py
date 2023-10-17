import requests

url = 'http://phpislove.challs.cyberchallenge.it/'
data = {'code' : '}print(${$strings{4}});#'}
r = requests.post(url, data=data)
print(r.text[r.text.find('CCIT{') : r.text.find('}') + 1])
print(r.headers)

# WRITE UP #################################################################################
#                                                                                            
# GENERAL CONSIDERATION ABOUT CODE FUNCTIONING                                              
# ------------------------------------------------------------------------------------------ 
# In the first section of the code there is an if statement that controls get arguments:      
# if there is a 'source' argument, the server shows the source code,                         
# else it shows the html page with the input form. This form sends our queries to server and   
# puts it automatically into the 'code' argument.                                             
# ------------------------------------------------------------------------------------------ 
# We can access to the second section using the 'code' argument and we can manipulate its    
# behavior to perform a cmd injection attack.                                                
# First of all the 'code's content is saved in $code variable and it must pass a security    
# control that pretends to block intrusions.                                                  
# We can see a blacklist composed by some variables, some useful functions and all internal   
# functions of php.                                                                           
# So we have to search a command that can lets us stamp flag variables' content without       
# trigger the security system.                                                              
# ------------------------------------------------------------------------------------------ 
# SEARCHING VULNERABILITIES
# Some notes:                                                    
# 1. To use blacklists is always a bad idea, someone will find a way to elude it!            
# 2. We are working with PHP/7.1.8, we can find this information looking the X-Powered-By   
#    variable in the header.                                                                
# 3. The code allows us to create an arbitrary function but this function apparently won't  
#    be never launched.                                                                      
# ------------------------------------------------------------------------------------------
# However reading documentation about 'create_function', we can discover that it is          
# deprecated because its implementation performs an internal eval() call. In the eval call   
# php declares an anonymous function in a similar way:                                       
#                                                                                            
#                       eval("function {$name}({$args}) { {$code} }");                       
#                                                                                            
# On this link https://www.exploit-db.com/exploits/32417 we can find an usefull exploit.     
#                                                                                            
#                       return -1 * var_dump($a[""]);}phpinfo();/*"]';                       
#                                                                                            
# This exploit close prematurely the corp of the anonymous function and makes the eval call  
# execute an arbitrary code followed by a comment character to eliminate the closed curly   
# braket.                                                                                     
# But we have some troubles:                                                                 
# First off all we can't use '/*' but we could substitute it with an '#' and obtain 
# the same behavior.          
# We must find a way to print the $flag content without using echo or var_dump()              
# ------------------------------------------------------------------------------------------
# RESOLUTION                                                                                 
# All blacklists are incompletes... Infact we can use 'print' to stamp the content.          
# So the exploit begins to take shape:                                                       
#                                                                                            
#                       }print($flag);#                                                      
#                                                                                            
# We have removed some usless component from the exploit in order to facilitate the          
# understanding. A careful eye would notice that we can't use 'flag' string because it is    
# in the blacklist, but we can use the blacklist against herself...                          
# We can call blacklist's items using '{}' instead of '[]', because they are supported on 
# this php version and then we can use the '${variable]' sintax to reference to the $flag 
# variable using a string. So the final exploit became:
# 
#                       }print(${$strings{4}});#
# 
# Now we can easily send a POST http request to the web server, filter its response and
# obtain the flag.
# ------------------------------------------------------------------------------------------