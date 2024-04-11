# მომხმარებელს შეეკითხეთ თუ რომელ პროგრამირების აკადემიაში სწავლობს. თუ პასუხი იქნება "GOA", დაუბეჭდეთ რომ სწორია. სხვა შემთხვევაში დაუბეჭდეთ, რომ არასწორი გადაწყვეტილება მიიღო.
academy = input("In which programming academy do you study?")
if academy == "GOA":
    print("true")
else:
    print("false")

# მომხმარებელს შემოატანინეთ საყიდელი ნივთის ფასი და მისი ბიუჯეტი. თუ ბიუჯეტი აღემატება ან ტოლია საყიდელი ნივთის ფასის, დაუბეჭდეთ რომ თანხა ყოფნის. სხვა შემთხვევაში, დაუბეჭდეთ თუ რამდენი აკლდება საყიდლად.
price = int(input("what is price? "))
budget = int(input("what is your budget? "))
if budget >= price:
    print("money is enough")
else:
    print(price - budget)
    
# დაწერეთ პროგრამა, რომელიც შეამოწმებს მომხმარებლის მიერ შემოტანილ რიცხვს. თუ რიცხვი მეტია ან ტოლი ხუთის, დაბეჭდეთ მისი ნამრავლი ორზე. სხვა შემთხვევაში დაბეჭდეთ მისი ნამრავლი ოთხზე.
number = int(input("please enter your number"))
if number >= 5:
    print(int(number * 2))
else:
    print(int(number * 4))


# თქვენს პროგრამაში ბილეთის ფასი იქნება 10 ლარი. მომხმარებელს შეეკითხეთ თუ რამდენი ბილეთის ყიდვა უნდა. თუ ეს რიცხვი ნაკლები იქნება 5-ზე, გამოუტანეთ ჩვეულებრივი შედეგი. სხვა შემთხვევაში ყოველ ბილეთზე გააკეთეთ 30%-იანი ფასდაკლება.
price = 10
ticket = int(input("how much ticket do you want"))
if ticket < 5:
    print(price * ticket)
else: 
    print((price * 70 /100) * ticket)
# შექმენით კალკულატორის პროგრამა, სადაც გექნებათ +, -, *, /. მომხმარებელს ჯერ შეეკითხეთ ორი რიცხვი, შემდეგ სასურველი ოპერაცია და ბოლოს დაუბეჭდეთ შედეგი.
number1 = int(input("please enter your first number"))
number2 = int(input("please enter your second number"))
print(number1 / number2)
print(number1 * number2)
print(number1 - number2)
print(number1 + number2)













