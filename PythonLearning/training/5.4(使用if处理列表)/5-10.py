#coding:gbk
current_users=['ryan','lancy','suki','gigi','GUCCI']
new_users=['Ana','Tom','Byrant','jay','gucci']
#������Ϊ��Ҫ���Դ�Сд�Ƚϣ��Ȱ�current_users�б������Ԫ��ȫ��תΪСд
save_users=[]
for current_user in current_users:
    save_users.append(current_user.lower())
print(save_users)
#�������б����
#save_users=[current_user.lower() for current_user in current_users]
#print(save_users)
for new_user in new_users:
    if new_user in save_users:
        print('The name' + ' ' + new_user.title() + ' ' + 'had been used')
    else:
        print('Hi' + ' ' + new_user.title() + ',' + 'you can used this name')
