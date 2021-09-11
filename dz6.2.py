1.lambda x, y: x**2 + y**2

2.(1)lambda animal: len(animal)

2.(2)string = 'Hello'
print(lambda string: len(string))


3.list(map(float, ["12", "5", "3"]))
[12, 5, 3]

list(map(int, ["12", "5", "3"]))
[12, 5, 3]


4.def more_10(n):
    return n > 10

5.(1)list_of_str = ['hello', 'apple', 'amigo']
list_of_str = list(map(lambda elem: elem.replace(a, ''), list_of_str))
print(list_of_str)

5.(2)lst = ['hello', 'apple', 'amigo']
removed = lst.replace("a", "")
print(lst)


6.(1)list_of_words = ['one', 'two', 'list', '', 'dict']
list(filter(lambda x: len(x) > 4, list_of_words))

6.(2)list_of_words = ['one', 'two', 'three']
[word for word in list_of_words if len(word) > 4]