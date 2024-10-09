mkdir lab0
cd lab0
mkdir doduo4 golurk6 mantine6 
touch graveler5  quilava7 shroomish6
cd doduo4
mkdir alakazam bulbasaur dwebble vanillite
touch phanpy ferrothorn
cd ..
cd golurk6
mkdir starly geodude
touch klinklang magcargo cinccino
cd ..
cd mantine6
mkdir typhlosion flygon magikarp 
touch forretress cascoon clefable 
cd ..
cd doduo4
echo -e "Способности Landslide Pickup Frisk\n" > phanpy
echo -e "тип диеты\nPhototroph Terravore\n" > ferrothorn
cd .. 
cd golurk6 
echo -e "weigth=178.6 height=24.0 atk=10\ndef=12\n" > klinklang
echo -e "Развитые способности Weak Armor\n" > magcargo
echo -e "Ходы\nAfter You Aqua Tail Bullet seed != Covet Gunk Helping Hand != Hyper\nVoice Iron Tail Knock Off Last Resort Rock Blast != Seed Bomb Sing !=\nSlepp Talk Snore Tail Slap!= Tickle!= Uproar\n" > cinccino
cd ..
echo -e "Возможности\nOverland=7 Borrow=4 Power=3 Intelligence=2 Groundshaper=0\n Sinker=0\n" > graveler5
cd mantine6
echo -e "Способности Selfdestruct Bug Bite Take Down\nRapid Spin Bide Natural Gift Spikes Mirror Shot Autotomize Payback\nExplosion Iron Defense Gyro Ball Double-Edge Magnet Rise Zap Cannon\nHeavy Slam\n" > forretress
echo -e "Тип диеты Nullivore\n" > cascoon
echo -e "Живет Cave\nMountain\n" > clefable
cd ..
echo -e "Способности Smokescreen Ember Quick Attack Flame\nWheel Defense Curl Swift Flame Charge Lava Plume Flamethrower Inferno\nRollout Double-Edge Eruption\n" > quilava7
echo -e "Возможности Overland=4\nSurface=2 Jump=2 Power=1 Intelligence=3\n" > shroomish6
chmod 770 doduo4
cd doduo4
chmod 551 alakazam
chmod -wxrw---x bulbasaur
chmod 752 dwebble
chmod 404 phanpy
chmod r-----r-- ferrothorn
        chmod: invalid file mode: r-----r--
        решение: chmod 752 ferrothorn или chmod u=rwx,g=rx,o=w ferrothorn
        обсуждение:
        u=rwx: Владелец (user) получает права на чтение (r), запись (w) и выполнение (x).
        g=rx: Группа (group) получает права на чтение (r) и выполнение (x). 
        o=w: Остальные (others) получают право только на запись (w).

cd ..
chmod 305 golurk6
cd golurk6
chmod  rw--w--w- klinklang
    chmod: invalid file mode: rw--w--w-
    решение: chmod 622 klinklang
chmod 700 geodude
chmod 444 graveler5
chmod 571 mantine6
chmod 444 forretress
chmod 737 typhlosion
chmod 044 cascoon
chmod 357 flygon
chmod 736 magikarp
cd ..
chmod 006 quilava7
chmod 440 shroomish6
cat lab0/golurk6/magcargo lab0/mantine6/forretress > lab0/graveler5_57
    cat: lab0/golurk6/magcargo: Permission denied
    решение:
        chmod 777  lab0/golurk6/magcargo
        chmod 777  lab0/mantine6/forretress
cp lab0/quilava7 lab0/doduo4/ferrothornquilava
    cp: lab0/quilava7: Permission 
    решение:
        chmod 777 lab0/quilava7
cp lab0/graveler5 lab0/mantine6/flygon/
ln -s shroomish6 lab0/golurk6/magcargoshroomish
cp -r lab0/golurk6/* lab0/golurk6/geodude/
    cp: lab0/golurk6/cinccino: Permission denied
    cp: lab0/golurk6/magcargoshroomish: No such file or directory
    решение:
        chmod 777 lab0/golurk6/cinccino
        Ошибка возникает потому, что символическая ссылка lab0/golurk6/magcargoshroomish указывает
        на несуществующий файл. Это нормально для символических ссылок, если целевой файл был удалён
        или перемещён.
        -L заставит cp следовать символическим ссылкам и копировать их целевые файлы, если они существуют.
        -P (по умолчанию) скопирует символические ссылки как ссылки, а не как их содержимое.
        cp -r -P lab0/golurk6/* lab0/golurk6/geodude/
ln -s lab0/golurk6 lab0/Copy_81
ln lab0/shroomish6 lab0/mantine6/cascoonshroomish
//3 - закончили здесь.
cat mantine6/* 2>/tmp/mantine6_errors.log | wc -m > /tmp/mantine6_char_count.txt
cat /tmp/mantine6_char_count.txt   
    вывод: 
        275
cat /tmp/mantine6_errors.log
    вывод:
        cat: mantine6/cascoon: Permission denied
        cat: mantine6/flygon: Permission denied
        cat: mantine6/magikarp: Is a directory
        cat: mantine6/typhlosion: Is a directory
cd lab0
ls -lSr mantine6
    вывод:
    total 8
    drwx-wxrwx  2 s465676 studs   2 25 сент. 16:46 typhlosion
    drwx-wxrw-  2 s465676 studs   2 25 сент. 16:46 magikarp
    d-wxr-xrwx  2 s465676 studs   3 25 сент. 21:00 flygon
    -r-----r--  1 s465676 studs  26 25 сент. 19:10 clefable
    ----r--r--  1 s465676 studs  29 25 сент. 19:08 cascoon
    -r--r-----  2 s465676 studs  74 25 сент. 19:14 cascoonshroomish
    -rwxrwxrwx  1 s465676 studs 202 25 сент. 19:07 forretress
cd ..

ls -R lab0 | grep 'e$' | xargs cat 2>> /tmp/lab0_errors.log | nl | sort
cat /tmp/lab0_sorted_output.txt
    вывод:
     1	Живет Cave
     2	Mountain
cat /tmp/lab0_errors.log
    вывод:
        find: lab0/doduo4/bulbasaur: Permission denied
        find: lab0/mantine6/flygon: Permission denied
ls -lR  2>&1 | grep -v '^total' | sort | tail -n 3
    вывод:
        lrwxr-xr-x  1 s465676 studs  12 25 сент. 21:13 Copy_81 -> lab0/golurk6
        ls: lab0/doduo4/bulbasaur: Permission denied
        ls: lab0/mantine6/flygon: Permission denied
ls -1 golurk6 2>/tmp/golurk6_errors.log | sort
    вывод:
        cinccino
        geodude
        klinklang
        magcargo
        magcargoshroomish
        starly
ls -lR 2>&1 | grep '^f' | sort -k6,7
    вывод:
        ls: lab0/doduo4/bulbasaur: Permission denied
        ls: lab0/mantine6/flygon: Permission  denied
        lab0/mantine6/flygon:
        ls: lab0/mantine6/flygon: Permission denied
        total 0
        -rwxr-x-w-  1 s465676 studs  40 25 сент. 16:42 lab0/doduo4/ferrothorn
        -rwxr-xr-x  1 s465676 studs 160 25 сент. 20:57 lab0/doduo4/ferrothornquilava
        -rwxrwxrwx  1 s465676 studs 202 25 сент. 16:47 lab0/mantine6/forretress
rm lab0/graveler5
    ошибка права доступа:
        override r--r--r-- s465676/studs uarch for lab0/graveler5?
    решение:
        chmod 777 lab0/graveler5
rm lab0/golurk6/klinklang
rm lab0/golurk6/magcargoshroomi
rm lab0/mantine6/cascoonshroomi
    ошибка права доступа:
        override r--r----- s465676/studs uarch for lab0/mantine6/cascoonshroomish?
    решение:
        chmod 777 lab0/mantine6/cascoonshroomi*
rmdir lab0/doduo4
    ошибка права доступа:
        rmdir: lab0/doduo4: Directory not empty
        rm: lab0/doduo4/bulbasaur: Permission denied

    решение:
        chmod 777 lab0/dodu4/bulbasaur
         rm -rf lab0/doduo4
rmdir lab0/doduo4/bulbasaur
    ошибка права доступа:
        rmdir: lab0/doduo4/bulbasaur: No such file or directory
    объяснение: 
        lab0/doduo4/bulbasaur 
        директория находилось в doduo4 а до перед этим действием мы удалили директория со всеми его файлами.
