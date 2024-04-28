from django import forms
class createNewTodo(forms.Form):
    name = forms.CharField(label="Name of todo", max_length=200)
    isDone = forms.BooleanField(required = False)
class createNewBlogpost(forms.Form):
    title = forms.CharField(widget=forms.Textarea)
    content = forms.CharField(label="Content")
class Buttonform(forms.Form):
    btn = forms.CharField()
