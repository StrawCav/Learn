"""
Search for 'math' functions: https://docs.python.org/3.9/library/math.html
Search for 'Builtin fuctions'(such as absolute values...): https://docs.python.org/3.9/library/functions.html


"""



# 查询Python的保留字 如“def，import等等”
import keyword 
print(keyword.kwlist)
print(len(keyword.kwlist)) #获取保留字符的个数（用len） 

# 多行注释用是三个英文引号
"""
Copyright: Kevin Guo..
"""
 
#变量与常量
#变量语法结构： 变量名字=value  
lucky_number = 6 #创建变量 并赋值
my_name = 'Kevin guo' # 字符串类型的变量

# The description of coding 流程图
r = float(input('Please enter the radius of the circle: '))
area = 3.14 * r * r
perimeter = 2 * 3.14 * r

print('The area of the circle is:', area, 'The perimeter of the circle is:', perimeter)

a = 3.1415926
print(f"{'a:.2f'}") #格式化输出，保留两位小数

# if函数语法结构 (注意在condtion后面不能没有冒号)
"""
if Condition 1:
    Statement 1, . . . , Statement k 
elif Condition 2:
    Statement k + 1, . . . , Statement m 
else:
    Statement m + 1, . . . , Statement n

"""
#Example : Lexicographic comparison
a = [ 2, 3 ]
b = [ 2, 2 ]
if a[0] < b[0]:
    print('a is less than b in lexicopgraphic order.')
elif b[0] < a[0]:
    print('b is less than a in lexicographic order.')
else:
    if a[1] < b[1]: 
        print('a is less than b in lexicographic order.')
    elif b[1] < a[1]:
        print('b is less than a in lexicographic order')
    else:
        print('a and b are equal')

#Example 判断奇偶
n = int(input('Please enter a number:')) #int ensures n is an integer
if n % 2:
    print(n,'is an odd number')
else:
    print(n,'is a even number')

print('the codes above can be simplified by the following')

result='is an odd number' if n % 2 else 'is a even number'
print (n, result)

# if的多分支结构
score = eval(input('please enter your final mark'))

if score < 0 or score > 100:
    print('Not a valid score')
elif 0 <= score < 60:
    print('E')
elif 60 <= score <70:
    print('D')
else:
    print ('First Class')
   
# if嵌套条件结构
answer = input('Do you drink the alcohol?')
if answer == 'y':
    proof = eval(input('please enter the vol%'))
    if proof < 20:
        print('Not drunk driving')
    elif proof < 80: #此处代表20<=proof<80
        print ('Please don not drive')
    else:
        print('Drunk driving')
else:
    print('No alcohol intake')

#多条件组合
#使用and，只有两边同时为True，正确条件才能运行 Example:
User_name=input('please enter your account number:')
Password=input('Please enter your password')
if User_name == 'gyy' and Password == '668800':
    print('Successfully Login')
else:
    print('Incorrect username and password')
#使用or链接，条件满足一个即可 Example:
score = eval(input('please enter your final marks'))
if score < 0 or score > 100:
    print('Not a vaild mark')
else:
    print('Your final mark is:', score)

#遍历循环for:
#Example 1:
for a in [ 1, 2, 3, 4, 5 ]: #此处for让括号内的数值一一罗列出来
    print(a)


L = [ 'C', 'a', 'l', 'c', 'u', 'l', 'u', 's' ]
for i in [ 0, 1, 2, 3, 4, 5, 6, 7 ]:
    print(L[i])


for i in range(len(L)):
    print(L[i])
#Example 2:
for i in 'hello': #将hello里面的字母一一提取出来
    print(i)
#Example 3: 用于range（）函数，产生一个[n,m)的正数序列，左边为闭区间，右边为开区间
for i in range(1,10):
    print(i)

for a in range(1,12):
    #可以里面加if条件语句:
    if a % 2 == 0:
        print(i,'is a even number')
#Example 3: 计算range函数里面的累加
s=0 #用于存储累加和
for i in range(1,11):
    s+=i #相当于s=s+i 累加符号
print('the sum of 1-10:', s)

#for else结构:
s=0
for i in range(1,11):
    s+=i
else:
    print('the sum of 1-10:',s) #里面for取数值的时候没有中断，直接跳到之和

#无限循环结构while:
#Example 1：用while来计算累加和 (同时补充while else结构)
s = 0
i = 1 #(1)初始化变量
while i <= 100: #（2）条件判断
    s+=i  #（3）语句块
    i+=1  # （4）改变变量 此处相当于i=i+1
else:
    print('the sum of 1-100:', s) #同for循环的else执行逻辑

#Example 2: While Loops in Maths:
a = 10

while a > 0:
    print(a)
    a = a - 1
    
a = 10

while a > 0:
    print(a)
    a -= 1 #相当于a=a-1

#break语句：
#Example 1:
L = [ 'C', 'a', 'l', 'c', 'u', 'l', 'u', 's' ]

i = 0
while i < len(L):
    print(L[i])
    i += 1
    if i == 3:
        break 

#Example 2:
s = 0
i = 1 #（1）初始化变量
while i < 11: #（2）条件判断
    #（3）语句块
    s+=i
    if s > 20:
        print('累加和大于20的当前数是:',i)
        break
    i+=1 #(4)改变变量

#  Interesting Example: 用于执行登录账号的命令：
i = 0
while i < 3:
    user_name = input('Please enter account name:')
    psw = input('Please enter password:')
    if user_name == 'gyy' and psw == '668800':
        print('Just a moment, logging')
        break
    else:
        if i < 2:
            print('Incorrect username and password, you have ',2-i,'times')
        i+=1
else:
    print('Wrong entering in three times')

# continue语句:
# Example 在while语句中
s = 0
i = 1
while i <= 100:
    if i % 2 == 1:
        i+=1
        continue #不再执行奇数相加的命令
    s += i
    i += 1
print('the sum of even numbers in 1-100 is:',s)

#Example 在for语句中
s = 0
for i in range(1,101):
    if i % 2 == 1:
        continue
    s+=i
print('the sum of even numbers in 1-100 is;',s)

#字典Dictornary
#List 
my_companies = ['Apple', 'JPMorgan', 'BlackRock', 'Blackstone'] #Each element in the list represent differnt index, from index0(Apple) to index3(Blackstone)
print(my_companies[0]) 


#创建字典
d = {10:'cat',20:'dog',30:'pet', 40:'zoo'}
#参数创建字典
d = dict(cat=10,dog=20)
print(d)

#字典属于序列，可以用max，min，len
print('max:',max(d))
print('min:',min(d))
print('number of elements:',len(d))

#字典的删除
del d

#字典元素的访问和遍历:
d = {'Hello':10, 'world':20, 'You':30}
print(d['Hello'])
print(d.get('world'))
print(d.get('me','Not exist')) #用d.get（key）相比于前者不会出现报错，在key后面可以加一个自己指定的默认值


#定义函数
def f(n):
    s=0
    for i in range(1,n+1):
        s+=i
    print(f'the sum of 1 to {n} is: {n}')
f(10)
f(100)

#return的用法
#定义一个二次函数
def g(x):
    return x ** 2 + 2 * x + 1 #return在此处返回给函数的调用处去处理

#return multiple values
#Example 1:
def calculate(a, b):
    sum_value = a + b
    difference = a - b
    product = a * b
    return sum_value, difference, product #Three values

result = calculate(5, 3)
print(result)  # Output: (8, 2, 15)

# Unpacking the result
sum_value, difference, product = calculate(5, 3)
print("Sum:", sum_value)        # Output: Sum: 8
print("Difference:", difference)  # Output: Difference: 2
print("Product:", product)        # Output: Product: 15

#Example 2:
def get_sum(x):
    s=0 #the sum of all numbers
    odd_sum=0 # the sum of odd numbers
    even_sum=0 # the sum of even numbers
    for i in range(1,x+1): 
        if i % 2 != 0: #it is an odd number
            odd_sum += i
        else:
            even_sum += i
        s += i
    return odd_sum, even_sum, s #three seperate values

result = get_sum(20)
print(result)


