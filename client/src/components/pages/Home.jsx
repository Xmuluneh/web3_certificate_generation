import React from 'react'
import { Link } from 'react-router-dom';
import LoginBtn from '../components/LoginBtn';


import '../assets/third_party/css/style.css'



const Home = () => {
  return (
    <div>

      <div className="container-fluid p-0 nav-bar">
        <nav className="navbar navbar-expand-lg bg-none navbar-dark py-3">

          <h1 className="m-0 display-4 font-weight-bold text-uppercase text-white">10 Academy</h1>

          <button type="button" className="navbar-toggler" data-toggle="collapse" data-target="#navbarCollapse">
            <span className="navbar-toggler-icon"></span>
          </button>

        </nav>
      </div>

      <div className="container-fluid p-0">
        <div id="blog-carousel" className="carousel slide" data-ride="carousel">
          <div className="carousel-inner">
            <div className="carousel-item active">
              <div className="carousel-caption d-flex flex-column align-items-center justify-content-center">
                <h2 className="text-primary text-capitalize m-0">Ten Academy Certificate</h2>
                <h3 className="display-2 m-0 mt-2 mt-md-4 text-white font-weight-bold text-capitalize">Join our Job-readiness Program, Earn Certificate</h3>
              </div>
            </div>

          </div>

        </div>
      </div>


      <div className="container gym-className mb-5">
        <div className="row px-3">
          <div className="col-md-6 p-0">
            <div className="gym-className-box d-flex flex-column align-items-end justify-content-center bg-primary text-right text-white py-5 px-5">
              <h3 className="display-4 mb-3 text-white font-weight-bold">Trainee</h3>
              <LoginBtn className="btn btn-lg btn-outline-light mt-4 px-4" to={"trainee"} />
            </div>
          </div>
          <div className="col-md-6 p-0">
            <div className="gym-className-box d-flex flex-column align-items-start justify-content-center bg-secondary text-left text-white py-5 px-5">
              <h3 className="display-4 mb-3 text-white font-weight-bold">Trainer</h3>
              <LoginBtn className="btn btn-lg btn-outline-light mt-4 px-4" to={"trainer"} />
            </div>
          </div>
        </div>
      </div>

      <div className="container py-5">
        <div className="row align-items-center">
          <div className="col-lg-6">
          </div>
          <div className="col-lg-6">
            <h2 className="display-4 font-weight-bold mb-4">About Us</h2>
            <div className="row py-2">
              <div className="col-sm-6">
               
                <h4 className="font-weight-bold">Certified Trainers</h4>
               
              </div>
              <div className="col-sm-6">
                <h4 className="font-weight-bold">Award Winning</h4>
                
              </div>
            </div>
          </div>
        </div>
      </div>


      <div className="footer container-fluid mt-5 py-5 px-sm-3 px-md-5 text-white">
        <div className="row pt-5">
          <div className="col-lg-4 col-md-6 mb-5">
            <h4 className="text-primary mb-4">Get In Touch</h4>
            <div className="d-flex flex-column justify-content-start">
              <Link className="text-white mb-2" to="">123 Street, New York, USA</Link>
              <Link className="text-white mb-2" to="">+012 345 67890</Link>
              <Link className="text-white mb-2" to="">info@example.com</Link>
            </div>
          </div>
          <div className="col-lg-4 col-md-6 mb-5">
            <h4 className="text-primary mb-4">Quick Links</h4>
            <div className="d-flex flex-column justify-content-start">
              <Link className="text-white mb-2" to="#">Home</Link>
              <Link className="text-white mb-2" to="#">About Us</Link>
              <Link className="text-white mb-2" to="#">Our Features</Link>
              <Link className="text-white" to="#"><i className="fa fa-angle-right mr-2"></i>Contact Us</Link>
            </div>
          </div>
          <div className="col-lg-4 col-md-6 mb-5">
            <h4 className="text-primary mb-4">Popular Links</h4>
            <div className="d-flex flex-column justify-content-start">
              <Link className="text-white mb-2" to="#">Home</Link>
              <Link className="text-white mb-2" to="#">About Us</Link>
              <Link className="text-white mb-2" to="#">Our Features</Link>
              <Link className="text-white" to="#"><i className="fa fa-angle-right mr-2"></i>Contact Us</Link>
            </div>
          </div>

        </div>
        <div className="container border-top border-dark pt-5">
          <p className="m-0 text-center text-white">
            &copy; <Link className="text-white font-weight-bold" to="#">TenX</Link>. All Rights Reserved. Credits to:
            <Link className="text-white font-weight-bold" to="https://htmlcodex.com">HTML Codex</Link>
          </p>
        </div>
      </div>
    </div>
  )
}

export default Home