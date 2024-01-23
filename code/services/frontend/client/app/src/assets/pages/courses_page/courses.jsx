import React, { useState } from 'react';
import './courses.css';
import JobAdModel from '../../DataModels/JobAd';


const jobAds = [
  new JobAdModel(
    1,
    'https://example.com/img1.jpg',
    'Programista JavaScript',
    'Firma XYZ 1',
    'Warszawa',
    'Pełny etat',
    '7000-9000 PLN',
    'Umowa o pracę',
    'Stacjonarna',
    'Poniedziałek - Piątek',
    'Tworzenie i utrzymanie aplikacji webowych',
    'Doświadczenie w programowaniu w JavaScript',
    'Jesteśmy firmą specjalizującą się w tworzeniu aplikacji webowych.',
    '2023-12-31'
  ),
  new JobAdModel(
    2,
    'https://example.com/img1.jpg',
    'Idiota',
    'Firma XYZ 2',
    'Warszawa',
    'Pełny etat',
    '7000-9000 PLN',
    'Umowa o pracę',
    'Stacjonarna',
    'Poniedziałek - Piątek',
    'Tworzenie i utrzymanie aplikacji webowych',
    'Doświadczenie w programowaniu w JavaScript',
    'Jesteśmy firmą specjalizującą się w tworzeniu aplikacji webowych.',
    '2023-12-31'
  ),
  

];

export default function Courses() {
    const [filter, setFilter] = useState('');
    const [selectedJobIndex, setSelectedJobIndex] = useState(null);
    const [showPopup, setShowPopup] = useState(false);
  
    const filteredJobs = jobAds.filter(job => job.tytul.toLowerCase().includes(filter.toLowerCase()));
  
    const applyForJob = () => {
      setShowPopup(true);
      setTimeout(() => setShowPopup(false), 2000);
    };
  
    return (
      <>
          <div className="course-container">
            <input type="text" placeholder="Filtruj po tytule..." onChange={e => setFilter(e.target.value)} />
            {filteredJobs.map((job, index) => (
              <div key={job.id}>
                <div onClick={() => setSelectedJobIndex(index === selectedJobIndex ? null : index)}>
                  <h2>{job.tytul} | {job.miast_lub_adres} | {job.nazwa_firmy}</h2>
                  <p>{job.widelki_wynagrodzenia}</p>
                </div>
                {index === selectedJobIndex && (
                  <div className="job-details">
                     
                        <p>{job.wymiar_pracy}</p>
                        <p>{job.rodzaj_umowy}</p>
                        <p>{job.rodzaj_pracy}</p>
                        <p>{job.dni_pracy}</p>
                        <p>{job.zakres_obowiazkow}</p>
                        <p>{job.wymagania}</p>
                        <p>{job.o_firmie}</p>
                        <p>{job.data_wygasniecia}</p>
                    <button onClick={applyForJob}>Aplikuj</button>
                    <button onClick={() => setSelectedJobIndex(null)}>Zamknij</button>
                  </div>
                )}
              </div>
            ))}
          
          </div>
          {showPopup && (
            <div className="popup">
              Aplikowano! Dziękujemy za zainteresowanie
            </div>
          )}
      </>
    );
  }