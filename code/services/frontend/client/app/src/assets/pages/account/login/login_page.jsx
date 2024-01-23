import './login_page.css';
import user_icon from './assets/person.png';
import email_icon from './assets/email.png';
import password_icon from './assets/password.png';
import { useState } from 'react';
// import InfoModal from './assets/components/PopUp/Popup'
 
export default function Login() {
    const [action, setAction] = useState("Zaloguj się");
    const initialValues = {
        email: "",
        password: "",
        confirm_password: "",
        nip: ""
    };
    const [formValues, setFormValues] = useState(initialValues);
    const [formErrors, setFormErrors] = useState({});
    // dla NIP
    const [isChecked, setIsChecked] = useState(false);
    // do powiadomienia o wyslaniu maial
    const [isModelOpen, setIsModelOpen] = useState(false);

    const openModel = () => {
        setIsModelOpen(true)
    }

    const closeModel = () => {
        setIsModelOpen(false)
    }
   

    const handleChange = (e) => {
        // console.log(e.target)
        const { name, value } = e.target;
        setFormValues({...formValues, [name] : value});
        // console.log(formValues)
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
    
        if (action === "Zaloguj się") {
            setActionAndResetForm("Zarejestruj się");
        } else {
            const errors = validate(formValues);
            setFormErrors(errors);
    
            if (Object.keys(errors).length === 0) {
                
                openModel();
    
               
                resetForm();
                // idzie rejestracja dalej
            } else {
                // Wywołaj to tylko, gdy są błędy
                
            }
        }
    };

    const handleSubmit_LogIn = async (e) => {
        e.preventDefault();
    
        if (action === "Zarejestruj się") {
            setActionAndResetForm("Zaloguj się");
        } else {
            const loginErrors = validateLogin(formValues);
            
            setFormErrors(loginErrors);
            if (Object.keys(loginErrors).length === 0 && loginErrors === 1) {
                resetForm();
                console.log("TU BEDZIE API NA MAILA")
            }  else if (Object.keys(loginErrors).length === 0 && loginErrors === 2) {
                resetForm();
                console.log("TU BEDZIE API NA NIP")
            }
        }
    };

    const validate = (values) => {
        const errors = {}
        const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
        const passwordRegex = /^(?=.*[A-Z])(?=.*\d).+/;
        
        if (!emailRegex.test(values.email)) {
            errors.email = "Sprawdz czy poprawnie wprowadziles maila"
        } 
        if (!passwordRegex.test(values.password)) {
            errors.password = "Hasło musi zawierać conajmniej 1 wielką literę oraz cyfrę"
        }
        if (values.password !== values.confirm_password) {
            errors.confirm_password = "Hasła nie są identyczne"
        }
        if (values.password.length < 7) {
            errors.password = "Hasło jest za krótkie"
        }
        if (!values.email || !values.password || !values.confirm_password ) {
            
            errors.email = "Uzupełnij wszystkie pola";
        }
        if(isChecked && !values.nip){
            errors.nip = "Uzupełnij NIP"
        }
        
        
        return errors;

    }

    const validateLogin = (values) => {
        const errors = {};
        const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
        const nipRegex = /^\d{10}$/;
        // TODO: dodac walidacje jak mail ani regex nie wchodzi , dac walidaje w osobne funkcje aby byl kurwa do nich jakis dostep xddd
        
        if (!values.email || !values.password) {
            errors.email = "Uzupełnij wszystkie pola";
            // wszedl NIP ale nie wszedl mail
        
        } else if (!nipRegex.test(values.email) && !emailRegex.test(values.email)) {
            errors.email = "Wprowadz poprawne dane (mail lub NIP)"
        
        } else if (nipRegex.test(values.email) && !emailRegex.test(values.email)) {
            return 2
        
        } else if (!nipRegex.test(values.email) && emailRegex.test(values.email)) {
            return 1
        } 
    
        return errors;
    };
    
    // czyszczenie inputow
    const resetForm = () => {
        setFormValues(initialValues);
        setFormErrors({});
    }

    const setActionAndResetForm = (newAction) => {
        setAction(newAction);
        resetForm();
    }
    

    return (
        <div className='container'>
            {/* <InfoModal
                isOpen={isModelOpen}
                closeModal={closeModel}
                message="Mail z potwierdzeniem został wysłany na podany adres"></InfoModal> */}
            <div className="header">
                <div className="text">
                    {action}
                </div>
                <div className="underline"></div>
            </div>
            <div className="inputs">
                <div className="input">
                    <img src={email_icon} alt="" />
                    <input 
                    onChange={handleChange} 
                    value={formValues.email} 
                    name='email' type="email" 
                    placeholder='Podaj swój adres email lub NIP' />
                </div>
                 <p className='errors'>{formErrors.email}</p> 
                <div className="input">
                    <img src={password_icon} alt="" />
                    <input 
                    onChange={handleChange} 
                    value={formValues.password} 
                    name='password' 
                    type="password" 
                    placeholder='Podaj hasło' />
                </div>
                <p className='errors'>{formErrors.password}</p>
                {action === "Zaloguj się" ? null : (
                    <div className="input">
                        <img src={password_icon} alt="" />
                        <input 
                        onChange={handleChange} 
                        value={formValues.confirm_password} 
                        name='confirm_password' 
                        type="password" 
                        placeholder='Podaj ponownie hasło' />
                    </div>
                )}
                {action==="Zarejestruj się" ?  
                <div  >
                    <label className='checkbox-label'>
                        <input 
                            type="checkbox"
                            checked={isChecked}
                            onChange={()=> setIsChecked(!isChecked)}
                            /> Rejestrujesz się jako firma?
                    </label>
                    <br/>
                    
                    {isChecked && (
                         <div className="input">
                         <img src={user_icon} alt="" />
                         <input
                             onChange={handleChange}
                             value={formValues.nip}
                             name='nip'
                             type="text"
                             placeholder='Podaj NIP'
                         />
                        {action === "Zarejestruj się" ? <p className='errors'>{formErrors.nip}</p> : null}     
                     </div>
                     
                    )}
                </div> : null}
               
            </div>
            {action === "Zarejestruj się" ? <p className='errors'>{formErrors.confirm_password}</p> : (
                <div className="forgot-password">
                    Zapomniałeś hasła? <span>kliknij tu</span>
                </div>
            )}
            <div className="submit-container">
                <div className={action === "Zaloguj się" ? "submit grey" : "submit"} onClick={ handleSubmit}>
                    Zarejestruj się
                </div>
                <div className={action === "Zarejestruj się" ? "submit grey" : "submit"} onClick={handleSubmit_LogIn}>
                    Zaloguj się
                </div>
            </div>
        </div>
    );
}
