import re

# pattern = re.compile('this')
pattern = re.compile(r"([a-zA-Z]).([a])")  # r stands for raw string
string = 'this search this inside of this text please!'
password_checker = re.compile(r"^[a-zA-Z0-9$%#@]{8,16}[0-9]$")
password = 'asdasds512321%$9'

# print(re.search('this', string))
# a = re.search('this', string)
a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)  # needs to be exact string
d = pattern.match(string)
check = password_checker.fullmatch(password)

print(a.span())
print(a.start())
print(a.end())
print(a.group())
# group 1 ([a-zA-Z]) searching for any letter
print(a.group(1))
# . followed by anything
# group 2 ([a]) followed by a
print(a.group(2))
print(b)
print(c)
print(d)
print(check)
