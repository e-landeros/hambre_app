from hambreApp.models import Customer, Driver

###############user object depricated from fb graph API need another way to get userid ##########
def create_user_by_type(backend, user, request, response, *args, **kwargs):
    if backend.name == 'facebook':
        avatar = 'https://graph.facebook.com/%s/picture?type=large' % response['id']
        
    # if user object is driver and not in db we will crate a new one
    # using user id from request object 
    if request['user_type'] == "driver" and not Driver.objects.filter(user_id=user.id):
        Driver.objects.create(user_id=user.id, avatar = avatar)
    elif not Customer.objects.filter(user_id=user.id):
        Customer.objects.create(user_id = user.id, avatar = avatar)

