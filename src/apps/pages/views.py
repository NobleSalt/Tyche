from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class Home(View):
    template_name = 'index.html'

    def get(self, *args, **kwargs):
        print(f"Referer: {self.request.headers.get('Referer')}")
        print(f"User-Agent: {self.request.headers.get('User-Agent')}")

        return render(self.request, self.template_name)


class About(View):
    template_name = 'about.html'

    def get(self, *args, **kwargs):
        print(f"Referer: {self.request.headers.get('Referer')}")
        print(f"User-Agent: {self.request.headers.get('User-Agent')}")

        return render(self.request, self.template_name)


class Contact(View):
    template_name = 'contact.html'


    def get(self, *args, **kwargs):
        print(f"Referer: {self.request.headers.get('Referer')}")
        print(f"User-Agent: {self.request.headers.get('User-Agent')}")

        return render(self.request, self.template_name)


class Menu(View):
    template_name = 'menu.html'

    def get(self, *args, **kwargs):
        print(f"Referer: {self.request.headers.get('Referer')}")
        print(f"User-Agent: {self.request.headers.get('User-Agent')}")

        return render(self.request, self.template_name)


class Blog(View):
    template_name = 'blog.html'

    def get(self, *args, **kwargs):
        print(f"Referer: {self.request.headers.get('Referer')}")
        print(f"User-Agent: {self.request.headers.get('User-Agent')}")

        return render(self.request, self.template_name)


# class BlogDetail(View):
#     template_name = 'blog_details.html'

#     def get(self, *args, **kwargs):
#         print(f"Referer: {self.request.headers.get('Referer')}")
#         print(f"User-Agent: {self.request.headers.get('User-Agent')}")

#         return render(self.request, self.template_name)
