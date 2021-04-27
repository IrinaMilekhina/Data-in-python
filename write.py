my_file = open('sample.txt', 'r').read()
# при флаге 'w' файл будет создан, если его не было
ff = open('copy.txt', 'w')
ff.write(my_file)
ff.close()

# файл уже создан, но при открытии он очистится
ff = open('copy.txt', 'w')
ff.close()

# снова наполним файл данными
ff = open('copy.txt', 'w')
ff.write(my_file)
ff.close()

# при флаге 'x' поймаем исключение FileExistsError, т.к. файл уже существует
ff = open('copy.txt', 'x')
ff.close()

# при флаге 'a' файл успешно откроется на дозапись
