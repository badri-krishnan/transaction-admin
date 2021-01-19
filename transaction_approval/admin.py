from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponseRedirect

from .models import Transaction

from .forms import TransactionStatusForm
from django.utils.html import format_html
from django.urls import reverse, path

from django_object_actions import DjangoObjectActions

# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(DjangoObjectActions,admin.ModelAdmin):
    list_display = ('transaction_id', 'amount', 'merchant_name', 'issuing_bank', 'merchant_bank','status')
    readonly_fields = ('transaction_id','amount', 'merchant_name', 'issuing_bank', 'merchant_bank','status','authorized_count','flag_count','reject_count')

    def toolfunc(self, request, obj):
        print("Hello objs" + str(obj))
        pass
    toolfunc.label = "Review"  # optional
    toolfunc.short_description = "Review this transaction"  # optional

    change_actions = ('toolfunc',)

    def review_status(self,obj):
        print(obj)
        return
