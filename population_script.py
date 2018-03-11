# Population script for WAD2 project 2018 by Euan McGrevey and Sam Griffin

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
					  'uofgconnect.settings')

import django
django.setup()
from social.models import University, College, Subject, Module, UserProfile, Follow, Post, Comment, Notification

def populate():

	data = {
		"University of Glasgow": { # University
			"logo": None,
			"colour": "003865",
			"email_domain": "gla.ac.uk",
			"colleges": { # Colleges
				"College of Science and Engineering": {
					"Computing Science": [ # Subject
						"Computer Systems 2", # Module
						"Java Programming 2",
						"Object Oriented Software Engineering",
						"Algorithms and Data Structures"
					],
					"Physics": [
						"Programming C under Linux",
						"Forces"
					],
					"Chemistry": [
						"Acids"
					]
				},
				"College of Arts": {
					"Music": [
						"Music Theory",
						"Music History"
					]
				}
			}
		},
		"University of Sussex": { # University
			"logo": None,
			"colour": "003B49",
			"email_domain": "sussex.ac.uk",
			"colleges": { # Colleges
				"College of Science and Engineering": {
					"Computer Science and Artificial Intelligence": [ # Subject
						"Introduction to Programming", # Module
						"Mathematical Concepts",
						"Programming Concepts",
						"Computer Vision",
						"Intelligence in Animals and Machines"
					]
				}
			}
		}
	}

	for uni, uni_data in data.items():
		u = add_uni(uni, uni_data['colour'], uni_data['email_domain'])

		for college, subjects in uni_data['colleges'].items():
			c = add_col(college, u)

			for subject, modules in subjects.items():
				s = add_sub(subject, c)

				for module in modules:
					m = add_module(module, s)


	# Now to create some dummy people and posts

	# users = None

def add_module(name, sub):
	m = Module.objects.get_or_create(subject=sub, name=name)[0]
	m.save()
	return m

def add_sub(name, college):
	s = Subject.objects.get_or_create(name=name, college=college)[0]
	s.save()
	return s

def add_col(name, uni):
	c = College.objects.get_or_create(name=name, university=uni)[0]
	c.save()
	return c

def add_uni(name, colour, domain, logo=None):
	u = University.objects.get_or_create(name=name, colour=colour, email_domain=domain, logo=logo)[0]
	u.save()
	return u
	



# Execution
if __name__ == '__main__':
	print("Starting population script...")
	populate()
	print("Population script complete")
