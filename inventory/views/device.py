from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import Http404
from inventory.forms import DeviceForm, DeviceMetaFormSet
from inventory.models import Device, DeviceMeta

def device_list(request):
    devices = Device.objects.all()
    title = 'Devices'
    context = {'devices': devices, 'title': title}

    return render(request, 'inventory/device/devices.html', context)


def create_device(request):
    form = DeviceForm()

    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid:
            form.save()
            messages.add_message(request, messages.SUCCESS, "Device saved.")
            return redirect('create_device')
        else:
            messages.add_message(request, messages.ERROR, "Error in saving entry.")

    title = 'Create Device'
    context = {'form': form, 'title': title}
    return render(request, 'inventory/device/device_form.html', context)


def edit_device(request, did=None):
    title = 'Edit Device'
    context = {}
    try:
        device = Device.objects.get(pk=did)
        form = DeviceForm(request.POST or None, instance=device)
        formset = DeviceMetaFormSet(queryset=DeviceMeta.objects.filter(device=device))
        print(formset)
        
        if request.method == 'POST':
            if form.is_valid:
                form.save()
                messages.add_message(request, messages.SUCCESS, "Category updated.")
                return redirect('edit_category', category.id)
            else:
                messages.add_message(request, messages.ERROR, "Error in saving entry.")

        context = {'form': form, 'formset': formset, 'title': title}
    except Device.DoesNotExist:
        raise Http404("Device does not exist")
    return render(request, "inventory/device/device_form.html", context)

