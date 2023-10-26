from pydantic import BaseModel

class Cv(BaseModel):
    user : User
    # Wszystkie dane użytkownika potrzebne do generowania CV z profilu (e-mail, telefon, data urodzenia, miejscowość)
    
    description : str
    # Krótka notatka o swojej osobie.

    experience : Dict[str, str]
    # Konieczna walidacja na poziomie front (Daty, adresy pracodawców, ogólnie wprowadzane informacje)
    # Oczekiwana struktura: 
    # {
    # "Okres pracy" : "data_rozpoczęcia - data_zakończenia",
    # "Stanowisko" : "Miejsce pracy, adres miejsca pracy",
    # "Opis stanowiska" : "To było moje stanowisko, robiłem to i tamto"
    # }
    
    education : Dict[str, str]
    # Również konieczna walidacja na poziomie front. Oczekiwana struktura:
    # {
    # "Okres nauki" : "data_rozpoczęcia - data_zakończenia",
    # "Kierunek" : "Zawód z technikum/zawodówy, lub ukończony kierunek studów",
    # "Specjalizacja" : "Jeśli studia, to istnieje, jeśli nie to chuj."
    # "Poziom wykształcenia" : "Magister, podstawowe, zawodówka etc."
    # }
    
    languages : Dict[str, str]
    # Znów walidacja potrzebna na froncie (głównie chodzi o to czy język istnieje czy coś, niby konieczne ale nie wiem.)
    # {
    # "Nazwa języka" : "Poziom języka (fajnie jakby był do wyboru, typu tam podstawowy średni biegły coś tam...)"
    # }
    
    skills : List[str]
    #Lista umiejętności, komunikatywność, spawanie.
    
    certificates : Dict[str, str]
    # {
    # "Data uzyskania/odbycia" : "No to wiadomo data",
    # "Nazwa certyfikatu/szkolenia" : "kurs pletwonurka",
    # "Organizator" : "Wojskowi lubią wiadomo co"
    # }

    additional_activity : Dict[str, str]
    # {
    # "Data aktywnosci" : "od - do",
    # "Nazwa aktywnosci" : "hackathon o puchar DKWOC, nagorda 32,50",
    # "Organizator" : "Mario Chm"
    # }

    interests : List[str]
    # Podroze, netflix

    links : Dict[str, str]
    # {
    # "Facebook" : "link do fejsa",
    # "Instagram" : "link do insta XD" itp... ile doda, tyle wpierdolić
    # }