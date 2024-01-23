# ------------------------------------------------------------------------------
# -- Osoby fizyczne
# -- -- Użytkownicy
# !! Hasło 'Password1' -> Hash '$2a$12$Kq8RZD3P71OT809kPAK/lOMA6Hph1yx4OFO1lTZ1w3ppfILtOKb2S'
INSERT INTO Users (uuid, password, email, phone_number, is_company, is_admin) VALUES
    (UUID(), '$2a$12$Kq8RZD3P71OT809kPAK/lOMA6Hph1yx4OFO1lTZ1w3ppfILtOKb2S',
        'j.kowalski@gmail.com', '554856995', 0, 0),
    (UUID(), '$2a$12$Kq8RZD3P71OT809kPAK/lOMA6Hph1yx4OFO1lTZ1w3ppfILtOKb2S',
        'a.nowak@gmail.com', '778658998', 0, 0),
    (UUID(), '$2a$12$Kq8RZD3P71OT809kPAK/lOMA6Hph1yx4OFO1lTZ1w3ppfILtOKb2S',
        'p.wisniewski@gmail.com', '445775669', 0, 0),
    (UUID(), '$2a$12$Kq8RZD3P71OT809kPAK/lOMA6Hph1yx4OFO1lTZ1w3ppfILtOKb2S',
        'm.zielinski@gmail.com', '234567890', 0, 0),
    (UUID(), '$2a$12$Kq8RZD3P71OT809kPAK/lOMA6Hph1yx4OFO1lTZ1w3ppfILtOKb2S',
        'k.wozniak@gmail.com', '345678901', 0, 0),
    (UUID(), '$2a$12$Kq8RZD3P71OT809kPAK/lOMA6Hph1yx4OFO1lTZ1w3ppfILtOKb2S',
        'l.kozlowski@gmail.com', '456789012', 0, 0),
    (UUID(), '$2a$12$Kq8RZD3P71OT809kPAK/lOMA6Hph1yx4OFO1lTZ1w3ppfILtOKb2S',
        'z.jankowski@gmail.com', '567890123', 0, 0),
    (UUID(), '$2a$12$Kq8RZD3P71OT809kPAK/lOMA6Hph1yx4OFO1lTZ1w3ppfILtOKb2S',
        'c.szymanski@gmail.com', '678901234', 0, 0),
    (UUID(), '$2a$12$Kq8RZD3P71OT809kPAK/lOMA6Hph1yx4OFO1lTZ1w3ppfILtOKb2S',
        'u.kaczmarek@gmail.com', '789012345', 0, 0),
    (UUID(), '$2a$12$Kq8RZD3P71OT809kPAK/lOMA6Hph1yx4OFO1lTZ1w3ppfILtOKb2S',
        'd.malinowski@gmail.com', '890123456', 0, 0);

# -- -- Pracownicy
# -- -- -- Pobieranie UUID dla nowo utworzonych użytkowników
SET @uuid1 = (SELECT uuid FROM Users WHERE email = 'j.kowalski@gmail.com');
SET @uuid2 = (SELECT uuid FROM Users WHERE email = 'a.nowak@gmail.com');
SET @uuid3 = (SELECT uuid FROM Users WHERE email = 'p.wisniewski@gmail.com');
SET @uuid4 = (SELECT uuid FROM Users WHERE email = 'm.zielinski@gmail.com');
SET @uuid5 = (SELECT uuid FROM Users WHERE email = 'k.wozniak@gmail.com');
SET @uuid6 = (SELECT uuid FROM Users WHERE email = 'l.kozlowski@gmail.com');
SET @uuid7 = (SELECT uuid FROM Users WHERE email = 'z.jankowski@gmail.com');
SET @uuid8 = (SELECT uuid FROM Users WHERE email = 'c.szymanski@gmail.com');
SET @uuid9 = (SELECT uuid FROM Users WHERE email = 'u.kaczmarek@gmail.com');
SET @uuid10 = (SELECT uuid FROM Users WHERE email = 'd.malinowski@gmail.com');

INSERT INTO Workers (FK_User_uuid, name, surname) VALUES
    (@uuid1, 'Jan', 'Kowalski'),
    (@uuid2, 'Anna', 'Nowak'),
    (@uuid3, 'Piotr', 'Wiśniewski'),
    (@uuid4, 'Michał', 'Zieliński'),
    (@uuid5, 'Katarzyna', 'Woźniak'),
    (@uuid6, 'Łukasz', 'Kozłowski'),
    (@uuid7, 'Zbigniew', 'Jankowski'),
    (@uuid8, 'Cezary', 'Szymański'),
    (@uuid9, 'Urszula', 'Kaczmarek'),
    (@uuid10, 'Dariusz', 'Malinowski');

# ------------------------------------------------------------------------------
# -- Przedsiębiorstwa
# -- -- Użytkownicy
# !! Hasło 'Company1' -> Hash '$2a$12$uCqNF2r1V.gb3kNr8p9RFuAOQrsszKNAWDL4kNfUrjTLFenOMhYLi'
INSERT INTO Users (uuid, password, email, phone_number, is_company, is_admin) VALUES
    (UUID(), '$2a$12$uCqNF2r1V.gb3kNr8p9RFuAOQrsszKNAWDL4kNfUrjTLFenOMhYLi',
        'osadowski@osadowski.pl', '601784833', 1, 0),
    (UUID(), '$2a$12$uCqNF2r1V.gb3kNr8p9RFuAOQrsszKNAWDL4kNfUrjTLFenOMhYLi',
        'biuro@bytecom.pl', '608338889', 1, 0),
    (UUID(), '$2a$12$uCqNF2r1V.gb3kNr8p9RFuAOQrsszKNAWDL4kNfUrjTLFenOMhYLi',
        'info@stema-meble.com', '609318800', 1, 0),
    (UUID(), '$2a$12$uCqNF2r1V.gb3kNr8p9RFuAOQrsszKNAWDL4kNfUrjTLFenOMhYLi',
        'bok@hurtowniastyropianu.pl', '513092032', 1, 0),
    (UUID(), '$2a$12$uCqNF2r1V.gb3kNr8p9RFuAOQrsszKNAWDL4kNfUrjTLFenOMhYLi',
        'serwis@boskar.pl', '748530080', 1, 0),
    (UUID(), '$2a$12$uCqNF2r1V.gb3kNr8p9RFuAOQrsszKNAWDL4kNfUrjTLFenOMhYLi',
        'biuro@screensun.pl', '571700076', 1, 0),
    (UUID(), '$2a$12$uCqNF2r1V.gb3kNr8p9RFuAOQrsszKNAWDL4kNfUrjTLFenOMhYLi',
        'biuro@audyt.swidnica.pl', '601160376', 1, 0),
    (UUID(), '$2a$12$uCqNF2r1V.gb3kNr8p9RFuAOQrsszKNAWDL4kNfUrjTLFenOMhYLi',
        'biuro@alustad.com.pl', '508072804', 1, 0),
    (UUID(), '$2a$12$uCqNF2r1V.gb3kNr8p9RFuAOQrsszKNAWDL4kNfUrjTLFenOMhYLi',
        'biuro@bit-kom.pl', '609491099', 1, 0),
    (UUID(), '$2a$12$uCqNF2r1V.gb3kNr8p9RFuAOQrsszKNAWDL4kNfUrjTLFenOMhYLi',
        'biuro@euforino.pl', '691977765', 1, 0);

# -- -- Firmy
# -- -- -- Pobieranie UUID dla nowo utworzonych użytkowników
SET @uuid_c1 = (SELECT uuid FROM Users WHERE email = 'osadowski@osadowski.pl');
SET @uuid_c2 = (SELECT uuid FROM Users WHERE email = 'biuro@bytecom.pl');
SET @uuid_c3 = (SELECT uuid FROM Users WHERE email = 'info@stema-meble.com');
SET @uuid_c4 = (SELECT uuid FROM Users WHERE email = 'bok@hurtowniastyropianu.pl');
SET @uuid_c5 = (SELECT uuid FROM Users WHERE email = 'serwis@boskar.pl');
SET @uuid_c6 = (SELECT uuid FROM Users WHERE email = 'biuro@screensun.pl');
SET @uuid_c7 = (SELECT uuid FROM Users WHERE email = 'biuro@audyt.swidnica.pl');
SET @uuid_c8 = (SELECT uuid FROM Users WHERE email = 'biuro@alustad.com.pl');
SET @uuid_c9 = (SELECT uuid FROM Users WHERE email = 'biuro@bit-kom.pl');
SET @uuid_c10 = (SELECT uuid FROM Users WHERE email = 'biuro@euforino.pl');

INSERT INTO Companies (FK_User_uuid, nip, name, description, address, url) VALUES
    (@uuid_c1, '8842679999', 'OSADOWSKI i Wspólnicy Sp. z o.o.',
        'Firma Osadowski i Wspólnicy Sp. z o.o. powstała w grudniu 2008 r. Od początku roku 2009 po przejęciu Firmy Prywatnej Osadowski jak i po pozyskaniu kapitału poprzez przyjęcie nowego udziałowca, przed Spółką otworzyły się nowe możliwości intensywnego rozwoju. Duży potencjał Spółki stanowi 20 letni dorobek kontaktów handlowych Firmy Prywatnej Osadowski z wieloma firmami z sektora produkcji konstrukcji stalowych.',
        'ul. Westerplatte 68, Świdnica 58-100',
        'http://www.osadowski.pl/'),
    (@uuid_c2, '8842243144', 'BYTECOM',
        'Głównie produkujemy torby z tkaniny PP, torby z materiału nie tkane, torby papierowe, torby poliestrowe, torby PP, torby termiczne, torby PVC, maty plażowe, torby na prezenty, torby reklamowe, torby z sznurkiem, kamizelki i sprzęt, doskonałe wyposażenie, dobre zarządzanie produkcją oraz różnorodne platformy komunikacyjne, co pozwala nam rozwijać się na dłuższą metę. Przeszliśmy audyt BSCI i posiadamy certyfikat ISO9001, co wskazuje, że jesteśmy kwalifikowanym dostawcą. Posiadamy zespół projektowy, dział produkcji i pakowania oraz jesteśmy wyposażeni w kompleksowe urządzenia. Możemy przygotować wizualizację 3D i projekt graficzny zgodnie z materiałami klienta. Dysponujemy zaawansowanymi maszynami drukarskimi, które umożliwiają doskonały druk. Nasi profesjonalni pracownicy, którzy są ściśle szkoleni, potrafią wykonać wyjątkowo delikatne prace krawieckie. Dbamy o każdy etap produkcji. Posiadamy 6-8 profesjonalnych inspektorów. Zawsze przeprowadzamy wstępną, śródczasową i końcową inspekcję wszystkich naszych zamówień, niezależnie od tego, czy są to małe czy duże zamówienia. Wszystkie nasze materiały przechodzą testy na obecność azotanów, test 6P, test Reach oraz test na zawartość ołowiu. Większość naszych materiałów jest eksportowana na rynki europejskie, azjatyckie i amerykańskie.',
        'ul. Kliczkowska 10, 58-100 Świdnica',
        'https://www.bytecom.pl/'),
    (@uuid_c3, '8840000064', 'STEMA',
        'Jesteśmy prężnie rozwijającą się firmą istniejącą na rynku od 1990 r. Wieloletni okres działalności pozwolił nam na zdobycie dużego doświadczenia w sprzedaży rozwiązań biurowych. Naszym atutem jest elastyczność w podejściu do Klienta oraz innowacyjność oferowanych rozwiązań. Stabilny i zaangażowany zespół pracowników o wysokich kwalifikacjach gwarantuje profesjonalizm i stale rosnącą jakość obsługi. Konsekwentnie rozwijamy główny kierunek naszej działalności, którym jest sprzedaż hurtowa i detaliczna mebli biurowych, przede wszystkim krzeseł, foteli oraz różnego rodzaju podstaw i stelaży. Aby sprostać oczekiwaniom naszych Klientów, większość oferowanych przez nas wyrobów posiadamy w naszych magazynach o powierzchni kilku tysięcy metrów kwadratowych. Nieustannie poszukujemy nowych rozwiązań, stale poszerzając naszą ofertę i dbając o wysoką jakość naszych produktów. Współpracujemy również z największymi producentami mebli i krzeseł biurowych co gwarantuje to produkty wysokiej jakości dostosowane do indywidualnych potrzeb każdego użytkownika. Umowy przedstawicielskie zawarte z producentami zapewniają naszym klientom niski poziom cen produktów oraz bezproblemową obsługę serwisową, także w okresie pogwarancyjnym.',
        'ul. Towarowa 22a, 58-100 Świdnica',
        'https://www.stema-meble.com/'),
    (@uuid_c4, '9271771760', 'Hurtownia Styropianu PHU LINGO',
        'Styropian i styrodur XPS oraz płyty PIR stanowią u nas od 2005 roku większy udział w sprzedaży materiałów budowlanych. Sklep Internetowy Hurtownia Styropianu powstał w celu sprzedaży styropianu skierowanej do klientów detalicznych i hurtowych. Zamieszczamy w nim produkty objęte promocją. W ofercie posiadamy także klej do styropianu, siatka do styropianu oraz tynki elewacyjne. Jest także styropapa i papa termozgrzewalna na dachy płaskie i fundamenty. HurtowniaStyropianu.pl',
        'ul. Słotwina 75, 58-100 Świdnica',
        'https://www.hurtowniastyropianu.pl/'),
    (@uuid_c5, '8840012110', 'BOSKAR Sp.j.',
        'Firma BOSKAR jest autoryzowanym sprzedawcą kopiarek Toshiba i Develop.  Prowadzimy serwis sprzętu biurowego W swojej historii posiadaliśmy autoryzację Nashuatec-a, Panasonic-a, Canon a, Sharp-a, Ricoh. Serwisujemy sprzęt kopiarkowy prawie wszystkich marek. Jako autoryzowany partner Hewlett Packard oferujemy Państwu sprzęt elektroniczny, oraz oryginalne akcesoria i materiały eksploatacyjne HP. Prowadzimy działalność na terenie byłego województwa wałbrzyskiego. Firma zajmuje się dostarczaniem firmom, instytucjom, szkołom różnorodnego sprzętu elektronicznego, biurowego.  Serwisujejemy  ten sprzęt oraz dostarczamy wszelkich materiałów eksploatacyjnych (tonery, atramenty) i artykułów biurowych. Do najważniejszych dziedzin naszej działalności należy serwis i sprzedaż kserokopiarek,drukarek, laptopów, monitorów, kas fiskalnych, niszczarek, tablic interaktywnych. Dla naszych klientów posiadamy szeroki wybór sprzętu potrzebnego do prowadzenia biura jak i wszelkiego rodzaju materiały biurowe w szczególności szeroki wybór atramentów i tonerów.',
        'ul. Sikorskiego 37, 58-105 Świdnica',
        'http://www.boskar.com.pl/'),
    (@uuid_c6, '8842587872', 'SCREENSUN',
        'Od 10 lat doradzamy, jak wybrać najlepsze i najpiękniejsze rolety, żaluzje, plisy i zasłony na wymiar. Udekorowaliśmy już setki okien w domach, biurach, hotelach i budynkach użyteczności publicznej oraz przejechaliśmy tysiące kilometrów na pomiar i montaż.  Nasz sklep internetowy Screensun™ powstał głównie z myślą o klientach spoza województwa dolnośląskiego, z którymi nie możemy spotkać się osobiście.  Wszystkie osłony okienne produkujemy na wymiar, a następnie wysyłamy na wskazany przez Ciebie adres w najkrótszym możliwym czasie. Zachęcamy do skorzystania z  konfiguratora, za pomocą którego idealnie dopasujesz produkt do własnych okien bez wychodzenia z domu.  Zakupy rolet, żaluzji, plis czy zasłon przez internet nigdy nie były prostsze. Na każdym etapie służymy kompleksowym doradztwem technicznym w zakresie precyzyjnego pomiaru, montażu i doboru systemu.',
        'ul. Prądzyńskiego 39/8, 58-105 Świdnica',
        'https://www.screensun.pl/'),
    (@uuid_c7, '8841001580', 'AUDYT Biuro Biegłych Rewidentów Sp. z o.o.',
        'Działamy w branży rachunkowej, audytorskiej i doradztwa podatkowego od 1994 roku. Nasza firma istnieje na rynku finansowo-księgowym województwa dolnośląskiego od ponad 25 lat.  Mamy bogate doświadczenie w przeprowadzaniu badań sprawozdań finansowych różnych jednostek gospodarczych, jak również w prowadzeniu księgowości wielu podmiotów gospodarczych. Oferujemy kompleksową obsługę.',
        'ul. Bystrzycka 24, 58-100 Świdnica',
        'https://www.audyt.swidnica.pl/'),
    (@uuid_c8, '8841096511', 'Alustad',
        'Alustad - jesteśmy producentem stolarki aluminiowej i stalowej.',
        'ul. Bokserska 4, 58-100 Świdnica',
        'https://www.alustad.com.pl/'),
    (@uuid_c9, '8842592666', 'BITKOM',
        'Branża alarmów i zabezpieczeń antywłamaniowych zajmuje się dostarczaniem produktów i usług związanych z zapobieganiem i reagowaniem na włamania, kradzieże i inne potencjalne zagrożenia w budynkach, na posesjach lub w innych miejscach. Branża dostarcza systemy alarmowe, które rejestrują i sygnalizują nieautoryzowany dostęp lub potencjalne zagrożenia. To może obejmować alarmy dźwiękowe, alarmy świetlne lub powiadomienia przekazywane do systemów monitoringu. Kamery bezpieczeństwa są używane do monitorowania i rejestrowania działań w określonych obszarach. Systemy monitoringu wideo pozwalają na rejestrowanie zdarzeń oraz dostęp do obrazu w czasie rzeczywistym. Czujniki ruchu wykrywają ruch w określonych obszarach i mogą inicjować alarmy w przypadku nieautoryzowanego dostępu lub ruchu w nocy. To również instalacja zabezpieczeń fizycznych, takich jak rolety antywłamaniowe, drzwi o zwiększonej wytrzymałości, zamki i okna o wyższym stopniu odporności na włamanie. Systemy kontroli dostępu pozwalają na zarządzanie i monitorowanie, kto ma dostęp do określonych pomieszczeń lub obszarów, zazwyczaj przy użyciu kart magnetycznych, kodów PIN lub technologii biometrycznych. Firmy monitorujące zapewniają usługi monitorowania systemów alarmowych i reagują na alarmy, np. dzwoniąc do odpowiednich służb lub właściciela nieruchomości w przypadku alarmu. Zabezpieczenia technologiczne obejmują zabezpieczenia cyfrowe i technologiczne, takie jak systemy alarmowe w smartfonach, które pozwalają na zdalne monitorowanie i kontrolowanie bezpieczeństwa. Branża oferuje produkty i rozwiązania, które pomagają w oznakowaniu mienia, np. znaki alarmowe, które ostrzegają potencjalnych włamywaczy. Branża alarmów i zabezpieczeń antywłamaniowych ma na celu zapewnienie bezpieczeństwa mienia i osób oraz zapobieganie włamaniom i kradzieżom. Oferuje różne opcje, od prostych systemów alarmowych po zaawansowane systemy monitoringu i kontroli dostępu.',
        'ul. Wrocławska 28/8, 58-100 Świdnica',
        'https://www.bit-kom.pl/'),
    (@uuid_c10, '8842115570', 'Euforino',
        'Tworzenie stron www to nie tylko technologia, to także działania z zakresu marketingu i komunikacji społecznej. Strony internetowe to w obecnych czasach niezbędne narzędzie marketingowe pozwalające na szybką, skuteczną i niedrogą komunikację z Twoimi klientami i partnerami. Doskonale rozumiemy te potrzeby, dlatego nasze strony www są zorientowane na skuteczność i realizację celów.',
        'ul. Kozara-Słobódzkiego 11/3, 58-105 Świdnica',
        'https://euforino.pl/');
