

def run(data, cunt):
	for i in range(len(data)):
		if data[i] == 1:
			print(cunt)
			break
		
		if type(data[i]) == type([]) and len(data[i]) > 0:
			cunt += 1
			run(data[i], cunt)
			cunt -= 1

def run2(my_dict, cunt):
	for key in my_dict.keys():
		if my_dict[key] == []:
			print(f'duck is {cunt} deep')
			break

		elif my_dict[key] == type(my_dict):
			cunt += 1
			run2(my_dict[key], cunt)
			cunt -= 1

if __name__ == '__main__':
	cunt = 0
	data = [[],[[],[[],[[1]]]],[[],[]],[],[],[],[[],[]]]
	run(data, cunt)

	my_dict = {'duck' : [] ,'goos' : {'goos1' : {'goos2' : {'num':1}, 'goos3' : {'num':1}}, 'goos4' : {'goos5' : {'num':1}}}}
	run2(my_dict, cunt)