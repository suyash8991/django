from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import job
# Create your views here.
class joblist(ListView):
    model=job
    paginate_by = 10
    queryset = job.objects.all()
class jobdetail(DetailView):
    context_object_name='job_detail'
    model=job
    template_name='job/jobdetail.html'
def check(request):
    if request.method=='POST':
        search=request.POST.get('Search')
        print(search)
        jobs=job.objects.order_by('company_name')
            #print(str(j.job_description))
        k= job.objects.filter(job_description__contains=search)
        for j in k:
            j.search_count=j.search_count+1
            j.save()
        return render (request,'job/search.html',{'search':k})

                #print(j)
    else:
        pass
    return render(request,'main.html')
def trending(request):
    k=job.objects.all().order_by('-search_count')[:10]
    return render(request,'job/trending.html',{'trend':k})
