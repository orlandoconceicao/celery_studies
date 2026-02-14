from celery import shared_task
import time

from celery import shared_task
import requests

@shared_task(bind=True, max_retries=3)
def enviar_email_usuario(self, usuario_id):
    try:
        print(f"Processando usuário {usuario_id}")

        # Simulação de chamada externa
        resposta = requests.get("https://httpbin.org/get")

        return {
            "status": "sucesso",
            "usuario": usuario_id
        }

    except Exception as e:
        raise self.retry(exc=e, countdown=5)