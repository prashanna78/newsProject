from django import forms
from .models import Author, News,Category

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name','email','address','image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder':'enter your name'
        })
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        # self.fields['category'].widget.attrs.update({
        #     'class': 'form-control select2'
        # })
 

class NewsForm(forms.ModelForm):
    class Meta:
        model=News
        fields=['category','title','image','details']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder':'enter your title'
        })
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
 
class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['title','category_image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder':'enter your title'
        })
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
