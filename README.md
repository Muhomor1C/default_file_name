# default_file_name

<p><a href="#anchor1">Russian</a></p>
<p><a href="#anchor2">Polski (automatyczne tłumaczenie)</a></p>
<p><a href="#anchor3">English (automatic translation)</a></p>


<p id="anchor1"></p>
<h2>Russian</h2>
<p>
Задача:
Создать функцию для автоматической генерации имени файла для "ленивых" пользователей с возможностью сохранять несколько файлов под условно одним именем.
Предусмотреть возможность создания имен для копий

Логика работы: 

<em><strong>1. При сохранении нового файла</strong></em>, пользователю предлагается имя по умолчанию - "My book".
  Если такое имя уже существует, то в конец ему  добавляется индекс в скобках. Например - <strong>My book(1)</strong> При этом, если файлы с индендексом
  уже существуют, то находится индекс последнего и увеличивается на 1. То же самое происходит с именем введенным пользователем вручную.
  
  <em><strong>2. При копировании файла</strong></em>, предлагается имя копируемого, в начало которого добавлена
  строка "Copy(N)", где N - номер копии. Например: <strong>Copy(1)My book</strong> Если у этого файла уже существуют копии, то находится
  номер последней и увеличивается на 1.
  
  Дополнительные возможности - по имени копии можно отследить всю цепочку копирования, что помогает службе поддержки в случае "потери" пользователем оригинала.
  
  Вся работа производится в двух функциях:
  
  <em><strong>up_version()</strong></em> - получает желаемое имя, создает шаблон для проверки на наличие подобных и генерирует новое имя
        
  <em><strong>find_index()</strong></em> - находит номер последнего файла или копии

Вся остальная обвязка - интерфейс для проверки работы.

Выполнено по заказу https://www.tellity.com/ Опубликовано с их разрешения
</p>

<p id="anchor2"></p>
<h2>Polski</h2>
<p>
Zadanie:
Utwórz funkcję automatycznego generowania nazwy pliku dla" leniwych " użytkowników z możliwością zapisywania wielu plików pod warunkowo jedną nazwą.
Zapewnić możliwość tworzenia nazw dla kopii

Logika pracy:

<em><strong>1. Podczas zapisywania nowego pliku</strong></em>, użytkownik otrzymuje domyślną nazwę - "My book".
Jeśli taka nazwa już istnieje, indeks w nawiasach jest dodawany na końcu. Na przykład - <strong>My book(1)</strong > jeśli pliki z indendexem
już istnieje, to jest indeks tego ostatniego i zwiększa się o 1. To samo dzieje się z nazwą wprowadzoną ręcznie przez użytkownika.

<em><strong>2. Podczas kopiowania pliku</strong> </em>, nazwa kopiowanego pliku jest sugerowana, na początku której dodawana jest linia "Copy(N)", gdzie N jest numerem kopii. Na przykład: <strong>Copy(1)My book</strong> Jeśli ten plik ma już kopie, to jest ostatni numer i jest zwiększany o 1.

Dodatkowe funkcje-nazwa kopii może śledzić cały łańcuch kopiowania, co pomaga zespołowi wsparcia w przypadku" utraty " oryginału przez użytkownika.

Cała praca odbywa się w dwóch funkcjach:

<em><strong>up_version()</strong></em > - pobiera żądaną nazwę, tworzy szablon do sprawdzania podobnych i generuje nową nazwę

<em><strong>find_index()</strong ></em > - wyszukuje numer ostatniego pliku lub kopii

Cała reszta uprzęży to interfejs do sprawdzania działania.

Wykonane na zamówienie https://www.tellity.com / opublikowane za ich zgodą
</p>

<p id="anchor3"></p>
<h2>English</h2>
<p>
Task:
Create a function for automatic file name generation for "lazy" users with the ability to save multiple files under conditionally the same name.
Provide for the possibility of creating names for copies

The logic of work:

<em><strong>1. When saving a new file</strong></em>, the user is offered a default name - "My book".
If such a name already exists, then an index in parentheses is added to the end of it. For example - <strong>My book(1)</strong> At the same time, if the files with the index
if they already exist, then the index of the latter is found and increases by 1. The same happens with the name entered by the user manually.

<em><strong>2. When copying a file</strong></em>, the name of the copied file is suggested, at the beginning of which the line "Copy(N)" is added, where N is the copy number. For example: <strong>Copy(1)My book</strong> If this file already has copies, then the number of the last one is found and increases by 1.

Additional features - by the name of the copy, you can track the entire chain of copying, which helps the support service in case the user "loses" the original.

All work is done in two functions:

<em><strong>up_version()</strong></em> - gets the desired name, creates a template to check for similar ones and generates a new name

<em><strong>find_index()</strong></em> - finds the number of the last file or copy

The rest of the binding is an interface for checking the operation.

Made to order https://www.tellity.com / Published with their permission
</p>


