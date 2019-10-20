from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect

# Create your views here.
from contacts.models import Contact
from django.conf import settings


def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']

        # Check if authenticated user has already made an enquiry about same listing
        if request.user.is_authenticated:
            has_contacted = Contact.objects.all().filter(email__icontains=email, listing_id=listing_id)
            if has_contacted:
                messages.error(request, 'You have already made an enquiry for this listing')
                return redirect('/listings/' + listing_id)

        contact_query = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone,
                                message=message, user_id=user_id)
        contact_query.save()

        # Sending a email
        send_mail(subject='Property Listing Enquiry',
                  message=f'There has been an enquiry for {listing} by {name}. Sign into Admin Panel for more info.',
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=['akumar@ijonaservices.com', 'vikashgaurav.vkg@gmail.com'],
                  fail_silently=False
                  )

        messages.success(request, 'Your message has been send successfully. A realtor will get back to you soon')

        return redirect('/listings/' + listing_id)
