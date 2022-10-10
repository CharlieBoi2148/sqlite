import database


stuff=[
		('2627 manor rd','North','manor@gmail.com'),
		('10421 Old Menchaca Rd','North', 'susan@austinsitesolution.com'),
		('5329 Cameron Rd','South','gage@gmail.com'),
	]

database.add_many(stuff)

database.show_all()