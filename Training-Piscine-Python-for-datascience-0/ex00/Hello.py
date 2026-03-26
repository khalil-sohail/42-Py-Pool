ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = 'World!'

list = list(ft_tuple)
list[1] = 'Morocco!'
ft_tuple = tuple(list)

ft_set.remove('tutu!')
ft_set.add('Benguerir!')
ft_dict["Hello"] = '1337Benguerir!'

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
