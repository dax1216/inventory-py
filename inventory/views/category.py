from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import Http404
from inventory.forms import CategoryForm
from inventory.models import Category


def category_list(request):
    categories = Category.objects.all()
    title = 'Categories'
    context = {'categories': categories, 'title': title}
    return render(request, 'inventory/category/categories.html', context)


def create_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid:
            form.save()
            messages.add_message(request, messages.SUCCESS, "Category saved.")
            return redirect('create_category')
        else:
            messages.add_message(request, messages.ERROR, "Error in saving entry.")

    title = 'Create Category'
    context = {'form': form, 'title': title}
    return render(request, 'inventory/category/category_form.html', context)


def edit_category(request, cid):
    title = 'Edit Category'
    context = {}
    try:
        category = Category.objects.get(pk=cid)

        if request.method == 'POST':
            form = CategoryForm(request.POST, instance=category)
            if form.is_valid:
                form.save()
                messages.add_message(request, messages.SUCCESS, "Category updated.")
                return redirect('edit_category', category.id)
            else:
                messages.add_message(request, messages.ERROR, "Error in saving entry.")

        form = CategoryForm(instance=category)
        context = {'form': form, 'title': title}
    except Category.DoesNotExist:
        raise Http404("Category does not exist")
    return render(request, "inventory/category/category_form.html", context)


def view_category(request, cid):
    title = ''
    context = {}
    try:
        category = Category.objects.get(pk=cid)
        context = {'category': category, 'title': title}
    except Category.DoesNotExist:
        raise Http404("Category does not exist")
    return render(request, "inventory/category/category.html", context)


def delete_category(request, cid):
    title = 'Delete Category'
    context = {}
    try:
        category = Category.objects.get(pk=cid)

        if request.method == 'POST':
            category.delete()
            messages.add_message(request, messages.SUCCESS, "Category deleted.")
            return redirect('category_list')

        context = {'category': category, 'title': title}
    except Category.DoesNotExist:
        raise Http404("Category does not exist")
    return render(request, "inventory/category/category.html", context)
