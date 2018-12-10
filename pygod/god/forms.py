from django import forms


class fanyiForm(forms.Form):
    '''
    翻译功能表单
    '''
    fanyi_content = forms.CharField(label='翻译', error_messages={
        'required': '请填写需要翻译的内容',
        'max_length': '填写的内容太长'
    }, widget=forms.TextInput(attrs={'class': 'form-item',
                                     'id': 'exampleInputContent',
                                     'placeholder': '请输入要翻译的内容',
                                     'rows': '1'
                                     }))
