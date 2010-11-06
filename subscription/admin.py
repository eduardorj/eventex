import datetime
from django.contrib import admin
from django.utils.translation import ugettext as _
from django.utils.translation import ungettext
from subscription.models import Subscription
from django.conf.urls.defaults import patterns, url
from django.http import HttpResponse

class SubscriptionAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'phone', 'created_at', 'subscribed_today', 'paid')
	date_hierarchy = 'created_at'
	search_fields = ('name', 'cpf', 'email', 'phone', 'created_at', 'created_at')
	
	actions = ['mark_as_paid']
	
	# def export_subscription(self, request):
		# subscriptions = self.model.objects.all()
		# rows = [','.join([s.name, s.email]) for s in subscription]
		
		# response = HttpRespose('\r\n'.join(rows))
		# response.mimetype = "text/csv"
		# response['Content-Disposition'] = 'attachment; filename=inscricoes.csv'
		
		# return response
	
	# def get_urls(self):
		# original_urls = super(Subscription, self).get_urls()
		# extra_url = patterns('',
			# url(r'exportar-inscricoes/$'
				# self.admin_site.admin_view(self.export_subscription),
				# name='export_subscription')
		# )
		
		# return extra_url + original_urls

	def mark_as_paid(self, request, queryset):
		count = queryset.update(paid=True)
		
		msg = ungettext(
			u'%(count)d inscricao foi marcada como paga.',
			u'%(count)d inscricoes foram marcadas como pagas.',
			count,
		) % {'count': count}
		
		self.message_user(request, msg)

	mark_as_paid.short_description = _('Marcar como pagas')
		
	def subscribed_today(self, obj):
		return obj.created_at.date() == datetime.date.today()

	subscribed_today.short_description = _('Inscrito hoje?')
	subscribed_today.boolean = True
	
	# def paid(self, obj):
		# return obj
	
	# paid.short_description = _('pago?')
	# paid.boolean = True
	
admin.site.register(Subscription, SubscriptionAdmin)