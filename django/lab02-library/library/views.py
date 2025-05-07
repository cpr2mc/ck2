from django.shortcuts import render, get_object_or_404
from .models import Book, Author

def book_list(request):
    books = Book.objects.order_by('title')
    context = {'books': books,}
    return render(request, 'library/book_list.html', context)

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'library/book_detail.html', {'book': book,})