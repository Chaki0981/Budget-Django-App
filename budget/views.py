from django.shortcuts import render
from django.views import View

# Create your views here.

class StartingPageView(View):
    template_name = 'budget/starting-page.html'
    def get(self, request):
        return render(request, self.template_name)