import { loadStdlib } from '@reach-sh/stdlib'
import Login from './components/Login'
import Form from './components/Form'
import Route from './components/Route'
import { BrowserRouter, Routes } from 'react-router-dom'

import React from 'react'

import './assets/css/app.css'
import Home from './pages/Home'

function App() {
  return (

    <BrowserRouter>
      <Routes>
        <Route exact path='/Form' element={<Form />} />
        <Route path={"/"} exact element={<Home />} />
        <Route path={"/login"} exact element={<Login />} />

      </Routes>
    </BrowserRouter>


  )
}

export default App;