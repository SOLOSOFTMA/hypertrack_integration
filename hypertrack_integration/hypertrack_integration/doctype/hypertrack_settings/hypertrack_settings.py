# -*- coding: utf-8 -*-
# Copyright (c) 2017, MN Technique and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import hypertrack
from frappe import _

class HyperTrackSettings(Document):
	pass


def get_hypertrack():
	settings = frappe.get_doc("HyperTrack Settings")

	if not settings.hypertrack_secret_key:
		frappe.throw(_("Set HyperTrack secret key in Settings."))

	hypertrack.secret_key = settings.hypertrack_secret_key
	
	return hypertrack

