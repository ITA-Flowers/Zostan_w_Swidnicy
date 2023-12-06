import './create-cv.css'
import resume from './assets/resume.png'
import resumesvg from './assets/resume-svg.svg'
import { useState
 } from 'react';
 
export default function CreateCv(){

    // code for languague picker
const [languages, setLanguages] = useState([{ language: '', proficiency: '' }]);

  const handleLanguageChange = (index, event) => {
    const newLanguages = [...languages];
    newLanguages[index][event.target.name] = event.target.value;
    setLanguages(newLanguages);
  };

  const handleAddLanguage = () => {
    setLanguages([...languages, { language: '', proficiency: '' }]);
  };

  const handleRemoveLanguage = (index) => {
    const newLanguages = [...languages];
    newLanguages.splice(index, 1);
    setLanguages(newLanguages);
  };
// code for work experience picker

const [workExperience, setWorkExperience] = useState([
    { startDate: '', endDate: '', position: '', description: '' },
  ]);

  const handleInputChange = (index, fieldName, value) => {
    const newWorkExperience = [...workExperience];
    newWorkExperience[index][fieldName] = value;
    setWorkExperience(newWorkExperience);
  };

  const handleAddWorkExperience = () => {
    setWorkExperience([
      ...workExperience,
      { startDate: '', endDate: '', position: '', description: '' },
    ]);
  };

  const handleRemoveWorkExperience = (index) => {
    const newWorkExperience = [...workExperience];
    newWorkExperience.splice(index, 1);
    setWorkExperience(newWorkExperience);
  };
//   eductaion form
const [education, setEducation] = useState([
    {
      startDate: '',
      endDate: '',
      fieldOfStudy: '',
      specialization: '',
      educationLevel: 'Zawodowe', 
    },
  ]);

  const handleInputChangeEducation = (index, fieldName, value) => {
    const newEducation = [...education];
    newEducation[index][fieldName] = value;
    setEducation(newEducation);
  };

  const handleAddEducation = () => {
    setEducation([
      ...education,
      {
        startDate: '',
        endDate: '',
        fieldOfStudy: '',
        specialization: '',
        educationLevel: 'Zawodowe',
      },
    ]);
  };

  const handleRemoveEducation = (index) => {
    const newEducation = [...education];
    newEducation.splice(index, 1);
    setEducation(newEducation);
  };

// courses form
const [certificates, setCertificates] = useState([
    {
      date: '',
      name: '',
      organizer: '',
    },
  ]);

  const handleInputChangeCertificate = (index, fieldName, value) => {
    const newCertificates = [...certificates];
    newCertificates[index][fieldName] = value;
    setCertificates(newCertificates);
  };

  const handleAddCertificate = () => {
    setCertificates([
      ...certificates,
      {
        date: '',
        name: '',
        organizer: '',
      },
    ]);
  };
//   links
const [links, setLinks] = useState([
    {
      label: '',
      url: '',
    },
  ]);

  const handleInputChangeLinks = (index, fieldName, value) => {
    const newLinks = [...links];
    newLinks[index][fieldName] = value;
    setLinks(newLinks);
  };

  const handleAddLink = () => {
    setLinks([
      ...links,
      {
        label: '',
        url: '',
      },
    ]);
  };

  const handleRemoveLink = (index) => {
    const newLinks = [...links];
    newLinks.splice(index, 1);
    setLinks(newLinks);
    console.log(links);
  };
  const handleRemoveCertificate = (index) => {
    const newCertificates = [...certificates];
    newCertificates.splice(index, 1);
    setCertificates(newCertificates);
  };

    return <div className="cv">
        <div className="container-cv">
        <div className="style-left">
            <p className="heading">
                Stwórz <span>Swoje</span> CV
            </p>
            <div className="line"></div>
            <p className="heading">
                Zacznij działać w kierunku <span>wymarzonej</span> kariery
            </p>
        </div>
        <div className="style-right">
            <img src={resumesvg} alt="resume" />
        </div>
        
        </div>
        <div className="body">
            <p className='heading-cv'>Generator CV</p>
            <div className="input-cv">
                <input 
                type="text"
                name='name'
                placeholder ="podaj swoje imie i nazwisko"
                />
            </div>
            
            <div className="input-cv">
                <input 
                type="phone"
                name='phone-number'
                placeholder ="podaj swój numer telefonu"
                />
            </div>
            <div className="input-cv">
               
                <input 
                type="date"
                name='date-birth'
                placeholder ="data urodzenia"
                />

            </div>
            <div className="input-cv">
               
                <input 
                type="text"
                name='city'
                placeholder ="miejsce zamieszkania (miejscowość)"
                />

            </div>
            
      <div className="input-cv desc">
               
               <input 
               type="text"
               name='city'
               placeholder ="Opisz swoje umiejętności"
               />

           </div>
            <div className="input-cv desc">
               
               <input 
               type="text"
               name='city'
               placeholder ="opisz krótko siebie, czym się interesujesz?"
               />

           </div>
           {/* jezyk wybor */}
           <h3>Znajomość języków</h3>
      {languages.map((language, index) => (
        <div key={index} className="language-inputs">
          <input
            type="text"
            name="language"
            placeholder="Język"
            value={language.language}
            onChange={(e) => handleLanguageChange(index, e)}
          />
          <input
            type="text"
            name="proficiency"
            placeholder="Poziom"
            value={language.proficiency}
            onChange={(e) => handleLanguageChange(index, e)}
          />
          {languages.length > 1 && (
            <button type="button" onClick={() => handleRemoveLanguage(index)}>
              Usuń
            </button>
          )}
        </div>
      ))}
      <button type="button" onClick={handleAddLanguage}>
        Dodaj język
      </button>
        {/* Work experience */}
        <h3>Doświadczenie zawodowe</h3>
      {workExperience.map((experience, index) => (
        <div key={index} className="work-experience-inputs">
          <div>
            <label>Okres pracy:</label>
            <input
              type="date"
              value={experience.startDate}
              onChange={(e) =>
                handleInputChange(index, 'startDate', e.target.value)
              }
            />
            <input
              type="date"
              value={experience.endDate}
              onChange={(e) =>
                handleInputChange(index, 'endDate', e.target.value)
              }
            />
          </div>
          <div>
            <label>Stanowisko:</label>
            <input
              type="text"
              value={experience.position}
              onChange={(e) =>
                handleInputChange(index, 'position', e.target.value)
              }
            />
          </div>
          <div>
            <label>Opis stanowiska:</label>
            <input
              type="text"
              value={experience.description}
              onChange={(e) =>
                handleInputChange(index, 'description', e.target.value)
              }
            />
          </div>
          {workExperience.length > 1 && (
            <button onClick={() => handleRemoveWorkExperience(index)}>
              Usuń
            </button>
          )}
        </div>
      ))}
      <button type="button" onClick={handleAddWorkExperience}>
        Dodaj miejsce pracy
      </button>
      {/* edukacjaaaa */}
      <h3>edukacja</h3>
      {education.map((edu, index) => (
        <div key={index} className="education-inputs">
          <div>
            <label>Okres nauki:</label>
            <input
              type="date"
              value={edu.startDate}
              onChange={(e) => handleInputChangeEducation(index, 'startDate', e.target.value)}
            />
            <input
              type="date"
              value={edu.endDate}
              onChange={(e) => handleInputChangeEducation(index, 'endDate', e.target.value)}
            />
          </div>
          <div>
            <label>Kierunek:</label>
            <input
              type="text"
              placeholder='Budownictwo'
              value={edu.fieldOfStudy}
              onChange={(e) => handleInputChangeEducation(index, 'fieldOfStudy', e.target.value)}
            />
          </div>
          <div>
            <label>Specjalizacja:</label>
            <input
            placeholder='może pozostać puste'
              type="text"
              value={edu.specialization}
              onChange={(e) => handleInputChangeEducation(index, 'specialization', e.target.value)}
            />
          </div>
          <div>
            <label>Poziom wykształcenia:</label>
            <select
              value={edu.educationLevel}
              onChange={(e) => handleInputChangeEducation(index, 'educationLevel', e.target.value)}
            >
              <option value="Zawodowe">Zawodowe</option>
              <option value="Średnie">Średnie</option>
              <option value="Inżynierskie">Inżynierskie</option>
              <option value="Magisterskie">Magisterskie</option>
              <option value="Doktoranckie">Doktoranckie</option>
            </select>
          </div>
          {education.length > 1 && (
            <button onClick={() => handleRemoveEducation(index)}>
              Usuń
            </button>
          )}
        </div>
      ))}
      <button type="button" onClick={handleAddEducation}>
        Dodaj miejsce nauki
      </button>
     
           {/* certyfikaty */}
           <h3>Certyfikaty</h3>
      {certificates.map((certificate, index) => (
        <div key={index} className="certificate-inputs">
          <div>
            <label>Data uzyskania/odbycia:</label>
            <input
              type="date"
              value={certificate.date}
              onChange={(e) => handleInputChangeCertificate(index, 'date', e.target.value)}
            />
          </div>
          <div>
            <label>Nazwa certyfikatu/szkolenia:</label>
            <input
              type="text"
              value={certificate.name}
              onChange={(e) => handleInputChangeCertificate(index, 'name', e.target.value)}
            />
          </div>
          <div>
            <label>Organizator:</label>
            <input
              type="text"
              value={certificate.organizer}
              onChange={(e) => handleInputChangeCertificate(index, 'organizer', e.target.value)}
            />
          </div>
          {certificates.length > 1 && (
            <button onClick={() => handleRemoveCertificate(index)}>
              Usuń
            </button>
          )}
        </div>
      ))}
      <button type="button" onClick={handleAddCertificate}>
        Dodaj certyfikat
      </button>
      {/* linki */}
      <h3>Linki</h3>
      {links.map((link, index) => (
        <div key={index} className="link-inputs">
          <div>
            
            <input
            placeholder='Nazwa witryny'
              type="text"
              value={link.label}
              onChange={(e) => handleInputChangeLinks(index, 'label', e.target.value)}
            />
          </div>
          <div>
           
            <input
            placeholder='nadres URL'
              type="url"
              value={link.url}
              onChange={(e) => handleInputChangeLinks(index, 'url', e.target.value)}
            />
          </div>
          {links.length > 1 && (
            <button onClick={() => handleRemoveLink(index)}>
              Usuń
            </button>
          )}
        </div>
      ))}
      <button type="button" onClick={handleAddLink}>
        Dodaj link
      </button>
      
      <div className="under-line"></div>

      <button type='button'>
        Dodaj swoje cv

      </button>
        </div>
        
    </div>
}