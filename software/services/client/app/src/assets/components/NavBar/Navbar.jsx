import "./navbar.css"
import MainPage from "../pages/main-page"
import { Link, useMatch, useResolvedPath } from "react-router-dom"
import { useState } from "react"

// NavBar component
export default function NavBar() {
    const [menuOpen, setMenuOpen] = useState(false);

    return (
        <nav>
            <Link to="" className="title">Swidnica</Link>
            <div 
                className="menu" 
                onClick={() => {
                    setMenuOpen(!menuOpen);
                }}
            >
                <span></span>
                <span></span>
                <span></span>
            </div>
            <ul className={menuOpen ? "open" : ""}>
                <CustomLink to="/main">Strona Glowna</CustomLink>
                <CustomLink to="/cv">Cv</CustomLink>
                <CustomLink to="/courses">Kursy</CustomLink>
                <CustomLink to="/login">Konto</CustomLink>
            </ul>
        </nav>
    );
}


function CustomLink({to,children, ...props}) {
    const resolvedPath = useResolvedPath(to)
    const isActive = useMatch({path: resolvedPath.pathname, end:  true})
    return (
        <li className={isActive ? "active" : ""}>
            <Link to={to} {...props}>{children}</Link>
        </li>
    )
}