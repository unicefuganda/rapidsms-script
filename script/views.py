from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from script.forms import  ScriptForm,ScriptStepForm
from script.models import Script,ScriptStep
from django.forms.models import modelformset_factory,inlineformset_factory
from django import forms
from generic.views import generic
from generic.sorters import SimpleSorter




def manage_script(request,template,script_pk=None):

    if script_pk:
        script=get_object_or_404(Script, pk=script_pk)
    else:
        script=Script()
    form=ScriptForm(request.POST or None,instance=script )
    if form.is_valid():
        num_steps=form.cleaned_data['num_steps']
        script=form.save()
        formset=inlineformset_factory(Script,ScriptStep,extra=num_steps,form=ScriptStepForm,can_delete=False)
        stepsformset=formset(instance=script)
        return render_to_response("script/add_steps.html",dict(formset=stepsformset,title="Add first steps"),
            context_instance=RequestContext(request))


    return render_to_response(template,dict(form=form,script=script),
        context_instance=RequestContext(request))


def edit_script(request,script_pk,template="script/edit_script.html"):
    script=get_object_or_404(Script, pk=script_pk)
    script_form=ScriptForm(request.POST or None,instance=script )
    formset=inlineformset_factory(Script,ScriptStep,form=ScriptStepForm,can_delete=True)
    stepsformset=formset(instance=script)
    if formset.is_valid():
        objects = formset.save()
    if script_form.is_valid():
        script_form.save()

    return render_to_response(template,dict(formset=stepsformset,script_form=script_form),
        context_instance=RequestContext(request))


def view_scripts(request):
    return generic(
        request,
        model=Script,
        objects_per_page=25,
        results_title='Scripts',
        columns=[('Script', True, 'pk', SimpleSorter()),
               ],
    )



