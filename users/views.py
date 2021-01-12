from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm
from blog.models import Post
from store.models import Product
# Create your views here.
def register(request):
	if request.method=='POST':
		form=UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request,f'Your account has been created , you are now able to log in')
			return redirect('login')
	else:	
		form=UserRegisterForm()
	return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
	if request.method=='POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		if u_form.is_valid():
			u_form.save()
			messages.success(request,f'Your account has been updated!')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)	
	context = {
		'u_form': u_form,
	}
	return render(request, 'users/profile.html', context)




@login_required
def favourite_add(request,pk):
	post = get_object_or_404(Post,pk=pk)
	if post.favourites.filter(pk=request.user.pk).exists():
		post.favourites.remove(request.user)
		fav = False
	else:
		fav = True
		post.favourites.add(request.user)
	return HttpResponseRedirect(request.META['HTTP_REFERER'])		



@login_required
def favourite_addd(request,id):
	product = get_object_or_404(Product,pk=id)
	if product.favourites.filter(pk=request.user.pk).exists():
		product.favourites.remove(request.user)
		fav = False
	else:
		fav = True
		product.favourites.add(request.user)
	return HttpResponseRedirect(request.META['HTTP_REFERER'])		



@login_required
def favourite_list(request):
	user = request.user
	new = user.favourite.all()
	newS = user.fav.all()
	return render(request,'users/favorites.html',{'new':new ,'newS':newS})



