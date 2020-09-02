print('#####################################')
print('###########欢迎来到英雄无敌##########')
print('##############载入中...##############')
print('##########正在加载请耐心等待#########')
use = str(input('请输入用户名:'))
pw1 = str(input('请输入密码:'))
pw2 = str(input('请再次输入密码:'))
while True:
    if pw1 == pw2:
        print('用户名为:',use)
        print('密码为:',pw1)
        break
    else:
        print('两次密码不同 请重新输入:')
        pw1 = str(input('请输入密码:'))
        pw2 = str(input('请再次输入密码:'))
print('######################################')
name = str(input('请输入英雄的名字:'))
print('英雄的名字:',name)


a = str(input('请选择您的职业[1.法师/2.弓箭/3.坦克/4.刺客/5.奶妈]:'))
hp1 ='HP=1000'
hp2 ='HP=1000'
hp3 ='HP=3000'
hp4 ='HP=1200'
hp5 ='HP=800'
while True:
      if a =='1':
         print('您的职业为法师',hp1)
         break

      if a =='2':
         print('您的职业为弓箭',hp2)
         break
      if a =='3':
         print('您的职业为坦克',hp3)
         break
      if a =='4':
         print('您的职业为刺客',hp4)
         break
      if a =='5':
         print('您的职业为奶妈',hp5)
         break
      else:
         print('输入职业不存在请重新输入:')
         a = str(input('请选择您的职业[1.法师/2.弓箭/3.坦克/4.刺客/5.奶妈]:'))
print('#############################')
