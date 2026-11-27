from datetime import timedelta
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Pessoa

class PessoaTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user("operador", password="teste-123456")
        self.client.force_login(self.user)

    def grant(self, *actions):
        self.user.user_permissions.add(*Permission.objects.filter(content_type__app_label="pessoas", codename__in=[f"{a}_pessoa" for a in actions]))

    def test_anonymous_redirect(self):
        self.client.logout()
        self.assertEqual(self.client.get(reverse("pessoas:list")).status_code, 302)

    def test_without_permission(self):
        self.assertEqual(self.client.get(reverse("pessoas:list")).status_code, 403)
        self.assertEqual(self.client.post(reverse("pessoas:create"), {"nome": "Teste"}).status_code, 403)

    def test_create_and_search(self):
        self.grant("add", "view")
        self.assertRedirects(self.client.post(reverse("pessoas:create"), {"nome": "Maria Exemplo", "email": "m@example.com"}), reverse("pessoas:list"))
        self.assertTrue(Pessoa.objects.filter(nome="Maria Exemplo").exists())
        self.assertContains(self.client.get(reverse("pessoas:list"), {"q": "Maria"}), "Maria Exemplo")
        self.assertNotContains(self.client.get(reverse("pessoas:list"), {"q": "Outro"}), "Maria Exemplo")

    def test_edit_and_status(self):
        self.grant("view", "change")
        p = Pessoa.objects.create(nome="Antes")
        self.assertRedirects(self.client.post(reverse("pessoas:update", args=[p.pk]), {"nome": "Depois"}), reverse("pessoas:list"))
        p.refresh_from_db()
        self.assertEqual(p.nome, "Depois")
        url = reverse("pessoas:status", args=[p.pk])
        self.assertEqual(self.client.get(url).status_code, 405)
        self.assertRedirects(self.client.post(url, {"acao": "inativar"}), reverse("pessoas:list"))
        p.refresh_from_db()
        self.assertFalse(p.ativo)
        self.assertNotContains(self.client.get(reverse("pessoas:list"), {"status": "ativos"}), "Depois")
        self.client.post(url, {"acao": "ativar"})
        p.refresh_from_db()
        self.assertTrue(p.ativo)

    def test_view_only_cannot_write(self):
        self.grant("view")
        p = Pessoa.objects.create(nome="Exemplo")
        self.assertEqual(self.client.post(reverse("pessoas:update", args=[p.pk]), {"nome": "Alterado"}).status_code, 403)
        self.assertEqual(self.client.post(reverse("pessoas:status", args=[p.pk]), {"acao": "inativar"}).status_code, 403)

    def test_future_birth_date(self):
        self.grant("add", "view")
        response = self.client.post(reverse("pessoas:create"), {"nome": "Teste", "data_nascimento": (timezone.localdate()+timedelta(days=1)).isoformat()})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Pessoa.objects.exists())
