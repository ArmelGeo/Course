from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import CoursesForm
from .models import Courses

# # Create your views here.
# def index(request):
#     courses = Course.all()
#     return render(request, 'catalog/courses_form.html', {"courses": courses})




def courses_list(request):
    courses = Courses.objects.all()

    return render(request, 'courseList/courses_list.html', { 'object_list' : courses})


def courses_detail(request, id):
    courses = Courses.objects.get(id)
    return render(request, 'courseList/courses_detail.html', {'courses': courses})


def courses_create(request, template_name = 'courseList/courses_form.html'): 
    form = CoursesForm(request.POST or None)
    if form.is_valid:
        form.save()
        return redirect('courseListe:course_list')
    return render (request, template_name, {'form' : form })



    # # form = CoursesForm(request.POST or None)  
    # if request.method == "POST":
    #     course= Courses()
    #     course.title = request.POST.get("title")
    #     course.body = request.POST.get("body")
    # # if form.is_valid(): 
    # #     course = form.save(commit=False)  
    # #     course.save()  
    # #     return redirect('courseList/courses_list.html')  
    # success_url = reverse_lazy('courseList: courses_list')
    # #return render(request, 'coursesList/courses_form.html', {'form': form})  
    # return render (request, 'courseList/courses_create_form.html')
  
  
  
def courses_edit(request, pk=id):   
    # form = CoursesForm(request.POST or None, instance=courses)  
    # if form.is_valid():  
    #    form.save()  
    #    return redirect('courseList/courses_list.html') 
    context = {}
    context ['courses'] = get_object_or_404(Courses, pk=id) 
    course = get_object_or_404(Courses, pk=id)
    return render(request, 'courseList/courses_form.html', {'course': course})  
  
  
  
def courses_delete(request, pk=id):   
    if request.method == 'POST':  
        courses.delete()  
        return redirect('coursesList/courses_list')  
    return render(request, 'coursesList/confirm_delete.html', {'object': courses})

# from django.views.generic import ListView  
# from django.views.generic.edit import CreateView, UpdateView, DeleteView  
# from django.urls import reverse_lazy  
       
# from .models import Courses  
       
       
# class CoursesList(ListView):  
#     model = Courses  
       
       
#     class CoursesCreate(CreateView):  
#         model = Courses  
#         fields = ['title', 'body', 'startDate', 'endDate']  
#         template_name_suffix = '_create_form.html'
#     #success_url = reverse_lazy('courseList: courses_list')  
    
 
       
       
# class CoursesUpdate(UpdateView):  
#     model = Courses  
#     fields = ['title', 'body', 'startDate', 'endDate']  
#     success_url = reverse_lazy('courseList: courses_list') 
#     template_name_suffix = '_edit_form.html' 
       
       
# class CoursesDelete(DeleteView):  
#     model = Courses  
#     success_url = reverse_lazy('courses_list')  