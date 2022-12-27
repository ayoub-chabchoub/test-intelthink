from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .models import Contact, PhoneNumber


# class based views
class ContactList(ListView):
    model = Contact


class ContactDetails(DetailView):
    model = Contact

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        queryset = PhoneNumber.objects.filter(contact=id_)
        contact = Contact.objects.get(pk=id_)
        return {"name": contact.name, "phones": [item.phone_number for item in queryset]}


# function based views
def create_contact(request):
    if request.method=='POST':
        print(request.POST)
        contact = Contact(name=request.POST['name'])
        contact.save()
        for key in request.POST:
            if key.startswith("phone"):
                phone_number = PhoneNumber(phone_number=request.POST[key], contact=contact)
                phone_number.save()
        return redirect('/contacts')
    else:
        return render(request, "phonebook/contact_create.html")
