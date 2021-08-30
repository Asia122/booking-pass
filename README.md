# Booking Pass

## Introduction

Booking-pass is a software development project that allows users to book the COVID-19 vaccine and know if he/she has the GreenPass or not. 

Given a username and a password, the program allows users to access different sections based on their roles. Username, password and roles are registered in the database *access_db.db.*

## Files

### ***access_db.db***

The *database access_db.db* contains two tables: one named *user* containing username and encoded password and one named *user_role* containing the usernames and their role. The two tables are connected through the variable username since it is the primary key of both tables and works as a foreign key in *user_role.* Therefore it is impossible to add new users in the table *user_role* if they are not already present in the table *user.*

### ***people_vaccinated.csv***

The CSV file *people_vaccinated.csv contains the list of all vaccinated people. The variables are Fiscal Code, Name, Surname, Gender, Date of birth, Place of Birth and Date of the first shot. This file will be used by doctors to add new vaccinated patients and by restaurateurs to check if customers have the green pass.

### ***registry_codes.csv***

The CSV file *registry_codes.csv* contains the list of the Italian cities with their relative code and acronym. This file is used to generate the fiscal code.

### ***access_db.py***

The module *access_db.py* contains the functions used to access the database db_password.db and modify it. The function *check_for_username_correct()* takes as input username and password. It is used to verify that the username and password given as input to the program are contained in the database *access_db* and gives as output the role of the user. The function *save_new_username_correct()* takes as input username password and role. It allows the admin to add new users to the database or to correct the data of one of the existing ones. This module also contains the function *parse_args* which defines the arguments needed to run the program.

### ***visualize.py***

The module *visualize.py* contains the functions which allow users to visualize data stored in the database *password_db.db* and in the dataset *people_vaccinated.csv*. The function *print_all_users()* gives the list of all the users present in the database and their role, *vaccinated_people()* takes as input the CSV dataset and allows to visualize the data contained. Finally, *print_info* allows getting all the data of a patient contained in *people_vaccinated.csv* given its fiscal code and the database.

### ***checker.py***

The module *checker.py* focuses on checking if a person has the GreenPass or not. To establish it, the date of the vaccination must be checked. If 15 days have passed from that date, (including the 15th day) the user has the GreenPass, otherwise not.

This information is accessible only to the restaurateur. In order to do that, the function *check_green_pass()* is used. First of all, it has to be checked if the user is present in the CSV file people_vaccinated using the function *check_fiscalcode()*.

If not, it means it doesn't even have the reservation for the vaccination.

- if nperson_date + 15 days = today --> YES GreenPass
- if nperson_date + 15 days < today --> YES GreenPass
- if nperson_date + 15 days > today --> NO GreenPass

### ***fiscal_code.py***

The module *fiscal_code.py* has 7 functions that together calculate the Italian Fiscal Code. The principal function is *fiscal_code_calculator()* that recalls and merges all the other functions returning all the small parts of the final fiscal code. The principal function is the one that if is called and passed name, surname, date of birth, gender, and place of birth will return the string containing the Italian Fiscal Code. The other functions are:

- *get_surname_letters() - returns the first 3 letters of the Italian fiscal code as string;*
- *get_name_letters() - returns the second 3 letters of the Italian fiscal code as string;*
- *consonants_counter() - returns the number of consonants in a word;*
- *get_birth_data() - returns an alphanumeric string that represents the part of the Italian fiscal code derived by the date of birth of the person.*
- *get_place_data() - returns the Belfiore code used in the cadastral code which comprises one letter, then three digits;*
- *get_control_char() - given the first 15 characters of the fiscal code, can return the control character. This letter is determined as follows:*
    - *the 8 odd characters are set apart; the same thing for the 7 even ones;*
    - *every single character converted into a numeric value;*
    - *all the values are to be added, the final result has to be divided by 26;*
    - *the remainder will give the last character.*

### ***adder.py***

The module adder*.py has the* purpose of letting doctors append inside the dataset *people_vaccinated.csv* the personal information of new people. Name, Surname, Gender, Date of birth, Place of Birth, fiscal code (if not given by the user, is automatically calculated calling the external function *fiscal_code.py)*  and finally the vaccination date, chosen by the doctor or suggested by the software, are all stored in a new line of people_vaccoinated.csv.

### ***booking.py***

The module *booking.py* contains the functions that, working together, enables to choose and return a suitable date for the vaccination. There are 3 functions that work together once the *select_date()* function is called in *adder.py*.
The function *select_date()*, through the use of *availability_entire_year()* shows the available days to book closest to the current day up to 2 months and let the user choose one. A date is considered available till a max of three people are booked.
If the entire year is booked it will show the available days of January of the next year. 

### ***main.py***

The module *main.py* recalls all the functions needed to run the program. Based on the argument selected by the user it allows to perform different actions. The arguments -c (username) and -p (password) are always mandatory and are checked by the function *check_for_username_correct()*. The other arguments are -l, -d and -f which usage will be defined later on in this paper.

## Installation

Access to the command prompt of your pc and paste:

```bash
git clone [https://github.com/Asia122/booking-pass](https://github.com/Asia122/booking-pass)
```

You will automatically download the folder containing all the modules and the files needed to run the program. Git should have been previously installed on the machine.

## Functionalities

The program, based on the arguments given, username and password, allows access to different sections. The mandatory arguments are -c and -p are mandatory arguments that take as input the username (-c) and password (-p). Username and password refer to a precise user stored in the database *access_db.db* who, depending on the role, can do various things. Indeed -l, -d and -f is not mandatory and allow only data visualization.

Now let’s see what users can do based on their role.

### **Admin**

The admin, using the arguments -c and -p, can add new users to the database *access_db.db.*

If you access the folder booking-pass from your prompt and you write:

```bash
python main.py -c Nicole00 -p Lab2021
```

The program will allow you to add a new user to the database or modify an existing one as follows:

```bash
You are an admin, being an admin you can add new users to the database or modify an old one
Do you want to add a new user? Type y or n: y
Tell me the username: Test_doctor
Tell me the password: Git2021
Tell me the role (admin, doctor or restaurant): doctor
```

Using the arguments -l, -c and -p the admin can visualize all the users of the database *access_db.db* and their role*.*

This time if you write on your prompt:

```bash
python main.py -l  -c Nicole00 -p Lab2021
```

You will get the following output:

```bash
Users:
Nicole00 admin
AndreaRocco restaurant
LeoProve doctor
AsiaM restaurant
RickyTrabu doctor
MartiF doctor
SabAma01 restaurant
Test_doctor doctor
```

### Doctor

The doctor, using the arguments -c and -p, can introduce data of its patients and get to know if they have already received their first vaccination shot. If not the doctor can check the available dates and find an appointment for its patients. He can book the vaccine for a maximum of 3 people a day.

Let’s see how it works in practice.

Write in your prompt:

```bash
python main.py -c DTest2021 -p h-farm
```

The program will ask you to insert your fiscal code or to give the data needed to calculate it.

To make it possible to calculate it the program will ask you the following data:

```bash
Now you can add new vaccinations
Introduce the Fiscal Code or simply push enter if you want it calculated automatically
Please enter the name -> Paolo
Please enter the surname -> Rossi
Please enter your gender: M or F -> M
Please enter the birthday gg/mm/yyyy-> 15/10/1964
Please enter the birthplace -> Padova
```

At this point, you can tell the program if the patient has already taken the first shot or if you did not.

If he/she has already taken the first shot the program will only ask you the date of the first shot and add the patient to *people_vaccinated.csv* otherwise it will guide you throughout the booking process.

It will firstly show the available dates in the next month from which you are asked to choose a date as follows and then it will proceed with the registration of the reservation in *people_vaccinated.csv:*

```bash
26/09/2021
27/09/2021
28/09/2021
29/09/2021
30/09/2021
select one of the available vaccination dates
input the year 2021
input the month 09
input the day 27
You successfully registered Paolo Rossi 's vaccination date!
```

Now use the arguments -d, -c and -p.

```bash
python main.py -d -c DTest2021 -p h-farm
```

The users registered as doctors can visualize all the data contained in the dataset people_vaccinated.csv.

```bash
Now you can see by yourself if fiscal code is present in our database manually
				 Fiscal Code        Name     Surname Gender Date of Birth                 Place of Birth Date First Shot
0   FRRNDR82T16A001X      Andrea     Ferrari      M    16/12/1982                    Abano Terme      03/09/2020
1   RSSFNC23C14A007C   Francesco       Rossi      M    14/03/1923                      Abbasanta      12/01/2021
2    FRRLSN52H5A017P  Alessandro    Ferretti      M    05/06/1952                      Accettura      09/02/2021
3   MNTMTT23C23A027C      Matteo     Montana      M    23/03/1923                     Aci Catena      06/07/2020
4    DVLLCU79A2A054L        Luca      Davoli      M    02/01/1979                          Acuto      07/09/2021
5   CTLLNZ55L18A047S     Lorenzo   Catellani      M    18/07/1955               Acquaviva Picena      07/04/2021
6   BNCMRC68E30A058X       Marco    Bonacini      M    30/05/1968               Adrara San Rocco      22/09/2021
7   TTIDVD19P12B873Q      Davide       Iotti      M    12/09/2019                      Casalduni      09/12/2021
8   MNZSMN26R22B879V      Simone     Menozzi      M    22/10/1926                Casale sul Sile      12/12/2020
9   CRRGPP19D17B888F    Giuseppe   Corradini      M    17/04/2019             Casaletto Spartano      26/11/2021
10  RIONTN81C14B886F     Antonio        Iori      M    14/03/1981                      Casaleone      01/05/2021
11  FNTRCR89L20B892S    Riccardo     Fontane      M    20/07/1989                 Casalfiumanese      29/08/2020
12  BRBMTT20M23B893A      Mattia    Barbieri      M    23/08/1920                    Casalgrande      02/12/2021
13  BRTLSS73H13B890R     Alessio     Bertani      M    13/06/1973             Casaletto di Sopra      02/05/2021
14   MGNFRC66R7H294J    Federico     Magnani      M    07/10/1966                         Rimini      25/09/2021
15  SPGGNN58P11H305D    Giovanni   Spaggiari      M    11/09/1958                     Rio Marina      25/08/2020
16  SSSGRL95A31H300I    Gabriele       Sassi      M    31/01/1995                      Riofreddo      10/06/2021
17   BRTMHL44T9H301Z     Michele    Bertolin      M    09/12/1944                    Riola Sardo      21/12/2020
18   BGIDNL69B8E238N     Daniele        Bigi      M    08/02/1969                   Guardamiglio      08/10/2020
19  BRGSFN05M10E239F     Stefano      Borghi      M    10/08/2005                    Guardavalle      16/11/2020
20  GDTLRD82A27E241E    Leonardo    Guidetti      M    27/01/1982                        Guardea      01/08/2021
21   SLSNCL09E1E245F      Nicola       Salsi      M    01/05/2009               Guardia Lombardi      15/08/2020
22  FRNSVT26D24E246Y   Salvatore  Fornaciari      M    24/04/1926              Guardia Perticara      19/10/2020
23   BRGMNL25S1E242Q    Emanuele     Braglia      M    01/11/1925             Guardia Piemontese      08/09/2021
24  HUXLSS77S62E249C     Alessia          Hu      F    22/11/1977            Guardia Sanframondi      04/08/2021
25  RLNCHR78B41E243U      Chiara   Orlandini      F    01/02/1978                   Guardiagrele      10/04/2020
26  PRNMTN01A68E244Z     Martina      Prandi      F    28/01/2001                  Guardialfiera      29/10/2020
27  SPSGLI82E47E248K      Giulia    Esposito      F    07/05/1982                   Guardiaregia      15/04/2020
28  VZZSRA82M60E337F        Sara     Vezzani      F    20/08/1982                        Isnello      09/08/2021
29  BRTFNC15R71E338H   Francesca     Bartoli      F    31/10/2015                   Isola D'Asti      01/03/2020
30  CHNFRC87A71E341S    Federica        Chen      F    31/01/1987              Isola Del Cantone      10/09/2021
31  BNOGRG74P46E348H     Giorgia        Boni      F    06/09/1974               Isola Del Giglio      05/01/2020
32  VCCLCA65S44E343W       Alice      Vecchi      F    04/11/1965  Isola Del Gran Sasso D'Italia      10/05/2020
33  GRSNNA92M67E317O        Anna      Grassi      F    27/08/1992                         Inzago      22/01/2021
34  SNCLSE31E70E321R       Elisa     Soncini      F    30/05/1931                         Ionadi      16/12/2021
35  SNGSFO42A49G088A       Sofia       Singh      F    09/01/1942                      Orbetello      22/07/2020
36  BDGVNT84C49G089L   Valentina    Bedognin      F    09/03/1984              Orciano Di Pesaro      08/10/2020
37  FRRLNE94D55G090K       Elena       Ferri      F    15/04/1994                 Orciano Pisano      24/06/2021
38  CDLRRA09L51D522B      Aurora   Codeluppi      F    11/07/2009                   Orco Feglino      10/12/2021
39  RNLRNN17P43M266E     Arianna     Rinaldi      F    03/09/2017                         Ordona      22/05/2020
40  LSGLRI87R48G093O      Ilaria     Lasagni      F    08/10/1987                          Orero      11/03/2020
41  BNSGDI27H46G095T       Giada     Benassi      F    06/06/1927                        Orgiano      19/12/2020
42  FNTLSN26M71G383K  Alessandra     Fantini      F    31/08/1926             San Nicolo' Gerrei      17/09/2020
43  PNCLRA59D67I066S       Laura   Panciroli      F    27/04/1959        San Pancrazio Salentino      09/11/2021
44  PCCBRC05B63G407U    Beatrice   Piccinini      F    23/02/2005                      San Paolo      31/08/2020
45  BNNSLV61B62B906K      Silvia      Bonini      F    22/02/1961             San Paolo Albanese      10/03/2020
46  RSSMRA71R64I135T       Maria       Russo      F    24/10/1971            San Quirico D'Orcia      06/10/2020
47  SMNLNR04L61I136D    Eleonora   Simonazzi      F    21/07/2004                    San Quirino      06/12/2020
48  CMPGAI56E58F713N        Gaia     Campani      F    18/05/1956                       Morbello      20/03/2020
49  CSNNCL00H51A703P      Nicole    Cusinato      F    11/06/2000             Bassano del Grappa      28/06/2021
50  TRBRCR00L30L407M    Riccardo    Trabucco      M    30/07/2000                        Treviso      09/08/2021
51  MRTSAI99B52C957F        Asia     Martini      F    12/02/1999                     Conegliano      03/07/2021
52  RCCNDR00T29G888M      Andrea       Rocco      M    29/12/2000                      Pordenone      17/09/2021
53  PRVLRD00R21F839H    Leonardo  Provenzano      M    21/10/2000                         Napoli      29/05/2021
54  MLNSLL00T54B157E    Isabella       Molon      F    14/12/2000                        Brescia      26/09/2021
55  MDASRN76H64C743Q     Sabrina      Amadio      F    24/06/1976                     Cittadella      15/08/2021
56  RSSPLA64R15G224Q       Paolo       Rossi      M    15/10/1964                         Padova      27/09/2021
```

Finally, use the arguments -f, -c and -p:

```bash
python main.py -f -c DTest2021 -p h-farm
```

The users registered as doctors can visualize the patients' contained in the dataset *people_vaccinated.csv* given their fiscal code.

```bash
Insert the Fiscal Code:RSSPLA64R15G224Q
RSSPLA64R15G224Q is the fiscal code of Paolo Rossi whose first dose date is 25/09/2021
```

### Restaurant

The restaurant using the arguments -c and -p can check if the client has the green pass or not.

```bash
python main.py -c Test_restaurant -p Pippo
```

The program will ask the user restaurant to give the fiscal code of the client as input and will return if it has the green pass or not as follows. 

```bash
Check if a person has the greenpass giving the Fiscal Code: RSSPLA64R15G224Q
RSSPLA64R15G224Q doesn't have the Green Pass yet.
```

## Authors

- Cusinato Nicole
- Martini Asia
- Provenzano Leonardo
- Rocco Andrea
- Trabucco Riccardo
