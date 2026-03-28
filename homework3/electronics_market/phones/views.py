from django.shortcuts import render, redirect
from django.views import View
from .models import Phones
from .forms import PhonesForm
from django.shortcuts import get_object_or_404

class PhonesListView(View):
    def get(self, request):
        phones = Phones.objects.all()
        return render(request, 'phones_list.html', {'phones': phones})


class PhoneCreateView(View):
    def get(self, request):
        form = PhonesForm()
        return render(request, 'phone_form.html', {'form': form})

    def post(self, request):
        form = PhonesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('phones_list')
        return render(request, 'phone_form.html', {'form': form})
    
class PhoneDetailView(View):
    def get(self, request, pk):
        phone = get_object_or_404(Phones, pk=pk)
        return render(request, 'phone_detail.html', {'phone': phone})


class PhoneUpdateView(View):
    def get(self, request, pk):
        phone = get_object_or_404(Phones, pk=pk)
        form = PhonesForm(instance=phone)
        return render(request, 'phone_form.html', {'form': form})

    def post(self, request, pk):
        phone = get_object_or_404(Phones, pk=pk)
        form = PhonesForm(request.POST, instance=phone)
        if form.is_valid():
            form.save()
            return redirect('phones_list')
        return render(request, 'phone_form.html', {'form': form})


class PhoneDeleteView(View):
    def get(self, request, pk):
        phone = get_object_or_404(Phones, pk=pk)
        return render(request, 'phone_delete.html', {'phone': phone})

    def post(self, request, pk):
        phone = get_object_or_404(Phones, pk=pk)
        phone.delete()
        return redirect('phones_list')