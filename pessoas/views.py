from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import ListView, CreateView, UpdateView
from .forms import PessoaForm
from .models import Pessoa

class PessoaList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = "pessoas.view_pessoa"
    model = Pessoa
    template_name = "pessoas/list.html"
    context_object_name = "pessoas"
    paginate_by = 20

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q", "").strip()[:150]
        status = self.request.GET.get("status", "todos")
        if q:
            qs = qs.filter(Q(nome__icontains=q) | Q(email__icontains=q) | Q(telefone__icontains=q))
        if status == "ativos":
            qs = qs.filter(ativo=True)
        elif status == "inativos":
            qs = qs.filter(ativo=False)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q", "").strip()[:150]
        context["status"] = self.request.GET.get("status", "todos")
        return context

class PessoaCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ("pessoas.add_pessoa", "pessoas.view_pessoa")
    model = Pessoa
    form_class = PessoaForm
    template_name = "pessoas/form.html"
    success_url = reverse_lazy("pessoas:list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Pessoa cadastrada com sucesso.")
        return response

class PessoaUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ("pessoas.change_pessoa", "pessoas.view_pessoa")
    model = Pessoa
    form_class = PessoaForm
    template_name = "pessoas/form.html"
    success_url = reverse_lazy("pessoas:list")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Cadastro atualizado com sucesso.")
        return response

@login_required
@permission_required(("pessoas.change_pessoa", "pessoas.view_pessoa"), raise_exception=True)
@require_POST
def alterar_situacao(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    acao = request.POST.get("acao")
    if acao not in ("ativar", "inativar"):
        from django.http import HttpResponseBadRequest
        return HttpResponseBadRequest("Ação inválida.")
    pessoa.ativo = acao == "ativar"
    pessoa.save(update_fields=["ativo", "atualizado_em"])
    messages.success(request, "Situação atualizada com sucesso.")
    return redirect("pessoas:list")
