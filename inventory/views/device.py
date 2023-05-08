from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import Http404
from inventory.forms import DeviceForm
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

