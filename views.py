from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

#disabling csrf (cross site request forgery)
@csrf_exempt
def index(request):

    if request.method == 'POST':
            #getting values from post
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

#adding the values in a context variable 
        context = {
            'name': name,
            'email': email,
            'phone': phone
        }

        template = loader.get_template('showdata.html')

        return HttpResponse(template.render(context, request))
    else:

        template = loader.get_template('index.html')
        return HttpResponse(template.render())