from django.db import models
from django.contrib.auth.models import User, Group
from datetime import datetime


class Project( models.Model ):
	title = models.CharField( max_length = 255, blank = False )
	code = models.CharField( max_length = 255, blank = False )
	is_active = models.BooleanField( default = False )
	group = models.ForeignKey( Group, blank = True, null = True )

	def __unicode__( self ):
		return u'%s ( %s )' % ( self.code, self.title )


class Phase( models.Model ):
	project = models.ForeignKey( Project )
	title = models.CharField( max_length = 255, blank = False )
	code = models.CharField( max_length = 255, blank = False )
	is_active = models.BooleanField( default = False )

	def __unicode__( self ):
		return u'%s ( %s )' % ( self.code, self.title )


class Block( models.Model ):
	project = models.ForeignKey( Project )
	title = models.CharField( max_length = 255, blank = False )
	code = models.CharField( max_length = 255, blank = False )
	is_active = models.BooleanField( default = False )

	def __unicode__( self ):
		return u'%s ( %s )' % ( self.code, self.title )


class Stage( models.Model ):
	title = models.CharField( max_length = 255, blank = False )
	code = models.CharField( max_length = 255, blank = False )
	is_active = models.BooleanField( default = False )

	def __unicode__( self ):
		return u'%s ( %s )' % ( self.code, self.title )


class Discipline( models.Model ):
	title = models.CharField( max_length = 255, blank = False )
	code = models.CharField( max_length = 255, blank = False )
	is_active = models.BooleanField( default = False )

	def __unicode__( self ):
		return u'%s ( %s )' % ( self.code, self.title )


class FloorPlanType( models.Model ):
	title = models.CharField( max_length = 255, blank = False )
	code = models.CharField( max_length = 255, blank = False )
	is_active = models.BooleanField( default = False )

	def __unicode__( self ):
		return u'%s ( %s )' % ( self.code, self.title )


class FloorLevelTracker( models.Model ):
	title = models.CharField( max_length = 255, blank = False )
	code = models.CharField( max_length = 255, blank = False )
	is_active = models.BooleanField( default = False )

	def __unicode__( self ):
		return u'%s ( %s )' % ( self.code, self.title )


class RevisionVersion( models.Model ):
	title = models.CharField( max_length = 255, blank = False )
	code = models.CharField( max_length = 255, blank = False )
	is_active = models.BooleanField( default = False )

	def __unicode__( self ):
		return u'%s ( %s )' % ( self.code, self.title )


class InternalRevisionVersion( models.Model ):
	title = models.CharField( max_length = 255, blank = False )
	code = models.CharField( max_length = 255, blank = False )
	is_active = models.BooleanField( default = False )

	def __unicode__( self ):
		return u'%s ( %s )' % ( self.code, self.title )


class Task( models.Model ):
	project = models.ForeignKey( Project )
	TASK_TYPE = (
			('UNPLANNED', 'Unplanned'),
			('PLANEED', 'planned'),
		)
	task_type = models.CharField( max_length=255,
									choices=TASK_TYPE, default='UNPLANNED')
	phase = models.ForeignKey( Phase )
	block = models.ForeignKey( Block )
	stage = models.ForeignKey( Stage )
	discipline = models.ForeignKey( Discipline )
	floor_plan_type = models.ForeignKey( FloorPlanType )
	floor_level_tracker = models.ForeignKey( FloorLevelTracker )
	revision_version = models.ForeignKey( RevisionVersion )
	internal_revision_version = models.ForeignKey( InternalRevisionVersion )
	drawing = models.CharField( max_length = 255, blank = False )
	drawing_description = models.TextField( blank = True )
	created_on = models.DateTimeField( default=datetime.now, blank=True )
	task_master = models.ForeignKey( User )
	related_task = models.CharField( max_length = 255, blank = True )
	hours = models.CharField( max_length = 255, blank = True )
	scheduled_date = models.DateField( blank = False )
	completed = models.BooleanField( default = False )
	user_completed_date = models.DateTimeField( null=True, blank=True )
	filelocation = models.CharField( max_length = 255, blank = True )

	reviewed = models.BooleanField( default = False )
	completed_date = models.DateTimeField( null = True, blank = True )
	comments = models.TextField( blank = True )
	filename_and_location_proper =  models.BooleanField( default = False, verbose_name = 'FileLocation?', help_text = "Is Filename and Location Proper?" )
	dispatched = models.BooleanField( default = False )

	def __unicode__( self ):
		return u'%s' % ( self.drawing )

	def save(self, *args, **kwargs):

		if self.completed:
			self.user_completed_date = datetime.now()
		else:
			self.user_completed_date = None
		if self.reviewed:
			self.completed_date = datetime.now()
		else:
			self.completed_date = None
		self.drawing = "%s%s-%s-%s-%s-%s-%s-R%s%s" % ( self.project.code, self.block.code, \
			self.phase.code, self.stage.code, self.discipline.code , self.floor_plan_type.code, self.floor_level_tracker.code, \
			self.revision_version.code, self.internal_revision_version.code )

		super(Task, self).save(*args, **kwargs)


class Category( models.Model ):
	title = models.CharField( max_length = 255, blank = False )
	created_at = models.DateTimeField( auto_now_add = True )
	def __unicode__( self ):
		return u'%s' % ( self.title )


class SubCategory( models.Model ):
	category = models.ForeignKey( Category, blank = True, null = True )
	title = models.CharField( max_length = 255, blank = False )
	created_at = models.DateTimeField( auto_now_add = True )
	def __unicode__( self ):
		return u'%s' % ( self.title )


class Contact( models.Model ):
	project = models.ForeignKey( Project, blank = True, null = True )
	category = models.ForeignKey( Category )
	subcategory = models.ForeignKey( SubCategory, blank = True, null = True )
	name = models.CharField( max_length = 255, blank = False )
	mobile = models.CharField( max_length = 255, blank = False )
	work_telephone = models.CharField( max_length = 255, blank = True )
	residence_telephone = models.CharField( max_length = 255, blank = True )
	designation = models.CharField( max_length = 255, blank = True )
	email = models.EmailField( max_length = 255, blank = False )
	alternate_email = models.TextField( blank = True )
	date_of_birth = models.DateField( blank = True, null = True )
	family_members = models.TextField( blank = True )
	office_address = models.TextField( blank = True )
	residential_address = models.TextField( blank = True )
	reference = models.CharField( max_length = 255, blank = True )
	remarks = models.TextField( blank = True )
	created_at = models.DateTimeField( auto_now_add = True )

	def __unicode__( self ):
		return u'%s' % ( self.name )