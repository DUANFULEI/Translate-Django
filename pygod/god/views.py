from django.shortcuts import render
import json
from urllib import parse
import urllib.request, urllib.parse
from god.forms import fanyiForm


# Create your views here.
def youdaofanyi(request):
    '''
    有道翻译功能
    '''

    query = {}  # 定义需要翻译的文本
    fanyi = request.POST.get('fanyi_content', '')
    query['q'] = fanyi  # 输入要翻译的文本
    url = 'http://fanyi.youdao.com/openapi.do?keyfrom=11pegasus11&key=273646050&type=data&doctype=json&version=1.1&' + parse.urlencode(
        query)  # 有道翻译api
    response = urllib.request.urlopen(url, timeout=5)
    # 编码转换
    try:
        html = response.read().decode('utf-8')
        d = json.loads(html)
        explains = d.get('basic').get('explains')  # 翻译后输出
        a1 = d.get('basic').get('uk-phonetic')  # 英式发音
        a2 = d.get('basic').get('us-phonetic')  # 美式发音
        explains_list = []
        for result in explains:
            explains_list.append(result)
        # 输出
        fanyi_dict = {
            'q': query['q'],
            'yinshi': a1,
            'meishi': a2,
            'explains_list': set(explains_list + d['translation']),
        }
        return fanyi_dict
    except Exception:
        try:
            fanyi_dict = {
                'q': query['q'],
                'explains_list': d['translation'],
            }
            return fanyi_dict
        except Exception as e:
            print(e)


def listblogs(request):
    '''
    翻译页面
    :param request:
    :return:
    '''
    fanyi_dict = {}
    fanyi_form = fanyiForm()
    if request.method == 'POST':
        fanyi_form = fanyiForm(request.POST)
        if fanyi_form.is_valid():
            fanyi_dict = youdaofanyi(request)

    bloglist = {
        'fanyi_form': fanyi_form,  # 翻译的表单
        'fanyi_dict': fanyi_dict,  # 翻译出来的文本
    }
    return render(request, 'fanyi.html', bloglist)
