from django import forms
from .models import Product_list, Project

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product_list
        fields = ['Product_Image', 'Product_Name', 'Product_Cat', 'Product_Description']
    
    Product_Description = forms.CharField(
        widget=forms.Textarea,
        help_text="Enter each description item on a new line."
    )

    def clean_Product_Description(self):
        description_text = self.cleaned_data['Product_Description']
        return description_text.splitlines()

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['Project_Image', 'Project_Name']
