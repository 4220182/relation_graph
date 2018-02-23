from django.shortcuts import render
from django.http import HttpResponse
import pygraphviz as gv
        
        
def pic(request):
    return render(request, 'pic.html')
           
            
def getpic(request):
    try :
        content = request.GET.get('content')
        print (content)
        g=gv.AGraph(content)
        g.layout('dot')
        png=g.draw(format='png') # draw png
        return HttpResponse(png, content_type='image/png')
    except gv.agraph.DotError :
        return None
    else :
        return None
    
        
        