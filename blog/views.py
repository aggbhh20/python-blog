from django.shortcuts import render, HttpResponse, redirect
from .models import TodoItem
from .models import Itemblogposts
from .forms import createNewTodo
from .forms import createNewBlogpost
from .forms import Buttonform
import random
# Create your views here.
def home(request):
    i = random.randint(0,2)
    return render(request, "base.html", {"randthing": str(i)})
def fuckyou(request):
    return HttpResponse("fuck you too ")
def todos(request):
    if request.method == "POST":
        form = createNewTodo(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            b = form.cleaned_data["isDone"]
            t = TodoItem(title = n, completed=b)
            t.save()
    else:
        form = createNewTodo()
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items, "form":form})
def blogposts(request):
    if request.method == "POST":
        blogpostform = createNewBlogpost(request.POST)

        if blogpostform.is_valid():
            n = blogpostform.cleaned_data["title"]
            c = blogpostform.cleaned_data["content"]

            with open('C:\\Users\\noh\\python-blog\\blog\\id.txt') as idTxt:
                idNum = int(idTxt.read())
            idNum += 1
            with open('C:\\Users\\noh\\python-blog\\blog\\id.txt','w') as idTxt:
                idTxt.write(str(idNum))
            t = Itemblogposts(title = n, content = c, idNum = idNum)
            t.save()
    else:
        blogpostform = createNewBlogpost()
    posts = Itemblogposts.objects.all()
    return render(request, "blogposts.html", {"Itemblogpost" : posts, "blogpostform":blogpostform})
def deleteBlogpost(request):
    if request.method == "POST":
        form = Buttonform(request.POST)
        if form.is_valid():
            val = form.cleaned_data.get("btn")
            val = int(val)
            print(Itemblogposts.objects.filter(idNum=val))
            instance = Itemblogposts.objects.get(idNum=val)
            instance.delete()
            print(val)
    return redirect("blogposts")
def seeBlogposts(request):
    blogpostform = createNewBlogpost()
    posts = Itemblogposts.objects.all()
    return render(request, "seeBlogposts.html", {"Itemblogpost" : posts, "blogpostform":blogpostform})
    
        
#TODO: ADD ID TO BLOGPOSTS
