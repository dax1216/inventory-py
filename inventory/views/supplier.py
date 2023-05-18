from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import Http404
from inventory.forms import SupplierForm
from inventory.models import Supplier
from django.contrib.auth.decorators import login_required


@login_required
def supplier_list(request):
    suppliers = Supplier.objects.all()
    title = 'Suppliers'
    context = {'suppliers': suppliers, 'title': title}
    return render(request, 'inventory/suppliers.html', context)


@login_required
def create_supplier(request):
    form = SupplierForm()

    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid:
            form.save()
            messages.add_message(request, messages.SUCCESS, "Supplier saved.")
            return redirect('create_supplier')
        else:
            messages.add_message(request, messages.ERROR, "Error in saving entry.")

    title = 'Create Supplier'
    context = {'form': form, 'title': title}
    return render(request, 'inventory/supplier_form.html', context)


@login_required
def edit_supplier(request, sid):
    title = 'Edit Supplier'
    context = {}
    try:
        supplier = Supplier.objects.get(pk=sid)

        if request.method == 'POST':
            form = SupplierForm(request.POST, instance=supplier)
            if form.is_valid:
                form.save()
                messages.add_message(request, messages.SUCCESS, "Supplier updated.")
                return redirect('edit_supplier', supplier.id)
            else:
                messages.add_message(request, messages.ERROR, "Error in saving entry.")

        form = SupplierForm(instance=supplier)
        context = {'form': form, 'title': title}
    except Supplier.DoesNotExist:
        raise Http404("Supplier does not exist")
    return render(request, "inventory/supplier_form.html", context)


@login_required
def view_supplier(request, sid):
    title = ''
    context = {}
    try:
        supplier = Supplier.objects.get(pk=sid)
        context = {'supplier': supplier, 'title': title}
    except Supplier.DoesNotExist:
        raise Http404("Supplier does not exist")
    return render(request, "inventory/supplier.html", context)


@login_required
def delete_supplier(request, sid):
    title = 'Delete Supplier'
    context = {}
    try:
        supplier = Supplier.objects.get(pk=sid)

        if request.method == 'POST':
            supplier.delete()
            messages.add_message(request, messages.SUCCESS, "Supplier deleted.")
            return redirect('supplier_list')

        context = {'supplier': supplier, 'title': title}
    except Supplier.DoesNotExist:
        raise Http404("Supplier does not exist")
    return render(request, "inventory/supplier.html", context)
