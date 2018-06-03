from django.shortcuts import render

from django_web.models import ArtInfo #导入数据库model中的类

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger #分页，注意（EmptyPage, PageNotAnInteger）不要忘记添加了
# Create your views here.
def index(request):
    limit= 10
    arti_info = ArtInfo.objects.all()
    paginator = Paginator(arti_info,limit)
    page = request.GET.get('page')  #获取request（也就是URL）中的页码

    try:
        loaded = paginator.page(page)   #获取对应页码的数据
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        loaded = paginator.page(1)  # 获取首页的数据
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results
        loaded = paginator.page(ArtInfo.paginator.num_pages)  # 获取末尾页的数据

    context = {
        'ArtInfo': loaded,
    }
    # print(arti_info[0].key)
    # print(arti_info[0].title)
    # print(arti_info[0].link)

    return render(request,'index.html',context)