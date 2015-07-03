try:
	from setuptools import setup
except:
	from distutils.core import setup


config = {
	"description" : "my project",
	"author" : "Shirley Berry",
	"url" : "project url",
	"download_url" : "download it here",
	"author_email" : "shirleylberry@gmail.com",
	"version:" : "0.0.1",
	"install_requires" : ["nose"],
	"packages" : ["gesso"]
	"scripts" : ['testscripts'],
	"name" : "gesso",
}

setup(**config)