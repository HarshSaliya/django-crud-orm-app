from django.shortcuts import render ,  redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import CreateUser  , LoginUser ,ProductForms  , RestaurantForms ,AuthorForm ,BlogForm
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import auth
from .models import Product ,Restaurant , Author ,Blog

# Create your views here.

# @login_required
def home(request):
    return render(request, 'home.html')

def loginn(request):

    form =  LoginUser()

    if request.method =="POST":
    
        form=LoginUser(request , data=request.POST)

        if form.is_valid():

            username=request.POST.get('username')
            password=request.POST.get('password')

            user= authenticate(username=username , password=password)

            if  user is not None:
                login(request , user)

                return redirect('home')    
            
    context = {'loginform' :form }

    return render(request, 'signin.html' , context=context)

def registration(request):

    form = CreateUser()

    if request.method == "POST":

        form=CreateUser(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login')
    
    context = {'registerform' :form}



    return render(request , 'signup.html' , context=context)


def logout_view(request):

    auth.logout(request)
    return redirect('loginn')
    



def create_product(request):

    form=ProductForms()
    if request.method == 'POST':
        form = ProductForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        else:
            form = ProductForms()

    return render(request , 'create_product.html' , {'form' : form})


def product_list(request):
    products= Product.objects.all()
    prod= {'products':products}
    return render(request , 'product_list.html' , prod)

#  3. UPDATE Product
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForms(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForms(instance=product)
    return render(request, 'update_product.html', {'form': form})

#  4. DELETE Product
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect('product_list')
    return render(request, 'delete_product.html', {'product': product})






def create_restaurnt(request):

    form= RestaurantForms()

    if request.method == "POST":
        form = RestaurantForms(request.POST)

        if form.is_valid():
            form.save()
            return redirect('restaurant_list')
        else:
            form = RestaurantForms()
        
    return render (request ,'create_restaurant.html' , { 'forms' : form})


def restaurant_list(request):
    try:
        rest =Restaurant.objects.all()

    except :
        print("something happpend")

    finally:
        print("its called ")
    return render(request , 'restaurant_list.html' , {'rest' :rest})


def delete_restaurnt(request ,pk):
    rest=get_object_or_404(Restaurant,pk=pk)

    if request.method=="POST":
        rest.delete()
        return redirect('restaurant_list')
    return render(request , 'delete_restaurnt.html' , {'rest' : rest})


def update_restaurnt(request , pk):
    rest = get_object_or_404(Restaurant, pk=pk)

    if request.method == "POST":
        form= RestaurantForms(request.POST , instance=rest)
        if form.is_valid():
            form.save()
            return redirect('restaurant_list')
    else:
        form = RestaurantForms(instance=rest)
    return render(request , 'update_restaurnt.html' ,{'form' : form})




def create_author(request):
    form =AuthorForm()

   
    if request.method=="POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()

    return render (request , 'create_author.html' ,{'form': form})


def author_list(request):
    author=Author.objects.all()
    data={'aj' : author}
    return render(request , 'author_list.html' ,data)


def delete_author(request ,pk):
    auth=get_object_or_404(Author , pk= pk)
    if request.method =="POST":
        auth.delete()
        return redirect('author_list')
    
    return render(request ,'delete_author.html' , {'auth':auth} )


def update_author(request , pk):
    authert = get_object_or_404(Author, pk=pk)

    if request.method=="POST":
        form= AuthorForm(request.POST , instance=authert)

        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm(instance=authert)

    return render(request , 'update_author.html' , {'form':form})


def create_blog(request):
    form = BlogForm()

    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request , 'create_blog.html' , {'form':form})
        

def blog_list(request):
    blog=Blog.objects.all()
    return render(request, 'blog_list.html' , {'blog':blog})

def delete_blog(request , pk):
    data =get_object_or_404(Blog , pk=pk)

    if request.method == "POST":
        data.delete()
        return  redirect('blog_list')
    
    return render(request , 'delete_blog.html' , {'form':data})

def update_blog(request , pk):
    data=get_object_or_404(Blog , pk=pk)

    if request.method == "POST":

        data = BlogForm(request.POST  , instance=data)

        if data.is_valid():
            data.save()
            return redirect('blog_list')
        
    else:
        data = BlogForm(instance=data)

    return render(request , 'update_blog.html' , {'form':data})