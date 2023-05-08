from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import Http404
from inventory.forms import BrandForm
from inventory.models import Brand

def brand_list(request):
    brands = Brand.objects.all()
    title = 'Brands'
    context = {'brands': brands, 'title': title}

    return render(request, 'inventory/brand/brands.html', context)


def create_brand(request):
    form = BrandForm()

    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid:
            form.save()
            messages.add_message(request, messages.SUCCESS, "Brand saved.")
            return redirect('create_brand')
        else:
            messages.add_message(request, messages.ERROR, "Error in saving entry.")

    title = 'Create Brand'
    context = {'form': form, 'title': title}
    return render(request, 'inventory/brand/brand_form.html', context)


def edit_brand(request, bid):
    title = 'Edit Brand'
    context = {}
    try:
        brand = Brand.objects.get(pk=bid)

        if request.method == 'POST':
            form = BrandForm(request.POST, instance=brand)
            if form.is_valid:
                form.save()
                messages.add_message(request, messages.SUCCESS, "Brand updated.")
                return redirect('edit_brand', brand.id)
            else:
                messages.add_message(request, messages.ERROR, "Error in saving entry.")

        form = BrandForm(instance=brand)
        context = {'form': form, 'title': title}
    except Brand.DoesNotExist:
        raise Http404("Brand does not exist")
    return render(request, "inventory/brand/brand_form.html", context)


def view_brand(request, bid):
    title = ''
    context = {}
    try:
        brand = Brand.objects.get(pk=bid)
        context = {'brand': brand, 'title': title}
    except Brand.DoesNotExist:
        raise Http404("Brand does not exist")
    return render(request, "inventory/brand/brand.html", context)


def delete_brand(request, bid):
    title = 'Delete Brand'
    context = {}
    try:
        brand = Brand.objects.get(pk=bid)

        if request.method == 'POST':
            brand.delete()
            messages.add_message(request, messages.SUCCESS, "Brand deleted.")
            return redirect('brand_list')

        context = {'brand': brand, 'title': title}
    except Brand.DoesNotExist:
        raise Http404("Brand does not exist")
    return render(request, "inventory/brand/brand.html", context)
