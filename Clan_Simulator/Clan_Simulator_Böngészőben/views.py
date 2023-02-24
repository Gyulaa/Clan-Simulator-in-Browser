from django.shortcuts import render, redirect
from django.http import JsonResponse
# from .forms import MemberForm
import random
from .forms import AddMemberForm
from . models import Member

# function for overview.html
def overview(request):
    # If there is no members in the database, it creates a genesis member
    member_count = Member.objects.count()
    if member_count == 0:
        genesis_member = Member(name='Genesis', vitality=15, resilience=15, pcn=2, childnumber=0,
                                position='Pawn', balance=500, alive=True, fatherid=0)
        genesis_member.save()
    _members = Member.objects.all()
    return render(request, 'overview.html', {"members": _members})

# function for operations.html
def operations(request):
    _members = Member.objects.all()
    return render(request, 'operations.html', {"members": _members})

# function for add_member.html
def add_member(request):
    # This code gets the data from the form in add_member.html. The 'name' will be the name of the new member, based on the given fatherID it searches that person who has equal id and get its values.
    # Creates a new person with small changes/mutations based on the father's properties.
    if request.method == "POST":
        form = AddMemberForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            fatherid = form.cleaned_data['fatherid']
            father = Member.objects.get(id=fatherid)
            fathervitality = father.vitality
            fatherresilience = father.resilience
            fatherpcn = father.pcn
            fatherposition = father.position
            fatherchildnumber = father.childnumber
            # if the father reached his child limit it gives an error
            if not fatherpcn == fatherchildnumber:
                # it create the new member
                member = Member(name=name, vitality=fathervitality + random.randint(-5, 5),
                                resilience=fatherresilience + random.randint(-5, 5),
                                pcn=fatherpcn + random.randint(-1, 1),
                                childnumber=0, position=fatherposition, balance=0, alive=True, fatherid=fatherid)
                member.save()
                # update childnumber for father
                Member.objects.filter(id=fatherid).update(childnumber=fatherchildnumber + 1)
            else:
                return JsonResponse({'error': 'This person has reached the child limit.'})
            return redirect('operations')
    else:
        form = AddMemberForm()
    return render(request, 'add_member.html', {'form': form})