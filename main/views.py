from django.shortcuts import render, redirect
from .models import Work, Message, Review

# Create your views here.
def index(request):
    title = "Ephraim"
    context = {'title':title}
    return render(request, 'index.html', context)

def contact(request):
    title = "Contact Me"

    if request.method == 'POST':
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        message = Message.objects.create(email=email, subject=subject, message=message)
        message.save()

        return redirect('index')


    context = {"title":title}
    return render(request, 'contact.html', context)

def about(request):
    title = "About Me"
    context = {"title":title}
    return render(request, 'about.html', context)

def works(request):
    title = "Works"
    works = Work.objects.all()
    work_groups = [works[i:i + 3] for i in range(0, len(works), 3)]
    work_count = works.count()
    context = {"title":title, "work_groups":work_groups, "work_count":work_count}
    return render(request, 'works.html', context)

def work(request, pk):
    title = "Work"
    work = Work.objects.get(id=pk)
    review = Review.objects.get(work=work)
    context = {"title":title, "work":work, "review":review}
    return render(request, 'work.html', context)