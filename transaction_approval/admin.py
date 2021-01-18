from django.conf.urls import url
from django.contrib import admin
from .models import Transaction
from django.utils.html import format_html
from django.urls import reverse

# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'amount', 'merchant_name', 'issuing_bank', 'merchant_bank')
    readonly_fields = ('transaction_id','amount', 'merchant_name', 'issuing_bank', 'merchant_bank','authorized_count','flag_count','reject_count')


    def approval_actions(self,obj):
        #Todo
        return

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            url(
                r'^(?P<transaction_id>.+)/status/$',
                self.admin_site.admin_view(self.process_status),
                name='transaction-status',
            ),
        ]
        return custom_urls + urls


    def process_status(self, request, transaction_id, *args, **kwargs):
        transaction_object = self.get_object(request, transaction_id)
        print(request.method)
        print(transaction_object)
