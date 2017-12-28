python3.6

主要import的包：
    jieba，flask，gensim

run.py:
    a. 在终端cd到本文件夹，输入“python run.py runserver”即可运行，网址为http://0.0.0.0:8000//，地址为自己ip地址
    b. 更改地址在app/__init__.py中

basic_parse:
    a. 用来处理文本的，其中涉及jieba中文分词、去停用词、去特殊标点符号等。
    b. preProcess方法是用于处理输入文档的。
    c. process4input方法是用于处理输入句子的。

app/main/views.py:
    基于Flask的web视图框架

app/templates/base.html:
    web源码
app/templates/get_data.js:
    用于web端textarea输入数据获取。


以下为训练过程中依次运行过的：

img_content_clean.py：
    a. 将app/data/image_info.txt中图片id与app/data/Tupianku_40K.txt中id相匹配的图片信息提取出，将所有文本顺序存
       在app/data/img_text.txt中，图片url地址顺序存储在app/data/img_url.txt中，将所有图片原文地址存储
       在app/data/img_texturl.txt中。
    b. 该程序已运行完毕，如不需要再处理文件，无需再运行。

news_content_clean.py:
    a. 将app/data/news_content.txt中含html代码的文本处理为所需文本，保存在app/data/news_content_clean.txt中。
    b. 此处只处理了20,000条。


train_lsi.py:
    a. lsi模型训练，相似度查询索引
    b. 将图片文本和处理的20,000条新闻文本作为字典词库，词库可继续扩充。
    c. 模型路径均保存在/model文件夹中

TextPic.py:
    返回与输入文本最匹配的20张图片url以及其文本url



