class JobAdModel {
    constructor(
      id,
      img,
      tytul,
      nazwa_firmy,
      miast_lub_adres,
      wymiar_pracy,
      widelki_wynagrodzenia,
      rodzaj_umowy,
      rodzaj_pracy,
      dni_pracy,
      zakres_obowiazkow,
      wymagania,
      o_firmie,
      data_wygasniecia
    ) {
      this.id = id;
      this.img = img;
      this.tytul = tytul;
      this.nazwa_firmy = nazwa_firmy;
      this.miast_lub_adres = miast_lub_adres;
      this.wymiar_pracy = wymiar_pracy;
      this.widelki_wynagrodzenia = widelki_wynagrodzenia;
      this.rodzaj_umowy = rodzaj_umowy;
      this.rodzaj_pracy = rodzaj_pracy;
      this.dni_pracy = dni_pracy;
      this.zakres_obowiazkow = zakres_obowiazkow;
      this.wymagania = wymagania;
      this.o_firmie = o_firmie;
      this.data_wygasniecia = data_wygasniecia;
    }
  }

export default JobAdModel