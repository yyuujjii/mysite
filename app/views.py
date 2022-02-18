from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .form import ContactForm
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail


class IndexView(TemplateView):
    template_name = 'app/index.html'


def index(request):
    return render(request, 'index.html')


def contents(request):
    return render(request, 'contents.html')


def contact(request):
    return render(request, 'contact.html')


""" 送信完了画面"""


def comp(request):
    return render(request, 'comp.html')


""" お問い合わせフォーム画面"""


def contact_form(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():

            subject = form.cleaned_data['subject']
            name = form.cleaned_data['name']
            tell = form.cleaned_data['tell']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            myself = form.cleaned_data['myself']
            recipients = [settings.EMAIL_HOST_USER]

            message = name + " 様\n\n" + "電話番号：" + tell + "\n\n" + "お問い合わせの内容\n\n" + message

            if myself:
                recipients.append(sender)
            try:
                send_mail(subject, message, sender, recipients)
            except BadHeaderError:
                return HttpResponse('無効なヘッダーが見つかりました。')

            return redirect('comp')

    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form})
