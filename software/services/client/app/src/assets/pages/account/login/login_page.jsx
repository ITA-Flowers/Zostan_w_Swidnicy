import './login_page.css'
import user_icon from './assets/person.png'
import email_icon from './assets/email.png'
import password_icon from './assets/password.png'
import { useState } from 'react'
export default function Login(){
    const [action,setAction] = useState("Zaloguj się");
    return (
        <div className='container'>
            <div className="header">
                <div className="text">
                    {action}
                </div>
                <div className="underline"></div>

            </div>
            <div className="inputs">
                {/* if action == login, nie jest potrzebne pole z imieniem */}
                {action==="Zaloguj się" ? <div></div> : <div className="input">
                    <img src={user_icon} alt="" />
                    <input type="text" placeholder='Podaj swoje imię' />
                </div>}
                
                <div className="input">
                    <img src={email_icon} alt="" />
                    <input type="email" placeholder='Podaj swój adres email'/>
                </div>
                <div className="input">
                    <img src={password_icon} alt="" />
                    <input type="password" placeholder='Podaj hasło' />
                </div>
            </div>
            {action === "Zarejestruj się"? <div></div> : <div className="forgot-password">Zapomniales hasla? <span>kliknij tu</span></div>}
            
            <div className="submit-container">
                <div className={action==="Zaloguj się" ? "submit grey": "submit"} onClick={()=>{setAction("Zarejestruj się")}}>Zarejestruj się</div>
                <div className={action==="Zarejestruj się" ? "submit grey": "submit"} onClick={()=>{setAction("Zaloguj się")}}>Zaloguj się</div>
            </div>
        </div>
    )
}