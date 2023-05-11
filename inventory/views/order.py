from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import Http404
from inventory.forms import OrderForm, OrderItemsFormSet
from inventory.models import Order, OrderItems, OrderNotes


def order_list(request):
    orders = Order.objects.all()
    title = 'Orders'
    context = {'orders': orders, 'title': title}

    return render(request, 'inventory/order/orders.html', context)


def create_order(request):
    form = OrderForm()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid:
            form.save()
            messages.add_message(request, messages.SUCCESS, "Order saved.")
            return redirect('create_order')
        else:
            messages.add_message(request, messages.ERROR, "Error in saving entry.")

    title = 'Create Order'
    context = {'form': form, 'title': title}
    return render(request, 'inventory/order/order_form.html', context)


def edit_order(request, did=None):
    title = 'Edit Device'
    context = {}
    try:
        device = Device.objects.get(pk=did)
        form = DeviceForm(request.POST or None, instance=device)
        formset = DeviceMetaFormSet(request.POST or None, queryset=DeviceMeta.objects.filter(device=device))

        if request.method == 'POST':
            if request.POST.get('form-TOTAL_FORMS') is None:
                if form.is_valid:
                    form.save()
                    messages.add_message(request, messages.SUCCESS, "Device updated.")
                    return redirect('edit_device', device.id)
                else:
                    messages.add_message(request, messages.ERROR, "Error in saving entry.")
            else:
                if formset.is_valid:
                    instances = formset.save(commit=False)

                    for instance in instances:
                        instance.device = device
                        instance.save()

                    for deleted_item in formset.deleted_objects:
                        deleted_item.delete()

                    messages.add_message(request, messages.SUCCESS, "Device meta updated.")
                    return redirect('edit_device', device.id)
                else:
                    messages.add_message(request, messages.ERROR, "Error in saving entry.")

        context = {'form': form, 'formset': formset, 'device': device, 'title': title}
    except Device.DoesNotExist:
        raise Http404("Device does not exist")
    return render(request, "inventory/device/device_form.html", context)


