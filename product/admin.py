from django.contrib import admin

from apitest.models import Apis
from apptest.models import AppCase
from product.models import Product


class ApisAdmin(admin.TabularInline):
    list_display = ["api_name", "api_url", "api_param_value", "api_method",
                    "api_result", "api_status", "create_time", "id", "product"]

    model = Apis
    extra = 1


class AppCaseAdmin(admin.TabularInline):
    list_display = ["app_case_name", "app_test_result", "create_time", "product"]
    model = AppCase
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_name", "product_desc", "product_owner", "create_time", "id"]
    inlines = [ApisAdmin, AppCaseAdmin]


admin.site.register(Product)