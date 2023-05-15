from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import Http404
from django.core.paginator import Paginator
from inventory.forms import OrderForm, OrderItemsFormSet
from inventory.models import Order, OrderItems, OrderNotes


def order_list(request):
    orders = Order.objects.all()
    paginator = Paginator(orders, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    title = 'Orders'
    context = {'orders': orders, 'title': title, 'page_obj': page_obj}

    return render(request, 'inventory/order/orders.html', context)


def create_order(request):
    form = OrderForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.issued_by = request.user
            instance.save()
            messages.add_message(request, messages.SUCCESS, "Order saved.")
            return redirect('create_order')
        else:
            messages.add_message(request, messages.ERROR, "Error in saving entry.")

    title = 'Create Order'
    context = {'form': form, 'title': title}
    return render(request, 'inventory/order/order_form.html', context)


def edit_order(request, oid=None):
    title = 'Edit Order'
    context = {}
    try:
        order = Order.objects.get(pk=oid)
        form = OrderForm(request.POST or None, instance=order)
        formset = OrderItemsFormSet(request.POST or None, queryset=OrderItems.objects.filter(order=order))

        if request.method == 'POST':
            if request.POST.get('form-TOTAL_FORMS') is None:
                if form.is_valid:
                    form.save()
                    messages.add_message(request, messages.SUCCESS, "Order updated.")
                    return redirect('edit_order', order.id)
                else:
                    messages.add_message(request, messages.ERROR, "Error in saving entry.")
            else:
                if formset.is_valid:
                    instances = formset.save(commit=False)

                    for instance in instances:
                        instance.order = order
                        instance.save()

                    for deleted_item in formset.deleted_objects:
                        deleted_item.delete()

                    messages.add_message(request, messages.SUCCESS, "Order Items updated.")
                    return redirect('edit_order', order.id)
                else:
                    messages.add_message(request, messages.ERROR, "Error in saving entry.")

        context = {'form': form, 'formset': formset, 'order': order, 'title': title}
    except Device.DoesNotExist:
        raise Http404("Order does not exist")
    return render(request, "inventory/order/order_form.html", context)


