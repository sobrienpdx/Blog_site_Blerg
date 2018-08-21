from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import BlogPost, Comment
from datetime import datetime
from datetime import timedelta
from django.contrib.auth.decorators import user_passes_test


def index(request):
	blog_list = BlogPost.objects.all()
	context = {'blog_list': blog_list}
	return render(request, 'blerg_app/index.html', context)


def search_blerg(request):
	if request.method == 'GET':
		print("you called search_book")
		search_query = request.GET['search_box']
		searched_blogs = []
		bodies = Book.objects.filter(body__icontains=search_query)
		titles =Book.objects.filter(title__icontains=search_query)
		comments = Book.objects.filter(comments__body__icontains=search_query)
		searched_blogs.extend(bodies.union(titles, comments))
		# searched_book.append(Book.objects.filter(author=search_query))
		context = {'blog_list': searched_blogs}
		return render(request, 'blog_app/index.html', context)


def visit_blerg(request, title):
	title_to_view = get_object_or_404(BlogPost, title=title)
	comments = Comment.objects.filter(blogpost__title=title)
	print(title_to_view)
	print(comments)
	# return HttpResponse("You went to a blog")
	context = {'title_to_view': title_to_view, 'comments': comments}
	return render(request, 'blerg_app/detail.html', context)


def confirm_commenter(user):
	print(user.groups.filter(name='Commenters').exists())
	return user.groups.filter(name='Commenters').exists()


@user_passes_test(confirm_commenter)
def comment(request, pk):
	if request.method == 'POST':
		new_comment = request.POST['new_comment']
		blogpost = get_object_or_404(BlogPost, pk=pk)
		Comment(body=new_comment, user=request.user, blogpost=blogpost).save()
		title = blogpost.title
		print(title)
		return redirect('blerg_app:visit_blerg', title=title)
		return HttpResponse(f'you called the comment function for {new_comment}')
