from django.db import models
from django.utils.translation import ugettext_lazy as _
from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import RichText, Orderable, Slugged
from mezzanine.pages.models import Page
from mezzanine.utils.models import upload_to


class HomePage(Page, RichText):
	'''
	A page representing the format of the home page
	'''
	introduction_heading = models.CharField(max_length=200, help_text="The heading at the top of the page", default="start a love for learning")
	arrange_visit_link = models.URLField(max_length=200, help_text="The arrange a visit link at the top of the page")
	see_our_setting_link = models.URLField(max_length=200, help_text="The see setting link at the top of the page")
	
	welcome_heading = models.CharField(max_length=200, default="welcome to owlets")
	welcome_text = models.TextField()
	welcome_link = models.URLField(max_length=200, help_text="This links to where the rest of the intro is")

	what_we_do_heading = models.CharField(max_length=200, default="some of the things we get upto")
	what_we_do_link = models.CharField(max_length=200)

	what_people_are_saying_heading = models.CharField(max_length="200", default="what parents are saying")

	our_fees_heading = models.CharField(max_length="200", default="our fees")

	class Meta:
		verbose_name = _("Home page")
		verbose_name_plural = _("Home pages")

class Slide(Orderable):
	'''
	A slider connected to a HomePage
	'''
	homepage = models.ForeignKey(HomePage, related_name="slides")
	image = FileField(verbose_name=_("Image"), upload_to=upload_to("theme.slide.image", "slides"), format="Image", max_length=255, null=True, blank=True)

class DoBox(Orderable):
	'''
	A 'what we do box' on the HomePage
	'''
	homepage = models.ForeignKey(HomePage, related_name="dobox")
	
	image = FileField(verbose_name=_("Image"), upload_to=upload_to("theme.dobox.image", "doboxes"), format="Image", max_length=255, null=True)
	title = models.CharField(max_length=255)
	text = models.CharField(max_length=255)
	link = models.CharField(max_length=255)

	class Meta:
		verbose_name = _("What we do box")
		verbose_name_plural = _("What we do boxes")


class ParentsSaying(Orderable):
	'''
	A testimonials box on the HomePage
	'''
	homepage = models.ForeignKey(HomePage, related_name="parentssaying")
	saying_quote = models.CharField(max_length=255)
	saying_name = models.CharField(max_length=255)

	class Meta:
		verbose_name = _("Testimonial")
		verbose_name_plural = _("Testimonials")

class Fees(Orderable):
	'''
	A group of fees
	'''
	homepage = models.ForeignKey(HomePage, related_name="fees")
	fees_age = models.CharField(max_length=255, help_text="Age group")
	fees_price = models.CharField(max_length=255)
	fees_description = models.CharField(max_length=255, help_text="Description")
	fees_link = models.CharField(max_length=255)

	class Meta:
		verbose_name = _("Fee")
		verbose_name_plural = _("Fees")

class A_Page(Page):
	'''
	A page representing a simple text based page
	'''
	heading = models.CharField(max_length=255, help_text="Page Title")
	image = FileField(verbose_name=_("Image"), upload_to=upload_to("theme.pages.image", "theimages"), format="Image", max_length=255, null=True)
	intropara = models.CharField(max_length=255, help_text="Introduction paragraph", verbose_name="First paragraph")

	class Meta:
		verbose_name = _("Page")

class Sections(Orderable):
	'''
	part of a richtext page - allowing you to post multiple Sections
	'''
	page = models.ForeignKey(A_Page, related_name="section")
	heading = models.CharField(max_length="255", verbose_name="section heading")
	content = models.TextField(blank=True, verbose_name="Text sections")

	class Meta:
		verbose_name = _("Section")
		verbose_name_plural = _("Sections")
