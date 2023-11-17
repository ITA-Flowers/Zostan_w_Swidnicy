# Dokumentacja

## Spis treści

### 1. [Diagram struktury architektury](#diagram-struktury-architektury)

### 2. [Komunikacja międzyusługowa](#komunikacja-międzyusługowa)

### 3. [UML](uml/README.md)

### 4. [Mikrousługi](services/README.md)

### 5. [Maszyna wirtualna](vm/README.md)

### 6. [Skrypty automatyzujące](tools/README.md)

---

## Diagram struktury architektury

![swidnica](https://github.com/ITA-Flowers/Zostan_w_Swidnicy/assets/74451381/5f58b8aa-6e71-47b7-b39c-796efce6bc51)

---

## Komunikacja międzyusługowa

### Wzory odpowiedzi HTTP

#### **Odpowiedzi `POZYTYWNE`**

Odpowiedź pozytywna powinna zawierać trzy pola:

1. `code` - Status odpowiedzi (duplikacja zwracanego statusu HTTP)
2. `message` - Słowny opis statusu odpowiedzi
3. `data` - Zwracana struktura danych

**Przykład:**

``` json
{
    "code" : 201,
    "message" : "Resource successfully created.",
    "data" : [
        "email" : "user@gmail.com"
        "username" : "user",
    ]
}
```

---

#### **Odpowiedzi `NEGATYWNE`**

Odpowiedzi negatywne powinny zawierać trzy pola:

1. `code` - Status odpowiedzi (duplikacja zwracanego statusu HTTP)
2. `message` - Słowny opis statusu odpowiedzi
3. `error` - Szczegółowy opis błędu

**Przykład:**

``` json
{
    "code" : 409,
    "message" : "Resource already exists.",
    "error" : "This email address is already taken."
}
```
