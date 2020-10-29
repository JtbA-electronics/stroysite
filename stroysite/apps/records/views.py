from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import RecordForm


def main(request):
	return render (request, 'records/main.html',{})

def services(request):
	return render (request, 'records/services.html',{})

def vacancy(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request,'records/vacancy.html',{'posts':posts})

def record_detail(request,pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'records/record_detail.html', {'post':post})

def record_new(request):
	if request.method == "POST":
		form = RecordForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('record_detail', pk=post.pk)
	else:
		form = RecordForm()
	return render(request, 'records/record_edit.html', {'form': form})

def record_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = RecordForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('record_detail', pk=post.pk)
	else:
		form =RecordForm(instance=post)
	return render(request, 'records/record_edit.html', {'form':form})

def contacts(request):
	return render (request, 'records/contacts.html',{})

def documents(request):
	return render (request, 'records/documents.html',{})
	
