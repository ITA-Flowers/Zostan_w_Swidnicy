# #Zostań_w_Świdnicy

*Platforma do ukierunkowania ścieżki rozwoju zawodowego, doboru odpowiedniej pracy oraz zapisów na kursy zawodowe organizowane przez lokalne przedsiębiorstwa dla mieszkańców miasta Świdnica i okolic. Opracowane podczas konkursu **HackYeah 2023**.*

---

## Spis treści

### 1. [Opis](#opis)

### 2. [Dokumentacja](https://github.com/ITA-Flowers/Zostan_w_Swidnicy/tree/masterdocs)

### 3. [Struktura repozytorium](#struktura-repozytorium)

---

## Opis

[!swidnica_tf_vm_wallpaper](https://raw.githubusercontent.com/ITA-Flowers/Zostan_w_Swidnicy/master/assets/vm_wallpaper.png?token=GHSAT0AAAAAACIQZQGLOZVJMEILVMQ7IYPAZJO45LA)

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
