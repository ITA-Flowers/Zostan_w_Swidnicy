import './login_page.css';
import user_icon from './assets/person.png';
import email_icon from './assets/email.png';
import password_icon from './assets/password.png';
import { useState } from 'react';

export default function Login() {
    const [action, setAction] = useState("Zaloguj się");
    const initialValues = {
        email: "",
        password: "",
        confirm_password: ""
    };
    const [formValues, setFormValues] = useState(initialValues);
    const [formErrors, setFormErrors] = useState({});

    const handleChange = (e) => {
        // console.log(e.target)
        const { name, value } = e.target;
        setFormValues({...formValues, [name] : value});
        // console.log(formValues)
    };

    const handleSubmit = (e) => {
        if (action == "Zaloguj się"){
            setAction("Zarejestruj się");
        } else {
        e.preventDefault();
        setFormErrors(validate(formValues));
        if ( Object.keys(formErrors).length === 0){
            // tu bedzie akcja jak bedzie logowanie api dzialalo
            console.log("giit");
        }
    }
    }

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
        if (!values.email || !values.password || !values.confirm_password ) {
            
            errors.email = "Uzupełnij wszystkie pola";
        }
        
        
        return errors;

    }

    return (
        <div className='container'>
            
            <div className="header">
                <div className="text">
                    {action}
                </div>
                <div className="underline"></div>
            </div>
            <div className="inputs">
                <div className="input">
                    <img src={email_icon} alt="" />
                    <input onChange={handleChange} value={formValues.email} name='email' type="email" placeholder='Podaj swój adres email' />
                </div>
                {action === "Zarejestruj się" ? <p className='errors'>{formErrors.email}</p> : null}
                <div className="input">
                    <img src={password_icon} alt="" />
                    <input onChange={handleChange} value={formValues.password} name='password' type="password" placeholder='Podaj hasło' />
                </div>
                {action === "Zarejestruj się" ? <p className='errors'>{formErrors.password}</p> : null}
                {action === "Zaloguj się" ? null : (
                    <div className="input">
                        <img src={password_icon} alt="" />
                        <input onChange={handleChange} value={formValues.confirm_password} name='confirm_password' type="password" placeholder='Podaj ponownie hasło' />
                    </div>
                )}
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
                <div className={action === "Zarejestruj się" ? "submit grey" : "submit"} onClick={() => {setAction("Zaloguj się");}}>
                    Zaloguj się
                </div>
            </div>
        </div>
    );
}
