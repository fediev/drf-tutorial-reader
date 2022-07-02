from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

from .models import Snippet


@csrf_exempt
def snippet_list(request):
    if request.method == "GET":
        snippets = Snippet.objects.all()
        data = list(snippets.values())
        return JsonResponse(data, safe=False)

    return JsonResponse({"error": f"Not Supported Method `{request.method}`"})


@csrf_exempt
def snippet_detail(request, pk):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        data = model_to_dict(snippet)
        return JsonResponse(data, safe=False)

    return JsonResponse({"error": f"Not Supported Method `{request.method}`"})
