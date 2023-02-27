from django.shortcuts import render
from .models import Customer, About, Expericence, Email, Service, Categories, Images, Testimonial, Contact, Development, Skills
from .forms import ImagesForm


def index(request):
    form = ImagesForm()
    print(request.POST)
    query = Customer.objects.all().first()
    about_model = About.objects.all().first()
    skill = Skills.objects.all()
    expericence = Expericence.objects.all()
    service = Service.objects.all()
    print(request.POST)
    image = Images.objects.all()
    category = Categories.objects.all()
    testimonial = Testimonial.objects.all()
    contact = Contact.objects.all()
    development = Development.objects.all()
    active = Development.objects.all().first()
    if 'email' in request.POST:
        a = request.POST
        b = Email()
        b.email = a['email']
        b.save()

    elif 'name' in request.POST:
        d = request.POST
        e = Contact()
        e.name = d['name']
        e.email_contact = d['email_contact']
        e.subject = d['subject']
        e.message = d['message']
        e.save()

    elif 'all' in request.POST:
        image = Images.objects.all()
    elif 'Frontend' in request.POST:
        image = Images.objects.filter(category_id__name='Frontend')
    elif 'Backend' in request.POST:
        image = Images.objects.filter(category_id__name='Backend')
    elif 'Documentation' in request.POST:
        image = Images.objects.filter(category_id__name='Documentation')

    elif 'Frontend' in request.POST:
        skill = Skills.objects.filter(development_id__name='Frontend')

    elif 'Backend' in request.POST:
        skill = Skills.objects.filter(development_id__name='Backend')

    elif 'Documentation' in request.POST:
        skill = Skills.objects.filter(development_id__name='Documentation')


    con = {
        'key': query,
        'about': about_model,
        'skill': skill,
        'expericence': expericence,
        'service': service,
        'image': image,
        'category': category,
        'testimonial': testimonial,
        'contact': contact,
        'active': active,
        'development': development,
        'form': form,
    }


    return render(request, 'index.html', context=con)

