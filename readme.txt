python3.6

��Ҫimport�İ���
    jieba��flask��gensim

run.py:
    a. ���ն�cd�����ļ��У����롰python run.py runserver���������У���ַΪhttp://0.0.0.0:8000//����ַΪ�Լ�ip��ַ
    b. ���ĵ�ַ��app/__init__.py��

basic_parse:
    a. ���������ı��ģ������漰jieba���ķִʡ�ȥͣ�ôʡ�ȥ��������ŵȡ�
    b. preProcess���������ڴ��������ĵ��ġ�
    c. process4input���������ڴ���������ӵġ�

app/main/views.py:
    ����Flask��web��ͼ���

app/templates/base.html:
    webԴ��
app/templates/get_data.js:
    ����web��textarea�������ݻ�ȡ��


����Ϊѵ���������������й��ģ�

img_content_clean.py��
    a. ��app/data/image_info.txt��ͼƬid��app/data/Tupianku_40K.txt��id��ƥ���ͼƬ��Ϣ��ȡ�����������ı�˳���
       ��app/data/img_text.txt�У�ͼƬurl��ַ˳��洢��app/data/img_url.txt�У�������ͼƬԭ�ĵ�ַ�洢
       ��app/data/img_texturl.txt�С�
    b. �ó�����������ϣ��粻��Ҫ�ٴ����ļ������������С�

news_content_clean.py:
    a. ��app/data/news_content.txt�к�html������ı�����Ϊ�����ı���������app/data/news_content_clean.txt�С�
    b. �˴�ֻ������20,000����


train_lsi.py:
    a. lsiģ��ѵ�������ƶȲ�ѯ����
    b. ��ͼƬ�ı��ʹ����20,000�������ı���Ϊ�ֵ�ʿ⣬�ʿ�ɼ������䡣
    c. ģ��·����������/model�ļ�����

TextPic.py:
    �����������ı���ƥ���20��ͼƬurl�Լ����ı�url



