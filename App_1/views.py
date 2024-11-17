from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . models import Product_list, Project
from . form import ProductForm, ProjectForm
from django.core.mail import send_mail
from django.conf import settings

def Home(request):
    list = Project.objects.all()
    return render(request,"home.html",{'project' : list})

def Upload_Product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('AdminMenu')
    else:
        form = ProductForm()
    return render(request, 'UploadProduct.html', {'form': form})

def Product(request):
    list = Product_list.objects.all()
    return render(request,'product.html',{'product' : list})

def AdminMenu(requset):
    list = Product_list.objects.all()
    p_list = Project.objects.all()
    return render(requset,'AdminMenu.html',{'product' : list, "p_list" : p_list})

def UpdateProduct(request, Product_id):
    product = get_object_or_404(Product_list, id=Product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():  # Call is_valid as a method with ()
            form.save()
            return redirect('AdminMenu')
    else:
        form = ProductForm(instance=product)
    return render(request, 'UpdateProduct.html', {'form': form})

def DeleteProduct(request,Product_id):
    list = Product_list.objects.get(id = Product_id)
    if request.method == 'POST':
        list.delete()
        return redirect('AdminMenu')
    return render(request,"DeleteProduct.html",{'list' : list})

def DetailProduct(request,Product_id):
    list = Product_list.objects.get(id = Product_id)
    return render(request,'DetailProduct.html',{'product' : list})

# ------------------------------------------------------------------------------

def Upload_Project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('AdminMenu')
    else:
        form = ProjectForm()
    return render(request, 'UploadProject.html', {'form': form})

def UpdateProject(request, Project_id):
    list = Project.objects.get(id=Project_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=list)
        if form.is_valid():
            form.save()
            return redirect('AdminMenu')
    else:
        form = ProjectForm(instance=list)
    return render(request, 'UpdateProject.html', {'form': form})


def DeleteProject(request,Project_id):
    list = Project.objects.get(id = Project_id)
    if request.method == 'POST':
        list.delete()
        return redirect('AdminMenu')
    return render(request,"DeleteProject.html",{'list' : list})


# -----------------------------------------------------------------

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'password123'

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check credentials
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            request.session['is_logged_in'] = True
            return redirect('AdminMenu')
        else:
            return HttpResponse("Invalid credentials", status=401)
    
    return render(request, 'login.html')

def admin_dashboard(request):
    if not request.session.get('is_logged_in'):
        return redirect('login')
    
    return render(request, 'AdminMenu.html')

def logout_view(request):
    request.session.flush()
    return redirect('login')

# ----------------------------------------------------------------------
def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Compose the email
        subject = f"New Contact Form Submission from {name}"
        email_message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage:\n{message}"
        recipient_list = ['recipient@example.com']  # Replace with your desired email

        # Send the email
        send_mail(subject, email_message, settings.EMAIL_HOST_USER, recipient_list)

        # Redirect to a success page or render a success message
        return redirect(request.path)  # Replace with your success URL

    return render(request, 'home.html')