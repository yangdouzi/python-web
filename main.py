from flask import *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('search.html')

#'/search_form'路由
@app.route('/search_form')
def search_form():
    a = request.values.get('word')
    #TODO2：使用name属性值'A组'，接收单选框数据
    res = request.values.get('A组')
    
    if res=='shop':
        url='https://search.dangdang.com/?key='+a
    if res=='video':
        url='https://search.bilibili.com/all?keyword='+a
    if res=='words':
        url='https://baike.baidu.com/item/'+a
    if res=='image':
        url='https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&dyTabStr=MCw2LDIsMyw1LDEsNCw3LDgsOQ%3D%3D&word='+a
    if res=='txt':
        url='https://wenku.baidu.com/search?ie=utf-8&word='+a
    if res=='sound':
        url='https://www.ximalaya.com/so/'+a
    if res=='app':
        url='https://appgallery.huawei.com/search/'+a
    if res=='a' or res=='b' or res=='d':
        url='https://code.xueersi.com/404'
    if res=='c':
        url='https://yangdouzi.github.io/game.html'
    return redirect(url)
    
app.run()