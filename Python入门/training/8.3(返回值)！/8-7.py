#coding:gbk
def make_album(singer,album,year=''):
    cd_name = {'name':singer,'cd':album}
    if year:
        cd_name['year'] = year
    return cd_name

cd_1 = make_album('�ܽ���','����',2019)
print(cd_1)

cd_2 = make_album('����','Ը��һ����')
print(cd_2)

cd_3 = make_album('����','Ը�����������㻷�����')
print(cd_3)
