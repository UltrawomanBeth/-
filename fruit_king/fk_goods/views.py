#encoding=utf-8
from django.shortcuts import render

# Create your views here.
def index(request):
    context={'title': '首页', 'cart_show': '1'}
    return render(request, 'fk_goods/index.html', context)






# def index(request):
#     goods_list=[]#[{},{},{}]===>{'typeinfo':,'new_list':,'click_list':}
#     #查询分类对象
#     #查询每个分类中最新的4个商品
#     #查询每个分类中最火的4个商品
#     type_list=TypeInfo.objects.all()
#     for t1 in type_list:
#         nlist=t1.goodsinfo_set.order_by('-id')[0:4]
#         clist=t1.goodsinfo_set.order_by('-gclick')[0:4]
#         goods_list.append({'t1':t1,'nlist':nlist,'clist':clist})
#     context={'title':'首页','glist':goods_list}
#     return render(request,'ttsx_goods/index.html',context)




