# This program asks the name and age of the user. Based on age, 
# it displays different messages

user_input = input( 'Qual é o seu nome? ' ) 

print( 'Olá, ' + user_input + '. Prazer em te conhecer!' )

user_age = int( input( 'Me conta qual a sua idade? ' ) )

if user_age < 10: 
	print( 'Que legal! Eu gosto muito do número ' + str( user_age ) + '!' )

elif user_age < 70: 
	print( 'Hmmm, que interessante. Tenho certeza que irá compreender perfeitamente o que irei te explicar!' )

else:
	print( 'Incrível! Também espero chegar aos ' + str( user_age ) + ' anos!' )