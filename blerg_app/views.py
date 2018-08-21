from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import BlogPost, Comment
from datetime import datetime
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


@user_passes_test(confirm_commenter)
def delete_comment(request, pk):
	if request.method == 'GET':
		comment = get_object_or_404(Comment, pk=pk)
		Comment.objects.get(pk=pk).delete()
		title = comment.blogpost.title
		return redirect('blerg_app:visit_blerg', title=title)
		return HttpResponse(f'deleted!')


@user_passes_test(confirm_commenter)
def edit_comment(request, pk):
	if request.method == 'POST':
		updated_comment = request.POST['text_to_change']
		comment = get_object_or_404(Comment, pk=pk)
		comment.body= updated_comment
		comment.save()
		title = comment.blogpost.title
		# return HttpResponse(f'see if that worked... new comment is {updated_comment}!')
		return redirect('blerg_app:visit_blerg', title=title)


def confirm_poster(user):
	return user.groups.filter(name='Posters').exists()


@user_passes_test(confirm_poster)
def new_post(request):
	user = request.user
	timestamp = datetime.now()
	context = {"user": user, "timestamp": timestamp}
	return render(request, 'blerg_app/new_post.html', context)
	return HttpResponse(f'go to new post page')


def save_post(request):
	print("save_post")
	if request.method == 'POST':
		body = request.POST['body']
		title = request.POST['title']
		new = BlogPost(body=body, user=request.user, title=title).save()
		print(new)
		return redirect('blerg_app:visit_blerg', title=title)
