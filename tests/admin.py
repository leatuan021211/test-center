# yourapp/admin.py
from django.contrib import admin
from .models import Test, TestQuestion


class TestQuestionInline(admin.TabularInline):
    model = TestQuestion
    extra = 1


class TestAdmin(admin.ModelAdmin):
    list_display = ("title", "duration", "category", "created_by", "created_at")
    search_fields = ("title", "description")
    list_filter = ("category", "created_by", "created_at")
    ordering = ("-created_at",)
    exclude = ("created_by",)
    inlines = [TestQuestionInline]
    list_per_page = 10

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        queryset = Test.objects.none()
        if request.user.is_staff:
            queryset = self.get_staff_queryset(request=request)

        if request.user.is_superuser:
            queryset = self.get_superuser_queryset(request=request)

        ordering = self.get_ordering(request)
        if ordering:
            queryset = queryset.order_by(*ordering)

        return queryset

    def get_staff_queryset(self, request):
        return Test.objects.filter(created_by=request.user)

    def get_superuser_queryset(self, request):
        return Test.objects.all()


class TestQuestionAdmin(admin.ModelAdmin):
    list_display = ("test", "question")
    search_fields = ("test__title", "question__text")
    list_filter = ("test",)
    list_per_page = 10

    def get_queryset(self, request):
        queryset = TestQuestion.objects.none()

        if request.user.is_staff:
            queryset = self.get_staff_queryset(request)

        if request.user.is_superuser:
            queryset = self.get_superuser_queryset(request)

        ordering = self.get_ordering(request)
        if ordering:
            queryset = queryset.order_by(*ordering)

        return queryset

    def get_staff_queryset(self, request):
        return TestQuestion.objects.filter(test__created_by=request.user)

    def get_superuser_queryset(self, request):
        return TestQuestion.objects.all()


admin.site.register(Test, TestAdmin)
admin.site.register(TestQuestion, TestQuestionAdmin)
