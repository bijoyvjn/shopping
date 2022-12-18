from datetime import *
import decimal
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


@login_required()
def index(request):
    template_name = 'index.html'
    return render(request, template_name)


@login_required()
def products_listing(request):
    if request.method == "GET":
        products = Product.objects.all()
        context = {'products': products}
        return render(request, 'products.html', context)


@login_required()
def products_main_listing(request):
    if request.method == "GET":
        products = Product.objects.all()
        context = {'products': products}
        return render(request, 'product_main_list.html', context)


@login_required()
def add_product(request):
    form = ProductForm()
    template_name = "product_add.html"
    context = {'form': form}
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.created_user = str(request.user)
            data.created_at = datetime.now()
            data.save()
            messages.success(request, 'Product Successfully Added.', 'alert-success')
            return redirect('products_main_listing')
        else:
            print(form.errors)
            messages.success(request, 'Data is not valid.', 'alert-danger')
            context = {'form': form}
            return render(request, template_name, context)
    else:
        return render(request, template_name, context)


@login_required()
def edit_product(request, pk):
    products = Product.objects.get(product_id=pk)
    template_name = "product_edit.html"
    form = ProductForm(instance=products)
    context = {'form': form}
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=products)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            messages.success(request, 'Product Successfully Updated.', 'alert-success')
            return redirect('products_main_listing')
        else:
            print(form.errors)
            messages.success(request, 'Data is not valid.', 'alert-danger')
            context = {'form': form}
            return render(request, template_name, context)
    else:
        return render(request, template_name, context)


def product_delete(request, pk):
    Product.objects.get(product_id=pk).delete()
    return redirect('products_main_listing')


def cart_items(request, pk):
    if request.method == "GET":
        template_name = 'cart.html'
        cart_items = Cart.objects.filter(customer__id=pk)
        total_amount = 0
        for i in cart_items:
            total_amount += float(i.amount)

        total_amount = "{:.2f}".format(total_amount)
        customer = request.user.id
        context = {'cart_items': cart_items, 'customer': customer, 'total_amount': total_amount}
        return render(request, template_name, context)


def cart(request):
    if request.method == "GET":
        product_id = request.GET['product_id']
        count = request.GET['count']
        item = Product.objects.get(product_id=product_id)
        cart_item_exist = Cart.objects.filter(customer=request.user.id, product__product_id=product_id)
        if cart_item_exist:
            exists_details = Cart.objects.get(customer=request.user.id, product__product_id=product_id)
            new_count = int(exists_details.quantity) + 1
            new_amt = float(exists_details.amount) + float(item.price)
            new_amt = "{:.2f}".format(new_amt)
            Cart.objects.filter(customer=request.user.id, product__product_id=product_id).update(customer=request.user,
                                                                                                 product=item,
                                                                                                 quantity=new_count,
                                                                                                 amount=new_amt)
        else:
            amt = float(count) * float(item.price)
            amt = "{:.2f}".format(amt)
            Cart.objects.create(customer=request.user, product=item, quantity=count, amount=amt)

        return redirect('cart_items', pk=request.user.id)


def remove_from(request, pk):
    Cart.objects.filter(cart_id=pk).delete()
    customer = request.user.id
    return redirect('cart_items', pk=customer)


def cart_plus(request, pk):
    cart_old = Cart.objects.get(cart_id=pk)
    new_quantity = int(cart_old.quantity) + 1
    new_amt = float(cart_old.amount) + float(cart_old.product.price)
    new_amt = "{:.2f}".format(new_amt)
    Cart.objects.filter(cart_id=pk).update(
        quantity=new_quantity,
        amount=new_amt,
    )
    return redirect('cart_items', request.user.id)


def cart_minus(request, pk):
    cart_old = Cart.objects.get(cart_id=pk)
    if cart_old.quantity == '1':
        pass
    else:
        new_quantity = int(cart_old.quantity) - 1
        new_amt = float(cart_old.amount) - float(cart_old.product.price)
        new_amt = "{:.2f}".format(new_amt)
        Cart.objects.filter(cart_id=pk).update(
            quantity=new_quantity,
            amount=new_amt,
        )
    return redirect('cart_items', request.user.id)
