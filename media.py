# coding=utf-8
class Movie():
	"""电影类 用于构建电脑实例对象"""
	def __init__(self, title,poster_image_url,trailer_youtube_url):
		self.title = title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url