"""
Wiki

Encyclopedia website

Gemaakt door: Susanne Becker
"""
from markdown2 import Markdown
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

from . import util


class NewEntryForm(forms.Form):
    """
    Form for new entries.
    """
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 20, 'rows': 7}))
    edit = forms.BooleanField(initial=False, widget=forms.HiddenInput(), required=False)

def index(request):
    """
    Display all encyclopedia entries.
    """
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    """
    Redirect to encyclopedia page if page exist.
    """
    page = util.get_entry(entry)

    if page is None:
        return render(request, "encyclopedia/error.html")
    else:
        return render(request, "encyclopedia/entry.html",{
            "title": entry,
            "content": Markdown().convert(page)
        })

def search(request):
    """
    Search an entry.
    """
    query = request.GET.get('q')
    if(util.get_entry(query) is None):
        entrylist = []
        for entry in util.list_entries():
            if query.lower() in entry.lower():
                entrylist.append(entry)
        return render(request, "encyclopedia/index.html", {
            "entries": entrylist
        })  
    else:
        return HttpResponseRedirect(reverse("entry", kwargs={'entry': query}))

def newEntry(request):
    """
    Create a new entry page.
    """
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
                title = form.cleaned_data['title']
                content = form.cleaned_data['content']
                if (title not in util.list_entries() or form.cleaned_data["edit"] is True):
                    util.save_entry(title, content)
                    return HttpResponseRedirect(reverse("entry", kwargs={'entry': title}))
                else:    
                    return render(request, "encyclopedia/error-entry.html", {
                        "title": entry
                    })
        else:
            return render(request, "encyclopedia/newEntry.html", {
             "form": form
            })
    else:
        return render(request, "encyclopedia/newEntry.html", {
            "form": NewEntryForm()
        })

def edit(request, entry):
    """
    If page has an entry: redirect to edit.html, place markdown content already in field 
    and dont give the user permission to change the title.
    """
    page = util.get_entry(entry)

    if page is None:
        return render(request, "encyclopedia/error.html", {
            "title": entry
        })
    else:
        form = NewEntryForm()
        form.fields["edit"].initial = True
        form.fields["title"].initial = entry
        form.fields["title"].widget = forms.HiddenInput()
        form.fields["content"].initial = page
        return render(request, "encyclopedia/edit.html", {
            "form": form,
            "edit": form.fields["edit"].initial,
            "title": form.fields["title"].initial   
        })