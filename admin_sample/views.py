from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse,render,redirect
from .models import *
from django.contrib import messages

def index(request):
    return render(request,"index.html")

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password =request.POST.get('password')

        check_pass=UserDetailsModel.objects.filter(username=username,password=password).first()
        if check_pass:
            request.session['username']=check_pass.username
            request.session['user_id']=check_pass.id
            orders_list=OrderStatusModel.objects.all()
            messages.success(request,"Successfully Login")
            return redirect('user_dashboard')
        else:
            messages.error("This user does not exits ")
    else:
        if request.session.get('username'):
            return redirect('user_dashboard')
    return render(request,'user_login.html',)

def user_signup(request):
    if request.method=="POST":
        name=request.POST['name']
        address= request.POST['address']
        username=request.POST['username']
        password=request.POST['password']
        found=UserDetailsModel.objects.filter(username=username)
        if found :
            messages.error(request,"This username not available")
        else:
            create_user=UserDetailsModel.objects.create(
                username_name=name,
                address=address,
                username=username,
                password=password,
            )
            if create_user:
                messages.error(request,"User Created")
    return render(request,'user_signup.html')

def user_logout(request):
    if "username" in request.session:
        del request.session["username"]
    if "user_id" in request.session:
        del request.session["user_id"]
    messages.success(request,"Successfully Logout")
    return redirect('/')

def user_dashboard(request):
    if request.session.get('username'):
        user_id=request.session.get('user_id')
        if request.method == 'POST':
            pin =request.POST.get('pin')
            sel_det=SellerDetailsModel.objects.filter(pin=pin).first()
            if not sel_det:
                messages.error(request,"Seller Not Exist for this pin")
                return render(request,'user_dashboard.html')
            order_no=request.POST.get('order_no')
            found=OrderDetailsModel.objects.filter(order_no=order_no)
            if found:
                messages.error(request,'This order no already exist')
                return redirect('user_dashboard')
            ord=OrderDetailsModel.objects.create(
                order_no=order_no,
                name=    request.POST.get('name'),
                quantity= request.POST.get('quantity'),
                price= request.POST.get('price'),
                pin= pin ,
            )
            order_state_created=OrderStatusModel.objects.create(order_id = ord.id ,seller_id =sel_det.id,user_id= user_id)
            if order_state_created:
                messages.error(request,"Order Created")
    else:
        return redirect('user_dashboard')
    return render(request,'user_dashboard.html')


def user_order_list(request):
    orders_list=''
    if request.session.get('seller_username'):
        user_id=request.session['seller_id']
        orders_list=OrderStatusModel.objects.filter(user_id=user_id)
    return render(request,"user_order_list.html",{'orders_list':orders_list})

def seller_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password =request.POST.get('password')
        check_pass=SellerDetailsModel.objects.filter(username=username,password=password).first()
        if check_pass:
            request.session['seller_username']=check_pass.username
            request.session['seller_id']=check_pass.id
            return redirect('seller_dashboard')
        else:
            messages.error(request,"This seller does not exits ")
    else:
        if request.session.get('seller_username'):
            return redirect('seller_dashboard')
    return render(request,'seller_login.html',)

def seller_signup(request):
    if request.method=="POST":
        name=request.POST['name']
        state_name= request.POST['state']
        pin=request.POST['pin']
        username=request.POST['username']
        password=request.POST['password']
        found =SellerDetailsModel.objects.filter(username=username)
        if found:
            messages.error(request,"This username not available")
        else:
            create_user=SellerDetailsModel.objects.create(
                seller_name=name,
                state_name=state_name,
                pin=pin,
                username=username,
                password=password,
            )
            if create_user:
                messages.error(request,"Seller created")
    return render(request,'seller_signup.html')


def seller_logout(request):
    if "seller_username" in request.session:
        del request.session["seller_username"]
    if "seller_id" in request.session:
        del request.session["seller_id"]
    messages.success(request,"Successfully Logout")
    return redirect('/')

def seller_dashboard(request):
    orders_list=''
    if request.session.get('seller_username'):
        seller_id=request.session['seller_id']
        orders_list=OrderStatusModel.objects.filter(seller_id=seller_id)
        if request.method=='POST':
            if  "btn_acsubmit" in request.POST :
                btn_value=request.POST["btn_acsubmit"]
                order_id=request.POST[f"order{btn_value}"]
                OrderStatusModel.objects.filter(order_id=order_id).update(
                    seller_action= 1,
                    remark= "Accepted"
                )
                return redirect('seller_dashboard')
            
            if  "btn_rjsubmit" in request.POST :
                btn_value=request.POST["btn_rjsubmit"]
                order_id=request.POST[f"order{btn_value}"]
                remark=request.POST[f"remark{btn_value}"]
                OrderStatusModel.objects.filter(order_id=order_id).update(
                    seller_action= 2,
                    remark= remark
                )
                return redirect('seller_dashboard')
    else:
        return redirect('seller_login')
    return render(request,'seller_dashboard.html',{"orders_list":orders_list})

