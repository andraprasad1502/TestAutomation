"""
Regular Expression
"""
import re

"""
1. Phone Number
"""
number = "+1 (201) 777-9999"
if re.match('(\+\d)?\s*\(\d{3}\)\s*\d{3}\-\d{4}$', number):
    print("Valid mobile number")
else:
    print("Invalid mobile number")


"""
2. Email Id
"""
email = "prasad_91@gmail.com"
if re.match('[a-z][\w_\.]+\@\w+\.(com|in)$', email, re.I):
    print("valid email id")
else:
    print("Invalid email id")

"""
3. Mac Address
"""
mac = "aa:12:cd:45:67:8a"
if re.match('([0-9a-f]{2}:){5}[0-9a-f]{2}$', mac, re.I):
    print("Valid mac address")
else:
    print("invalid mac address")


"""
4. IP Address
"""
ipaddr = "255.255.255.255"
#if re.match('((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])$', ipaddr):
if re.match('((25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])\.){3}(25[0-5]|(2[0-4]|1[0-9]|[1-9])?[0-9])$', ipaddr):
    print("valid ip address")
else:
    print("invalid ip address")


"""
5. Findall
"""
string = "python is a scripting lang. python is easy. python is more comfortable"
matched = re.findall('python', string)
if matched:
    print("Matched items :", matched)
else:
    print("not matched")

