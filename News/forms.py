from datetime import date
from django import forms
from .models import Author, News,Category, Comment

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name','email','address','image','date']

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
        self.fields['date'].widget.attrs.update({
            'class': 'form-control date-time-picker',
        })
        # self.fields['category'].widget.attrs.update({
        #     'class': 'form-control select2'
        # })
 

class NewsForm(forms.ModelForm):
    class Meta:
        model=News
        fields=['category','title','image','details', 'date']
        # date = forms.DateTimeField (input_formats=['%d/%m/%Y %H:%M'])
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

        
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['title'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder':'enter your title'
        })
        self.fields['date'].widget.attrs.update({
            'class': 'form-control date-time-picker',
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


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['author','news','name','email','comment','status']

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


