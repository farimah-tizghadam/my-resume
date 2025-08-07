from django.shortcuts import render


context = {
    'name' : 'Farimah',
    'surname' : 'Tizghadam',
    'email' : 'farimahtizghadam@gmail.com',
    'phone' : '(+98)9106797104',
    'Location' : 'Tehran, iran',
}
 
def index_view(request):
    return render(request, 'website/index.html', context)