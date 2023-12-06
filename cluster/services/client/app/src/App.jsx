import React  from "react";
import NavBar from "./assets/components/Navbar";
import MainPage from "./assets/pages/main-page";
import CreateCv from "./assets/pages/cv_page/create-cv";
import Courses from "./assets/pages/courses_page/courses";
import { Route, Routes } from "react-router";
import Login from "./assets/pages/account/login/login_page";
export default function App() {
  
  return <>
  <NavBar/>
  
    <Routes>
      <Route path="/" element={<MainPage/>}/>
      <Route path="/main" element={<MainPage/>}/>
      <Route path="/cv" element={<CreateCv/>}/>
      <Route path="/courses" element={<Courses/>}/>
      <Route path="/login" element={<Login/>}/>
    </Routes>
  </>
    
  
}