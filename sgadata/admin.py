from django.contrib import admin
from models import *
from helper import *
from datetime import datetime, timedelta
from django.conf import settings

# Send For Review to manager
# def send_for_review( modeladmin, request, queryset ):
# 	queryset.update( completed = True , user_completed_date = datetime.now() )
# send_for_review.short_description = "Send For Review to manager"

# Send back to user for updating
def unmark_reviewed( modeladmin, request, queryset ):
	queryset.update( completed = False, user_completed_date = None )
	queryset.update( reviewed = False, completed_date = None )
unmark_reviewed.short_description = "Unmark Completed and Reviewed"

# Unmark Task not completed
def unmark_completed( modeladmin, request, queryset ):
	queryset.update( completed = False, user_completed_date = None )
unmark_completed.short_description = "Unmark Task Completed"

# Unmark File Name and location proper
def unmark_filename_and_lcoation_proper( modeladmin, request, queryset ):
	queryset.update( filename_and_location_proper = False )
unmark_filename_and_lcoation_proper.short_description = "Unmark File Name and Location Proper"

# Unmark Task Dispatched
def unmark_dispatched( modeladmin, request, queryset ):
	queryset.update( dispatched = False )
unmark_dispatched.short_description = "Unmark Task Dispatched"

# Mark Task Completed
def mark_completed( modeladmin, request, queryset ):
	queryset.update( completed = True, user_completed_date = datetime.now() )
mark_completed.short_description = "Mark Task Completed"

# Mark Task Reviewed
def mark_reviewed( modeladmin, request, queryset ):
	queryset.update( reviewed = True, completed_date = datetime.now() )
mark_reviewed.short_description = "Mark Task Reviewed"

# Mark Task Dispatched
def mark_dispatched( modeladmin, request, queryset ):
	queryset.update( dispatched = True )
mark_dispatched.short_description = "Mark Task Dispatched"

# Mark FileName and Location Proper
def mark_filename_and_lcoation_proper( modeladmin, request, queryset ):
	queryset.update( filename_and_location_proper = True )
mark_filename_and_lcoation_proper.short_description = "Mark File Name and Location Proper"

# Send Transmittal
def send_transmittal( modeladmin, request, queryset ):
	email_subject = "Transmittal Entry"
	email_body = '%s/%s' %( queryset[0].filelocation, queryset[0] )
	from_name = settings.DEFAULT_FROM_NAME
	from_email = settings.DEFAULT_FROM_EMAIL
	recipients = settings.ADMINS
	send_email_mandrill(
		email_subject,
		email_body,
		from_name,
		from_email,
		recipients,
	)
send_transmittal.short_description = "Send Transmittal"

# Register your models here.
class TaskAdmin( admin.ModelAdmin ):
	fieldsets = (
		(None, {
			'fields': ( 'drawing', )
		}),
		(None, {
			'fields': ( 'project','task_type', 'phase', 'block' ,'stage', 'discipline')
		}),
		('Drawing Number Details', {
			'fields': ( 'floor_plan_type', 'floor_level_tracker', 'revision_version', 'internal_revision_version' )
		}),
		('Drawing Description', {
			'fields': ( 'drawing_description', )
		}),
		(None, {
			'fields': ('created_on', 'task_master', 'related_task', 'hours', 'scheduled_date', 'user_completed_date', 'filelocation')
		}),
		(None, {
			'fields': ( 'completed_date', 'comments', 'filename_and_location_proper' )
		})
	)
	list_display = ( 'drawing','task_master' , 'hours', 'scheduled_date', 'completed', 'user_completed_date_24_hour' , 'reviewed', 'completed_date_24_hour', 'filename_and_location_proper', 'dispatched' )
	search_fields = ( 'drawing', )
	readonly_fields = ('drawing', 'created_on', 'user_completed_date', 'completed_date' )
	list_filter = ( 'task_type', 'reviewed', 'completed', 'task_master', 'project' )
	# list_editable = ( 'completed', 'reviewed', 'dispatched', 'filename_and_location_proper' )

	actions = [ unmark_dispatched, unmark_filename_and_lcoation_proper, unmark_reviewed, unmark_completed, mark_completed, mark_dispatched, mark_reviewed, mark_filename_and_lcoation_proper, send_transmittal ]
	ordering = ('task_type',)

	def user_completed_date_24_hour( self, obj ):
		if obj.user_completed_date:
			return (obj.user_completed_date + timedelta(hours=5.5)).strftime( '%b %d, %Y %H:%m' )
		else:
			return None
	user_completed_date_24_hour.short_description = "user_completed_date"

	def completed_date_24_hour( self, obj ):
		if obj.completed_date:
			return (obj.completed_date + timedelta(hours=5.5)).strftime( '%b %d, %Y %H:%m' )
		else:
			return None
	completed_date_24_hour.short_description = "completed_date"

	def get_queryset(self, request):
		qs = Task.objects.filter( project__group__in =  request.user.groups.all() )
		return qs

class PhaseAdmin( admin.ModelAdmin ):
	list_display = ( 'title', 'project', 'code' )
	search_fields = ( 'title', 'project' )
	list_filter = ( 'project' )

class BlockAdmin( admin.ModelAdmin ):
	list_display = ( 'title', 'project', 'code' )
	search_fields = ( 'title', 'project' )
	list_filter = ( 'project' )

admin.site.register( Task, TaskAdmin )
admin.site.register( Project )
admin.site.register( Phase )
admin.site.register( Block )
admin.site.register( Stage )
admin.site.register( Discipline )
admin.site.register( FloorPlanType )
admin.site.register( FloorLevelTracker )
admin.site.register( RevisionVersion )
admin.site.register( InternalRevisionVersion )

admin.site.register( Category )
admin.site.register( SubCategory )

class ContactAdmin( admin.ModelAdmin ):
    # actions = ['activate_users', 'resend_activation_email']
    list_display = ( 'name', 'category', 'subcategory', 'mobile', 'email' )
    search_fields = ( 'name', 'email', 'reference' )
    list_filter = ( 'category', 'subcategory', 'project' )

admin.site.register( Contact, ContactAdmin )
