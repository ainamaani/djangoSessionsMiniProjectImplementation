from django.shortcuts import render
from . models import Products

def Items(request):
    items = Products.objects.all()
    return render(request,'items.html',{
        'items':items
    })

def SingleItem(request,id):
    item = Products.objects.get(id=id)
    recently_viewed_products = None

    if 'recently_viewed' in request.session:
        if id in request.session['recently_viewed']:
            request.session['recently_viewed'].remove(id)

        products = Products.objects.filter(pk__in=request.session['recently_viewed'])
        recently_viewed_products = sorted(products,
            key=lambda x: request.session['recently_viewed'].index(x.id)
        )
        request.session['recently_viewed'].insert(0,id)
        if len(request.session['recently_viewed']) > 5:
            request.session['recently_viewed'].pop()

    else:
        request.session['recently_viewed'] = [id]

    request.session.modified = True

    return render(request,'item.html',{
        'item': item,
        'viewed_pdts': recently_viewed_products
    })
# Create your views here.
