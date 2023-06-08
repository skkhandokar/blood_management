from django import forms
class ListTextWidget(forms.TextInput):
    def __init__(self, data_pack, name, *args, **kwargs):
        super(ListTextWidget, self).__init__(*args, **kwargs)
        self._name = name
        self._pack = data_pack
        self.attrs.update({'list': 'list__%s' % self._name})
    def render(self, name, value, attrs=None, renderer=None):
        text_html = super(ListTextWidget, self).render(
            name, value, attrs=attrs)
        data_pack = '<datalist id="list__%s">' % self._name
        for item in self._pack:
            data_pack += '<option value="%s">' % item
        data_pack += '</datalist>'
        return (text_html + data_pack)