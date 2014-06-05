from django.contrib import admin
from django.db import models
from mezzanine.pages.admin import PageAdmin
from mezzanine.core.admin import TabularDynamicInlineAdmin
from .models import HomePage, Slide, DoBox, ParentsSaying, Fees, A_Page, Sections

class SlideInline(TabularDynamicInlineAdmin):
	model = Slide

class DoBoxInline(TabularDynamicInlineAdmin):
	model = DoBox

class ParentsSayingInline(TabularDynamicInlineAdmin):
	model = ParentsSaying

class FeesInline(TabularDynamicInlineAdmin):
	model = Fees

class HomePageAdmin(PageAdmin):
	inlines = [SlideInline, DoBoxInline, ParentsSayingInline, FeesInline,]
	exclude = ['content',]

class SectionsInline(TabularDynamicInlineAdmin):
	model = Sections

class A_PageAdmin(PageAdmin):
	inlines = [SectionsInline,]

admin.site.register(HomePage, HomePageAdmin)
admin.site.register(A_Page, A_PageAdmin)
