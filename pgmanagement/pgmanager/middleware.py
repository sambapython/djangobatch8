from django.shortcuts import render
from pgmanager.models import Track
class RequestTrack:
	def __init__(self, view):
		self.view=view
	def __call__(self, request):
		# some code need to execute before processign every request
		#print("before processing")
		resp = self.view(request)
		# some code need to execute after processign every request
		#print("after processing"
		if resp.status_code==404:
			return render(request,"pgmanager/404.html")
		if resp.status_code==500:
			return render(request,"pgmanager/500.html")
		track = Track(status_cod=resp.status_code, url=request.get_raw_uri())
		track.save()
		return resp
