# #Zostań_w_Świdnicy

*Projekt opracowany podczas konkursu **HackYeah 2023**.*

---

## Spis treści

### 1. [Opis](#opis)

### 2. [Dokumentacja](docs/)

### 3. [Struktura repozytorium](#struktura-repozytorium)

---

## Opis

![image](https://github.com/ITA-Flowers/Zostan_w_Swidnicy/assets/74451381/fa5577ca-f411-45d8-bf57-256f67b65ec3)

Platforma do ukierunkowania ścieżki rozwoju zawodowego, doboru odpowiedniej pracy oraz zapisów na kursy zawodowe organizowane przez lokalne przedsiębiorstwa dla mieszkańców miasta Świdnica i okolic.

---

## Struktura repozytorium

``` text
.
├── assets                              /*!< obrazy, wykresy, diagramy */            
├── docs                                /*!< dokumentacja */                
└── software                            /*!< kod źródłowy aplikacji */       
    ├── services                        /*!< mikrousługi */    
    │   ├── api_gateway                 /*!< Usługa API_GATEWAY */    
    │   │   ├── Dockerfile                  /*!< skrypt budujący obraz Docker'a */    
    │   │   └── app                         /*!< kod źródłowy usługi */    
    │   ├── client                      /*!< Usługa aplikacji klienckiej */    
    │   │   ├── Dockerfile                  /*!< skrypt budujący obraz Docker'a */
    │   │   └── app                         /*!< kod źródłowy usługi */
    │   ├── db                          /*!< Usługa DB */
    │   │   ├── Dockerfile                  /*!< skrypt budujący obraz Docker'a */
    │   │   └── scripts                     /*!< skrypty inicjujące bazy danych */
    │   ├── db_driver                   /*!< Usługa DB_DRIVER */
    │   │   ├── Dockerfile                  /*!< skrypt budujący obraz Docker'a */
    │   │   └── app                         /*!< kod źródłowy usługi */
    │   ├── docker-compose.yml          /*!< skrypt agregujący obrazy Docker'a */
    │   ├── employee                    /*!< Usługa EMPLOYEE */
    │   │   ├── Dockerfile                  /*!< skrypt budujący obraz Docker'a*/
    │   │   └── app                         /*!< kod źródłowy usługi */
    │   ├── employer                    /*!< Usługa EMPLOYER */
    │   │   ├── Dockerfile                  /*!< skrypt budujący obraz Docker'a */
    │   │   └── app                         /*!< kod źródłowy usługi */
    │   └── identity                    /*!< Usługa IDENTITY */
    │       ├── Dockerfile                  /*!< skrypt budujący obraz Docker'a */
    │       └── app                        /*!< kod źródłowy usługi */
    ├── tools                       /*!< narzędzia i skrypty pomocnicze dla VM */
    └── vm                          /*!< maszyna wirtualna, konfiguracje VM */
```
