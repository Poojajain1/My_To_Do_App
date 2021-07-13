from pdb import set_trace
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDOItem
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def home(request):
    all_todo_items=ToDOItem.objects.all()
    return render(request, 'home.html', {'all_items':all_todo_items})

@csrf_exempt
def addToDo(request):
    print(request.body)
    content=request.POST['content']
    #content = request.POST.get('content', False)
    # content=request.POST.get('content')
    new_item=ToDOItem(content=content)
    new_item.save()
    return HttpResponseRedirect('/app_ToDo/')
    
@csrf_exempt
def deleteTodo(request,todo_id):
    item_to_delete=ToDOItem.objects.get(id=todo_id)
    print(request.body)
    item_to_delete.delete()    
    return HttpResponseRedirect('/app_ToDo/')    


    

    #create a new todo all_iteam
    #save
    #redirect the browser to'/todo/'