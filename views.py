from django.http import JsonResponse
from .tasks import enviar_email_usuario

def enviar_email(request):

    enviar_email_usuario.apply_async(
        args=[1],
        countdown=30  # executa após 30 segundos
    )

    return JsonResponse({"mensagem": "Tarefa agendada para 30 segundos"})