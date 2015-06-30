import mandrill
from django.conf import settings


# Send email to the given receipting using mandrill
def send_email_mandrill( email_subject, email_body, from_name, from_email, admins, subaccount_name = 'barleyz' ):

		recipients = []
		for admin in admins:
			recipient = {'email': admin[1],
						'name': admin[0],
						'type': 'to'}
			recipients.append(recipient)
		recipient_email_address = None
		email_sent_status = None
		email_sent_remarks = None
		message_id = None

		try:
			# prepare mandrill client object
			mandrill_client = mandrill.Mandrill( settings.EMAIL_HOST_PASSWORD )

			# prepare mandrill message object
			message = {
				'html': email_body,
				'text': 'Barleyz',
				'subject': email_subject,
				'from_name': from_name,
				'from_email': from_email,
				'to': recipients,
				'headers': {'Reply-To': from_email},
				'important': None,
				'track_opens': None,
				'track_clicks': None,
				'auto_text': None,
				'auto_html': None,
				'inline_css': None,
				'url_strip_qs': None,
				'preserve_recipients': None,
				'view_content_link': None,
				'bcc_address': from_email,
				'tracking_domain': None,
				'signing_domain': None,
				'return_path_domain': None,
				'merge': True,
				'merge_language': 'mailchimp',
				'global_merge_vars': None,
				'merge_vars': None,
				'tags': ['tour-package-itinerary'],
				'subaccount': subaccount_name,
				'google_analytics_domains': None,
				'google_analytics_campaign': None,
				'metadata': None,
				'recipient_metadata': None,
				'attachments': None,
				'images': None
			}

			# send email
			email_result = mandrill_client.messages.send( message = message, async = False )
			print email_result

			# get email sending info
			recipient_email_address = email_result[ 0 ][ 'email' ]
			email_sent_status = email_result[ 0 ][ 'status' ]
			email_sent_remarks = email_result[ 0 ][ 'reject_reason' ]
			message_id = email_result[ 0 ][ '_id' ]

		except Exception, e:
			print e
			import logging
			logging.error( 'problem sending email to guest' )

		return recipient_email_address, email_sent_status, email_sent_remarks, message_id, email_result