from django.shortcuts import render,redirect,get_object_or_404
from  books.models import Book
from django.forms import ModelForm
from  .models import Book
from  .forms import BookForm

def book_list(request):
    book=Book.objects.all()
    return render(request, 'books/book_list.html', {'book':book})

def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'form/form.html', {'form':form})

def book_update(request,book_id):
    book = get_object_or_404(Book,pk=book_id)
    form = BookForm(request.POST or None , instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request ,'form/form.html',{'form': form})

def book_delete(request,book_id):
    book = get_object_or_404(Book,pk=book_id)
    if request.method=='POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/Book_confirm_delete.html', {"book":book})

def view_book(request,book_id):
    book= get_object_or_404(Book, pk=book_id)
    return render(request,'books/viewbook.html',{"book":book})
