
import random;
import numpy;

# 1.(12)Есть натуральное двузначное число n. Верно ли, что среди его цифр есть 1 или 9?

varX=random.randint(10,99);
varY=list(str(varX));

for i in range(len(varY)):
    if varY.count("1")== 0 and varY.count("9")== 0:
        print(f"Чисел 1 и 9 в числе {varX} не имеется!!");
        break;
    elif int(varY[i]) == 1:
            print(f"Имеется число {int(varY[i])} в числе {varX}");
    elif int(varY[i])== 9:
        print(f"Имеется число {int(varY[i])} в числе {varX}");

print ("\n");


#2.(12)
b=0.5;
m=8;
a=2.4*(10**2);
j=(1.7,2.9,8);

for i in range(len(j)):
    y = (m-b)/(numpy.sin(a -(numpy.e**a)));
    z=3*y+numpy.sqrt(a-(4*j[i]*b));
    print(z);

print("\n")
j=2;
while j<=3:
    y = (m - b) / (numpy.sin(a - (numpy.e ** a)));
    z = 3 * y + numpy.sqrt(a - (4 * j * b));
    print(z);
    j+=0.5;


print("\n");
m=(0.4,-1,1.9);
b=2

for i in range(len(m)):
       while b <= 3:
        y = (m[i] - b) / (numpy.sin(a - (numpy.e ** a)));
        z = 3 * y + numpy.sqrt(a - (4 * j * b));
        b+=0.5;
        print(z);

#3. (4) Фирма ежегодно на протяжении n лет закупала оборудование стоимостью соответственно s1, s2, ...,
# sn pублей в год (эти числа вводятся и обрабатываются последовательно).
# Ежегодно в результате износа и морального старения (амортизации)
# все имеющееся оборудование уценивается на р%. Какова общая стоимость накопленного оборудования за n лет?

print("\n");
varAge = 2020 - int(input("Введите год с которого производить подсчеты: "));
initialCost=[]; #начальная стоимость оборудования
const_reductionInPrice=5; #амортизация %
residualValue=[]; #окончательная стоимость с учетом амортизации
for i in range(varAge):
     x=0;
     initialCost.append(input("Введите первоначальную стоимость оборудования №" +str(i+1)+": "));
     x=const_reductionInPrice *(varAge-i);
     residualValue.append(int(initialCost[i])-((int(initialCost[i])/100)*x));


sumResult = sum(residualValue); #общая сумма стоимости всего оборудования (с учетом амортизации)
print(f"общая сумма стоимости всего оборудования (с учетом амортизации) = {sumResult}");

print("\n");

#4.(12) Найти номер минимального элемента списка.
varSizeArray = int(input("Введите размер списка: "));
array = [];

for i in range(varSizeArray):
    array.append(random.randint(0,99));

minElement=array[0];
numberMinElement=0;
for i in range(len(array)):
    if array[i]<minElement:
        minElement=array[i];
        numberMinElement=i;

print(array);
print(f"Значение минимального элемента составляет = {minElement}, с номером = {numberMinElement}");


