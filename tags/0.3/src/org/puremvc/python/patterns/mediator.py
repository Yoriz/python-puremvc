"""
PureMVC - Copyright(c) 2006-08 Futurescale, Inc., Some rights reserved.
Your reuse is governed by the Creative Commons Attribution 3.0 United States License
"""

import org.puremvc.python.interfaces
import org.puremvc.python.patterns.observer
import org.puremvc.python.patterns.facade

class Mediator(org.puremvc.python.patterns.observer.Notifier, org.puremvc.python.interfaces.IMediator, org.puremvc.python.interfaces.INotifier):
	"""
	A base C{IMediator} implementation. 
	 
	@see: L{View<org.puremvc.as3.core.view.View>}
	"""
	
	NAME = "Mediator"
	facade = None
	viewComponent = None
	mediatorName = None
	
	def __init__(self, mediatorName=None, viewComponent=None):
		"""
		Mediator Constructor
		
		Typically, a C{Mediator} will be written to serve
		one specific control or group controls and so,
		will not have a need to be dynamically named.
		"""
		self.facade = org.puremvc.python.patterns.facade.Facade.getInstance()
		if mediatorName:
			self.mediatorName = mediatorName
		else:
			self.mediatorName = self.NAME
		self.viewComponent = viewComponent	
	
	def getMediatorName(self):
		"""
		Get the name of the C{Mediator}.
		@return: the Mediator name
		"""
		return self.mediatorName
	
	def setViewComponent(self,viewComponent):
		"""
		Set the C{IMediator}'s view component.
		
		@param viewComponent: the view component
		"""
		self.viewComponent = viewComponent
		
	def getViewComponent(self):
		"""
		Get the C{Mediator}'s view component.
		
		@return: the view component
		"""
		return self.viewComponent
	
	def listNotificationInterests(self):
		"""
		List the C{INotification} names this
		C{Mediator} is interested in being notified of.
		
		@return: List the list of C{INotification} names
		"""
		return []
	
	def handleNotification(self,notification):
		"""
		Handle C{INotification}s.
		
		Typically this will be handled in a if/else statement,
		with one 'comparison' entry per C{INotification}
		the C{Mediator} is interested in.
		"""
		pass

	def onRegister(self):
		"""
		Called by the View when the Mediator is registered
		"""
		pass

	def onRemove(self):
		"""
		Called by the View when the Mediator is removed
		"""
		pass