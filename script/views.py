from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from script.forms import  ScriptForm,ScriptStepForm
from script.models import Script,ScriptStep
from django import forms






def manage_script(request,template,script_pk=None):

    if script_pk:
        script=get_object_or_404(Script, pk=script_pk)
    else:
        script=Script()
    form=ScriptForm(request.POST or None,instance=script )
    if form.is_valid():
        num_steps=form.cleaned_data['num_steps']
        from django.forms.formsets import formset_factory
        formset=formset_factory(ScriptStepForm, extra=num_steps)

        render_to_response(template,dict(formset=formset,title="Add first steps"),
            context_instance=RequestContext(request))


    return render_to_response(template,dict(form=form,script=script),
        context_instance=RequestContext(request))

