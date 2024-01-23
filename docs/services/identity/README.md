# Usługa *Identity*

## *Usługa do obsługi uwierzytelnienia i autoryzacji użytkowników platformy*

---

## Spis treści

### 1. [Wykaz głównych endpointów](#1-wykaz-głównych-endpointów)

### 2. [Obsługa logowania](#2-obsługa-logowania)

### 3. [Obsługa rejestracji](#3-obsługa-rejestracji)

---

## Wykaz głównych endpointów

### Prefiks : `/api/identity`

### Endpointy

|**Prefiks**|**Opis**|
|---|---|
|`/login` | Obsługa logowania |
|`/register` | Obsługa rejestracji |

---

## Obsługa logowania

### Enpoint `/api/identity/login/user`

*Uwierzytelnienie użytkownika.*

**Metoda HTTP** : `POST`

**Request Body:**

``` json
{
  "email": "user@mailbox.com",
  "password": "Password1"
}
```

**Response `OK`:**

``` json
{
  "code": 200,
  "message": "User successfully authenticated.",
  "data": {
    "email" : "user@mailbox.com",
    "password_hash" : "$2b$12$0vkC/yg/H8iVKxXW9J0QCOxTiDQE.lgWFPm1xVxUDuXH2lAkQUDh2",
    "phone_number" : "+48524665997"
  }
}
```

**Response `UNAUTHORIZED`:**

``` json
{
    "code" : 401,
    "message" : "Authentication ended with failure.",
    "error" : "Invalid credentials or user not registered yet!"
}
```

---

### Enpoint `/api/identity/login/company`

*Uwierzytelnienie przedsiębiorstwa.*

**Metoda HTTP** : `POST`

**Request Body:**

``` json
{
  "email": "user@mailbox.com",
  "password": "Password1"
}
```

**Response `OK`:**

``` json
{
  "code": 200,
  "message": "Company user successfully authenticated.",
  "data": {
    "email" : "user@mailbox.com",
    "password_hash" : "$2b$12$0vkC/yg/H8iVKxXW9J0QCOxTiDQE.lgWFPm1xVxUDuXH2lAkQUDh2",
    "phone_number" : "+48524665997"
  }
}
```

**Response `UNAUTHORIZED`:**

``` json
{
    "code" : 401,
    "message" : "Authentication ended with failure.",
    "error" : "Invalid credentials or company not registered yet!"
}
```

---

## Obsługa rejestracji

### Enpoint `/api/identity/register`

*Rejestracja nowego użytkownika.*

**Metoda HTTP** : `POST`

**Request Body:**

``` json
{
    "email" : "user@mailbox.com",
    "password" : "Password1",
    "phone_number" : "+48524665997"
}
```

**Response `CREATED`:**

``` json
{
  "code": 201,
  "message": "User successfully registered.",
  "data": {
    "email" : "user@mailbox.com",
    "password_hash" : "$2b$12$0vkC/yg/H8iVKxXW9J0QCOxTiDQE.lgWFPm1xVxUDuXH2lAkQUDh2",
    "phone_number" : "+48524665997"
  }
}
```

**Response `CONFLICT`:**

``` json
{
    "code" : 409,
    "message" : "User already exists.",
    "error" : "This e-mail address is already taken!"
}
```
