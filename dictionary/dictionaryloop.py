fav_language={"masum":"C++","amir":"Java","moon":"python"}
my_list=["masum","C++","amir","java",]
for name ,language in fav_language.items():
	print(name.upper() + "'s favourit language is " + language + ".")

for name in fav_language.keys():
	print(name.title())
for language in fav_language.values():
	print(value.title())
if my_list in fav_language:
	print("True")
else:
	print("False") 
