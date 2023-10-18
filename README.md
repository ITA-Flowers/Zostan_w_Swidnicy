# #Zostań_w_Świdnicy

## *Projekt opracowany podczas konkursu **HackYeah 2023**.*

---

## Spis treści

### 1. [Opis](#opis)

### 2. [Struktura repozytorium](#struktura-repozytorium)

### 3. [Dokumentacja](docs/README.md)

---

## Opis

![image](https://github.com/ITA-Flowers/Zostan_w_Swidnicy/assets/74451381/fa5577ca-f411-45d8-bf57-256f67b65ec3)

Platforma do ukierunkowania ścieżki rozwoju zawodowego, doboru odpowiedniej pracy oraz zapisów na kursy zawodowe organizowane przez lokalne przedsiębiorstwa dla mieszkańców miasta Świdnica i okolic.

---

## Struktura repozytorium

``` text
.
├── assets                          /*!< obrazy, wykresy, diagramy */            
├── docs                            /*!< dokumentacja */
├── vm                              /*!< maszyna wirtualna */                
└── software                        /*!< kod źródłowy aplikacji */       
    ├── services                        /*!< mikrousługi */    
    │   ├── api_gateway                     /*!< Usługa API_GATEWAY */    
    │   │   └── app                             /*!< kod źródłowy usługi */    
    │   ├── client                          /*!< Usługa aplikacji klienckiej */    
    │   │   └── app                             /*!< kod źródłowy usługi */
    │   ├── db                              /*!< Usługa DB */
    │   │   └── scripts                         /*!< skrypty inicjujące bazy danych */
    │   ├── db_driver                       /*!< Usługa DB_DRIVER */
    │   │   └── app                             /*!< kod źródłowy usługi */
    │   ├── employee                        /*!< Usługa EMPLOYEE */
    │   │   └── app                             /*!< kod źródłowy usługi */
    │   ├── employer                        /*!< Usługa EMPLOYER */
    │   │   └── app                             /*!< kod źródłowy usługi */
    │   └── identity                        /*!< Usługa IDENTITY */
    │   │   └── app                            /*!< kod źródłowy usługi */
    │   └── compose.yml                     /*!< skrypt budujący klaster Docker Compose */
    └── tools                           /*!< narzędzia i skrypty pomocnicze dla VM */
```
