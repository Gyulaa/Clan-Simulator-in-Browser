from django.shortcuts import render, redirect
from django.http import JsonResponse
# from .forms import MemberForm
import random
from .forms import AddMemberForm
from . models import Member
import json

# function for overview.html
def overview(request):
    # If there is no members in the database, it creates a genesis member
    member_count = Member.objects.count()
    if member_count == 0:
        genesis_member = Member(name='Genesis', vitality=15, resilience=15, health=100, age=2, pcn=3, childnumber=0,
                                position='Pawn', balance=500, alive=True, fatherid=0)
        genesis_member.save()
    _members = Member.objects.all()

    return render(request, 'overview.html', {"members": _members})

# function for operations.html
def operations(request):
    # If there is no members in the database, it creates a genesis member
    member_count = Member.objects.count()
    if member_count == 0:
        genesis_member = Member(name='Genesis', vitality=15, resilience=15, health=100, age=2, pcn=3, childnumber=0,
                                position='Pawn', balance=500, alive=True, fatherid=0)
        genesis_member.save()
    _members = Member.objects.all()
    return render(request, 'operations.html', {"members": _members})

#family tree
def render_family_tree(member, members, generation):
    descendants = members.filter(fatherid=member.id)
    
    # Az examinee if the member is alive
    alive_text = "(Alive)" if member.alive else "(Deceased)"
    #generate indentation
    html = f'<li style="margin-left: {generation*6}px">'
    html += f'<span class="caret { "deceased" if not member.alive else "" }">{member.name}  - ID: {member.id}</span>'
    
    if descendants:
        html += '<ul class="nested">'
        for descendant in descendants:
            html += render_family_tree(descendant, members, generation+1)
        html += '</ul>'
        
    html += '</li>'
    return html

#function for family_tree.html
def family_tree(request):
    members = Member.objects.all()
    tree_html = ''

    for member in members.filter(fatherid=0):
        tree_html += render_family_tree(member, members, 0)

    return render(request, 'family_tree.html', {'tree_html': tree_html})

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
            fatherage = father.age
            fatherpcn = father.pcn
            fatherposition = father.position
            fatherchildnumber = father.childnumber
            fatheralive = father.alive
            if fatheralive == True:
                if fatherage > 1:
                    if not fatherpcn == fatherchildnumber:
                        #mutation in vitality
                        childrenvitality = fathervitality + random.randint(-5, 5)
                        #min value: 0
                        if childrenvitality < 0:
                            childrenvitality = 0
                        #max value: 100
                        if childrenvitality > 100:
                            childrenvitality = 100
                        #mutation in resilience
                        childrenresilience = fatherresilience + random.randint(-5, 5)
                        #min value: 0
                        if childrenresilience < 0:
                            childrenresilience = 0
                        #max value: 100
                        if childrenresilience > 100:
                            childrenresilience = 100
                        # mutation in the possible child number
                        childrenpcn = fatherpcn + random.randint(-1, 1)
                        #min value: 0
                        if childrenpcn < 0:
                            childrenpcn = 0
                        #max value: 100
                        if childrenpcn > 5:
                            childrenpcn = 5
                        # it creates the new member
                        member = Member(name=name, vitality=childrenvitality,
                                        resilience=childrenresilience,
                                        pcn=childrenpcn,
                                        childnumber=0, position=fatherposition, balance=50, alive=True, fatherid=fatherid)
                        member.save()
                        # update childnumber for father
                        Member.objects.filter(id=fatherid).update(childnumber=fatherchildnumber + 1)        
                    # if the father reached his child limit it gives an error
                    else:
                        return JsonResponse({'error': 'This person has reached the child limit.'})
                else:
                    return JsonResponse({'error': 'This person is too young.'})
            else:
                return JsonResponse({'error': 'This person has died.'})
            return redirect('operations')
    else:
        form = AddMemberForm()
    return render(request, 'add_member.html', {'form': form})


# function for age increment and health decrement
def update_members(request):
    # Get all members from the database
    members = Member.objects.all()
    # Loop through each member and update values
    for member in members:
        if member.alive == True:
            # income based on vitality
            if member.age > 1:
                member.balance += member.vitality * 10
                # income based on ranks: peasant, citizen, baron, count, king
                if member.position == "Pawn":
                    member.balance -= 50
                elif member.position == "Baron":
                    member.balance += 100
                elif member.position == "Count":
                    member.balance += 200
                elif member.position == "King":
                    member.balance += 500
                # promotion
                if member.balance > 5000:
                    member.position = "King"
                elif member.balance > 2000:
                    member.position = "Count"
                elif member.balance > 1000:
                    member.position = "Baron"
                elif member.balance > 500:
                    member.postion = "Citizen"
                else:
                    member.position = "Pawn"
            # family expenses
            member.balance -= member.childnumber * 100
            # member getting older
            member.age += 1
            # members health
            if member.age < 2:
                childhoodIllness = random.randint(1, 4)
                if childhoodIllness == 4:
                    member.health = -1
                    member.alive = False
                if len(members) > 3:
                    member.health -= 1250 / member.resilience + random.randint(-30, 30)
                else:
                    member.health -= 500 / member.resilience + random.randint(-30, 30)
            elif member.age > 4:
                member.health -= 1000 / member.resilience + random.randint(-40, 40)
            else:
                member.health -= 750 / member.resilience + random.randint(-30, 30)
            # dying by health
            if member.health <= 0:
                member.alive = False
                member.health = -1
                sons = Member.objects.filter(fatherid=member.id)
                for son in sons:
                    if son.age < 2:
                        son.alive = False
                        son.health = -1
                        son.balance = -1
                        son.save()
            # dying by bankruptcy
            if member.age > 1:
                if member.balance < 1:
                    member.alive = False
                    member.balance=-1
                sons = Member.objects.filter(fatherid=member.id)
                for son in sons:
                    if son.age < 2:
                        son.alive = False
                        son.balance = -1
                        son.health = -1
                        son.save()
            member.save()
    for member in members:
        if member.alive == False:
        # Inherit wealth
            if member.balance > 0:
                sons = []
                grandsons = []
                brothers = []
                sonsofbro = []
                alive = []

                for competitor in members:
                    # make sure not the same person
                    if competitor.id != member.id:
                        # children of member
                        if competitor.fatherid == member.id:
                            #children is alive?
                            if competitor.alive == True:
                                #append son's id
                                sons.append(competitor.id)
                            else:
                                for grandcompetitor in members:
                                    if grandcompetitor.fatherid == competitor.id:
                                        if grandcompetitor.alive==True:
                                            grandsons.append(grandcompetitor.id)
                        #brothers
                        elif competitor.fatherid == member.fatherid:
                            if competitor.alive == True:
                                brothers.append(competitor.id)
                            else:
                                for grandcompetitor in members:
                                    if grandcompetitor.fatherid == competitor.id:
                                        if grandcompetitor.alive==True:
                                            sonsofbro.append(grandcompetitor.id)
                        else:
                            if competitor.alive == True:
                                alive.append(competitor.id)
                #possible outcomes
                if len(sons) > 0:
                    inheritance_value = member.balance / len(sons)
                    for heir in members:
                        if heir.id in sons:
                            heir.balance += inheritance_value
                            member.balance = 0
                            heir.save()
                elif len(grandsons) > 0:
                    inheritance_value = member.balance / len(grandsons)
                    for heir in members:
                        if heir.id in grandsons:
                            heir.balance += inheritance_value
                            member.balance = 0
                            heir.save()
                elif len(brothers) > 0:
                    inheritance_value = member.balance / len(brothers)
                    for heir in members:
                        if heir.id in brothers:
                            heir.balance += inheritance_value
                            member.balance = 0
                            heir.save()
                elif len(sonsofbro) > 0:
                    inheritance_value = member.balance / len(sonsofbro)
                    for heir in members:
                        if heir.id in sonsofbro:
                            heir.balance += inheritance_value
                            member.balance = 0
                            heir.save()
                else:
                    if len(alive) > 0:
                        inheritance_value = member.balance / len(alive)
                        for heir in members:
                            if heir.id in alive:
                                heir.balance += inheritance_value
                                member.balance = 0
                                heir.save()
                member.save()
    return redirect('operations')

def reset_game(request):
    # Törölje az összes személy rekordot
    Member.objects.all().delete()
    # Egyéb inicializálási lépések, ha szükséges
    return redirect('operations')