from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import forms
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import BadHeaderError, send_mail


class IndexView(TemplateView):
    template_name = 'index.html'


def index(request):
    return render(request, 'index.html')


def contents(request):
    return render(request, 'contents.html')


def contact(request):
    return render(request, 'contact.html')


""" 送信完了画面"""


def comp(request):
    return render(request, 'comp.html')


class FormView(TemplateView):

    # 初期変数定義
    def __init__(self):
        self.params = {"Message": "情報を入力してください。",
                       "form": forms.Contact_Form(),
                       }

    # GET時の処理を記載
    def get(self, request):
        return render(request, "contact_form.html", context=self.params)

    # POST時の処理を記載
    def post(self, request):
        if request.method == "POST":
            self.params["form"] = forms.Contact_Form(request.POST)

            # フォーム入力が有効な場合
            if self.params["form"].is_valid():
                subject = self.params["form"].cleaned_data['subject']
                name = self.params["form"].cleaned_data['name']
                tell = self.params["form"].cleaned_data['tell']
                message = self.params["form"].cleaned_data['message']
                sender = self.params["form"].cleaned_data['sender']
                myself = self.params["form"].cleaned_data['myself']
                recipients = [settings.EMAIL_HOST_USER]
                bcc = recipients

                message = name + " 様\n\n" + "電話番号：" + tell + "\n\n" + "お問い合わせの内容\n\n" + message

                if myself:
                    recipients.clear()
                    recipients.append(sender)

                try:
                    send_mail(subject, message, sender, recipients, bcc)
                except BadHeaderError:
                    return HttpResponse('無効なヘッダーが見つかりました。')

            # 入力項目をデータベースに保存
            self.params["form"].save(commit=True)
            self.params["Message"] = "入力情報が送信されました。"

            return render(request, "comp.html", context=self.params)


""" お問い合わせフォーム画面"""


""" def contact_form(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        form_db = People(request.POST)

        if form.is_valid():
            form_db.save()

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

    return render(request, 'contact_form.html', {'form': form}) """
