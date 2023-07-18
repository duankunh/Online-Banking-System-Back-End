from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
# Create your views here.
from django.views.generic import DetailView, FormView, ListView

from banks.forms import AddBankForm, AddBranchForm
from banks.models import Bank, Branch


class AddBankView(FormView):
    template_name = 'banks/add_bank.html'
    form_class = AddBankForm

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponse('UNAUTHORIZED', status=401)
        return super().get(request)

    def post(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponse('UNAUTHORIZED', status=401)
        return super().post(request)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        bank = form.save()
        bank_id = bank.id
        return HttpResponseRedirect(f"/banks/{bank_id}/details/")


class AddBranchView(FormView):
    template_name = 'banks/add_branch.html'
    form_class = AddBranchForm

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponse('UNAUTHORIZED', status=401)
        temp = Bank.objects.all().filter(id=self.kwargs['bank_id']).first()
        if temp:
            if temp.owner != self.request.user:
                return HttpResponse('FORBIDDEN', status=403)
        else:
            return HttpResponse('NOT FOUND', status=404)
        get = super().get(request)
        return get

    def post(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponse('UNAUTHORIZED', status=401)
        temp = Bank.objects.all().filter(id=self.kwargs['bank_id']).first()
        if temp:
            if temp.owner != self.request.user:
                return HttpResponse('FORBIDDEN', status=403)
        else:
            return HttpResponse('NOT FOUND', status=404)
        return super().post(request)

    def form_valid(self, form):
        temp = Bank.objects.all().filter(id=self.kwargs['bank_id']).first()
        branch = Branch.objects.create(
            name=form.cleaned_data['name'],
            transit_num=form.cleaned_data['transit_num'],
            address=form.cleaned_data['address'],
            email=form.cleaned_data['email'],
            capacity=form.cleaned_data['capacity'],
            bank=temp
        )
        return HttpResponseRedirect(f"/banks/branch/{branch.id}/details/")


class DisplayBankView(ListView):
    template_name = 'banks/List.html'
    queryset = Bank.objects.all()
    context_object_name = 'banks'


class DisplayDetailBankView(DetailView):
    template_name = 'banks/Detail.html'
    context_object_name = 'bank'

    def get_object(self, queryset=None):
        temp = Bank.objects.all().filter(id=self.kwargs['bank_id']).first()
        if temp is None:
            return HttpResponse('NOT FOUND', status=404)
        return temp


def DisplaySpecificBranchView(request, branch_id):
    temp = Branch.objects.all().filter(id=branch_id).first()
    if temp is None:
        return HttpResponse('NOT FOUND', status=404)
    return JsonResponse(
        {"id": temp.id, "name": temp.name, 'transit_num': temp.transit_num,
         'address': temp.address,
         "email": temp.email,
         "capacity": temp.capacity,
         "last_modified": temp.last_modified})


def DisplayAllBranchesView(request, bank_id):
    branches = Branch.objects.all().filter(bank=bank_id)
    print(branches)
    if branches is None:
        return HttpResponse('NOT FOUND', status=404)

    data_json = []
    for temp in branches:
        data_json.append(
            {"id": temp.id, "name": temp.name, 'transit_num': temp.transit_num,
             'address': temp.address,
             "email": temp.email,
             "capacity": temp.capacity,
             "last_modified": temp.last_modified})
    return JsonResponse(data_json, safe=False)
