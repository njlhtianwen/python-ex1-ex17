# -*- coding: UTF-8 -*-  
# 定义x字符串
x = "There are %d types of people." % 10

# 将右边的字符串定义到左边的变量中
binary = "binary"
do_not = "don't"

# 引号中％和字母相连，代表输出格式，引号外％后有空格，后面是变量
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'" % y

# 定义逻辑性变量
hilarious = False

# 定义输出自身格式的变量
joke_evaluation = "Isn't that joke so funny?! %r"

# 输出两个变量，中间用％相隔
print joke_evaluation % hilarious

# 定义字符串
w = "This is the left side of..."
e = "a string with a right side."

print w + e
