from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Dept, Mat, Course, CourseReview, AdminMessage
from .forms import RecomForm, MessageForm
from django.contrib.admin.views.decorators import staff_member_required
from django.template.loader import render_to_string
from django.http import JsonResponse
import datetime


def dept(request):
    depts = Dept.objects.order_by('name')
    context = {'dept_list':depts}
    return (context)


def mat_list(request, dept_id):
    mats_no = Mat.objects.filter(dep = dept_id)
    mats = mats_no.order_by('id')
    depto = Dept.objects.get(id = dept_id)
    return render(request,'reviews/mat_list.html',{'mat_list':mats,'depto':depto})


def search(request):
    ctx = {}
    url_parameter = request.GET.get("q")
    if url_parameter and len(url_parameter) > 2:
        cate = Course.objects.filter(name__icontains=url_parameter)
    else:
        cate = []

    ctx["cate"] = cate

    if request.is_ajax():
        html = render_to_string(template_name="reviews/partial-res.html", context={"cate": cate})
        data_dict = {"html_from_view": html}
        return JsonResponse(data=data_dict, safe=False)

    return render(request, "reviews/index.html", context=ctx)


def index_view(request):
    val1=search(request)
    val2=dept(request)
    ctx={'v1':val1,'v2':val2}
    return render(request,"reviews/index.html",context = ctx)


def course_list(request, mat_id):
    courses_no = Course.objects.filter(mat = mat_id)
    courses = courses_no.order_by('name')
    materia = Mat.objects.get(id = mat_id)
    context = {'course_list':courses, 'materia':materia}
    return render(request,'reviews/course_list.html',context)


def course_detail(request, mat_id, course_id):
    course_no = get_object_or_404(Course, pk=course_id)
    course_rev = CourseReview.objects.filter(course=course_id).order_by('-year','-cuatr')
    pagin = Paginator(course_rev,5)
    form = RecomForm()
    page_number = request.GET.get('page')
    try:
        revs = pagin.page(page_number)
    except PageNotAnInteger:
        revs = pagin.page(1)
    except EmptyPage:
        revs = pagin.page(pagin.num_pages)


    return render(request, 'reviews/course_detail.html', {'course': course_no, 'form': form, 'listado':revs})



def add_recom(request, course_id, mat_id):
    course = get_object_or_404(Course, pk=course_id)
    mat = get_object_or_404(Mat, pk=course.mat.id)
    form = RecomForm(request.POST)
    if form.is_valid():
        recom = form.cleaned_data['recom']
        comment = form.cleaned_data['comment']
        cuatr = form.cleaned_data['cuatr']
        year = form.cleaned_data['year']
        CReview = CourseReview()
        CReview.course = course
        CReview.recom = recom
        CReview.cuatr = cuatr
        CReview.year = year
        CReview.comment = comment
        CReview.save()
        return HttpResponseRedirect(reverse('reviews:course_detail',args=(mat.id,course.id,)))

    return render(request, 'reviews/course_detail.html', {'course':course, 'form':form})



def flag_rev(request,rev_id):
    r = CourseReview.objects.filter(id=rev_id).update(flag = -1)
    print("flagging rev:"+rev_id)
    return HttpResponse(status=204)



def del_rev(request, rev_id):
    # TODO: SQL delete
    print(type(rev_id))
    print("deleting"+rev_id)
    return HttpResponse(status=204)



def contacto(request):
    form = MessageForm()
    return render(request,'reviews/contacto.html',{'form':form})



def send_msg(request):
    form = MessageForm(request.POST)
    if form.is_valid():
        mensaje = form.cleaned_data['mensaje']
        sendM = AdminMessage()
        sendM.mensaje = mensaje
        sendM.date = datetime.datetime.now()
        sendM.save()
        return HttpResponseRedirect(reverse('reviews:contacto'))
    return render(request, 'reviews/contacto.html',{'form':form})
