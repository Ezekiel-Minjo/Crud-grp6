from django.shortcuts import render, redirect, get_object_or_404    
from .models import Item
from .forms import ItemForm

# Create your views here.

# read list all items
def item_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

# create a new item
def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('itemList')
    else:
        form = ItemForm()
    return render(request, 'form.html', {'form': form})

# update an existing item
def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('itemList')
    else:
        form = ItemForm(instance=item)
    return render(request, 'form.html', {'form': form})

# delete an item
def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('itemList')
    return render(request, 'delete.html', {'item': item})

# end of views.py 