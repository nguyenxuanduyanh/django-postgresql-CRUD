from .models import Post
from django.http import HttpResponse
import json


# Create your views here.
def ViewAllPosts(request):
    # Paging
    current_page = int(request.GET.get('pageNumber', 1))
    if current_page > 0:
        current_page -= 1

    off_set = current_page * int(request.GET.get('itemPerPage', 2))

    all_post = Post.objects.all()[off_set:int(request.GET.get('itemPerPage', 2)) + off_set]
    return HttpResponse(all_post)


def ViewPost(request, id):
    try:
        seletected_post = Post.objects.get(id=id)
    except:
        return HttpResponse(status=404, content="Post Not Found")

    return HttpResponse(seletected_post)


def AddPost(request):
    if request.method == 'POST':
        save_post = Post()
        if json.loads(request.body)['title']:
            save_post.title = json.loads(request.body)['title']
        if json.loads(request.body)['author_id']:
            try:
                save_post.author_id = json.loads(request.body)['author_id']
                save_post.save()
                print(save_post)
            except:
                return HttpResponse("Author doesn't exist")
        return HttpResponse("create post successfully: {}".format(save_post))


def UpdatePost(request, id):
    if request.method == 'PUT':
        try:
            selected_post = Post.objects.get(id=id)
        except:
            return HttpResponse(status=404, content="Post Not Found")
        if selected_post:
            if json.loads(request.body)['title']:
                selected_post.title = json.loads(request.body)['title']
            try:
                if json.loads(request.body)['author_id']:
                    selected_post.author_id = json.loads(request.body)['author_id']
                    selected_post.save()
            except:
                return HttpResponse("Author doesn't exist")
            return HttpResponse("create post successfully: {}".format(selected_post))


def DeletePost(request, id):
    if request.method == 'DELETE':
        try:
            selected_post = Post.objects.get(id=id)
        except:
            return HttpResponse(status=404, content="Post Not Found")
        if selected_post:
            selected_post.delete()

            return HttpResponse("delete post successfully: {}".format(selected_post))
