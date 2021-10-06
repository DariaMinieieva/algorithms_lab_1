# Звіт
## Лабораторна робота №1
Мінєєва Дар’я

### Опис постановки задачі та експерименту:
Порівняти ефективності роботи алгоритмів сортування (selection sort, insertion sort, merge sort та shell sort) на вхідних даних різного типу (масив рандомізованих елементів, масив із відсортованими елементами, масив із відсортованими елементами у зворотньому порядку, масив з елементами з множини {1, 2, 3}) та різного розміру (від 2^7 до 2^15 елементів). До уваги береться кількість порівнянь елментів масивів та час сортування.

### Специфікація комп’ютера: 
* Операційна система: Linux Manjaro
* Кількість ядер: 4
* Татова частота: min/max: 400/3100 MHz
* Пам’ять: 12 GiB


### Сортування на випадковим чином згенерованих масивах

![First](/image/Comp_rand.png)
Даний графік демонструє кількість порівнянь, необхідну для кожного з чотирьох алгоритмів для сортування масиву випадкових значень. Можна зробити висновок, що найкращим алгоритмом в даному випадку є merge sort, а найгіршим - selection sort. Не набагато гірше за сортування злиттям пряцює shell sort, але, як видно з графіку, зі збільшенням кількості елементів у масиві, його складність зростає стрімкіше за merge sort.

![Second](/image/Time_rand.png)
Складність по часу сортування на рандомізованих масивах, за своєю поведінкою, подібна до кількості порівнянь, найкращим та найгіршим алгоритмом для сортування залишаються merge sort та selection sort відповідно.

### Сортування на відсортованих масивах (найкращий випадок)

![Third](/image/Comp_sorted.png)
При сортуванні вже відсортованих масивів ситуація змінюється, кількість порівнянь залишається найбільшою у selection sort, але алгоритмом з найменшою кількістю порівнянь стає insertion sort. Merge sort та shell sort, в даному випадку, працюють майже однаково. 

![Forth](/image/Time_sorted.png)
Час роботи алгоритмів на відсортованому масиві асимптотично схожий  до кількості порівнянь, лише на вхідних даних меншої кількості алгоритми поводять себе трохи по-іншому.
На даному етапі можна сказати, що алгоритми, які на перший погляд здаються неефективними (в даному випадку insertion sort) можуть поводити себе набагато краще в граничних випадках, як наприклад в даному випадку.

### Сортування на масивах відсортованих у зворотньому порядку (найгірший випадок)

![Fifth](/image/Comp_unsorted.png)
Розглянемо роботу заданих алгоритмів у найгіршому випадку, коли масив відсортований у зворотньому порядку. Кількість порівнянь selection sort та insertion sort збігається і є найбільшою серед усіх. Найкращим, як і у випадку з рандомізованими даними, є merge sort, після якого йде shell sort.

![Sixth](/image/Time_unsorted.png)
Час сортування відрізняється від попердніх випадків, в даному експерименті insertion sort працює найдовше, а найкще працюють алгоритми merge sort та shell sort.

### Сортування на масивах, що містять елементи з множини {1, 2, 3}

![Seventh](/image/Comp_123.png)
При сортування масиву, що складається з елементів {1, 2, 3} найменшу кількість порівнянь використовують shell sort та merge sort (shell sort працює краще з невеликою різницею). Найбільша кількість порівнянь порібна для алгоритму selection sort.

![Eighth](/image/Time_123.png)
Час роботи у цьому експерименті практично збігається для selection sort  insertion sort, а також для merge sort та shell sort. Загалом алгоритм shell sort працює найкраще серед даних чотирьох для сотування масиву даних з багатьма повторами.

### Загальний висновок

Даний експеритмент показує, що різні алгоритми працюють краще для різних вхідних даних, для масиву з випадковими елментами найкраще підійте merge sort, для масиву відсортованих або майже відсортованих даних - insertion sort, для масиву з едементами відсортованими у зворотньому порядку - найкраще буде застосовувати merge sort, хоча по часу виконання, shell sort, майже не відрізняється, а для масиву, що містить багато повторів - shell sort. 
Також варто зазначити, що ефективність алгоритів, взалежності від вхідних даних, може змінюватись кардинально, як, наприклад є з я insertion sort, який в експерименті з відсортованими даними праює найкраще, на масиві з елементами, відсортованими у зворотноьму порядку - найгірше.

 