# taobaopa
cookie 是淘宝搜索页面的newwork下DOC的cookie,在网页登录状态下的cookie，使用py需要替换
goods 是搜索的商品，可自行替换
depth 是爬虫的页码

使用.py的步骤和前提：
1、python下载安装，环境变量配置好
最好在python的安装目录下安装request、bs4、lxml等模块
2、安装requests模块，bs4和lxml可不装
pip3 install requests  //requests 请求库安装，命令行(因为python版本是3以上)
pip3 install bs4
pip3 install lxml
3、用命令行在py文件目录下，python taobao.py（或者使用pycharm打开这个py文件run）
