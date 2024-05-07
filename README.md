1. models.Animal.objects.all()     
<QuerySet [<Animal: Лев>, <Animal: Скункс>, <Animal: Ужик>, <Animal: Ежик>, <Animal: Карась>, <Animal: Пенгвин>]>

2. models.Animal.objects.first()   
 <Animal: Лев>

3. models.Animal.objects.last()  
<Animal: Пенгвин>

4. models.Animal.objects.count()  
6
 5. models.Animal.objects.order_by('name')  
<QuerySet [<Animal: Ежик>, <Animal: Карась>, <Animal: Лев>, <Animal: Пенгвин>, <Animal: Скункс>, <Animal: Ужик>]>

6. models.Animal.objects.order_by('-name')  
<QuerySet [<Animal: Ужик>, <Animal: Скункс>, <Animal: Пенгвин>, <Animal: Лев>, <Animal: Карась>, <Animal: Ежик>]>

7. models.Animal.objects.order_by('population') 
<QuerySet [<Animal: Ужик>, <Animal: Пенгвин>, <Animal: Лев>, <Animal: Ежик>, <Animal: Скункс>, <Animal: Карась>]>

8. models.Animal.objects.order_by('-population')  
<QuerySet [<Animal: Карась>, <Animal: Скункс>, <Animal: Ежик>, <Animal: Лев>, <Animal: Пенгвин>, <Animal: Ужик>]>

9. models.Animal.objects.filter(name__contains='и') 
<QuerySet [<Animal: Ужик>, <Animal: Ежик>, <Animal: Пенгвин>]>

10. models.Animal.objects.filter(name__contains='У')  
 <QuerySet [<Animal: Ужик>]>

11. models.Animal.objects.filter(name__exact='Лев') 
<QuerySet [<Animal: Лев>]>

12. models.Animal.objects.filter(name__exact='Скунс')  
<QuerySet []>

13. models.Staff.objects.all()  
<QuerySet [<Staff: Кол я>, <Staff: Иванов Иван>]>

14. models.Staff.objects.filter(salary__gt=100) 
<QuerySet [<Staff: Кол я>, <Staff: Иванов Иван>]>

15. models.Staff.objects.filter(salary__gt=50000)  
<QuerySet [<Staff: Кол я>]>

16. models.Staff.objects.filter(salary__lt=50000)  
 <QuerySet [<Staff: Иванов Иван>]>

17. models.Staff.objects.filter(salary__lt=100)
<QuerySet []>
18. models.Staff.objects.filter(salary__lte=90000) 
<QuerySet [<Staff: Кол я>, <Staff: Иванов Иван>]>

19. models.Staff.objects.filter(salary__lt=90000)  
<QuerySet [<Staff: Иванов Иван>]>

20. models.Staff.objects.filter(salary__gte=90000) 
<QuerySet [<Staff: Кол я>]>

21. models.Staff.objects.filter(salary__gt=90000)  
<QuerySet []>

22. models.Staff.objects.latest('date_of_birth') 
<Staff: Кол я>

23. models.Staff.objects.get(id=1)  
<Staff: Кол я>

24. models.Staff.objects.filter(id=3).exists()  
False

25. models.Staff.objects.filter(first_name='Иван').exists()
True

26. models.Animal.objects.create(name='Бобер',population=22)
<Animal: Бобер>

27. models.Animal.objects.filter(id__gt=2).update(is_rare=True)  
5

28. models.Animal.objects.filter(id__gt=2).delete() 
(5, {'core.Animal': 5})

29. models.Staff.objects.dates('date_of_birth', 'day',)  
<QuerySet [datetime.date(1999, 12, 14), datetime.date(2002, 5, 7)]>

30. models.Staff.objects.dates('date_of_birth', 'day',).reverse()  
<QuerySet [datetime.date(2002, 5, 7), datetime.date(1999, 12, 14)]>

31. models.Animal.objects.values('name', 'type')
<QuerySet [{'name': 'Лев', 'type': 'mammal'}, {'name': 'Скункс', 'type': 'mammal'}]>

32. models.Animal.objects.values_list('name', flat=True)  
<QuerySet ['Лев', 'Скункс']>

33. models.Animal.objects.exclude(name__contains='С')
<QuerySet [<Animal: Лев>]>
