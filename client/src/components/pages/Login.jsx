// Import necessary components and styles
import Header from './Header/header';
import MyAlgoWallet from './MyAlgoWallet/MyAlgoWallet';
import { Main, MainBody } from '../Main.styles';

const Login = () => {
  // Check if the user is already authenticated
  const isAuthenticated = localStorage.getItem("token");

  // Redirect to the home page if authenticated
  if (isAuthenticated) {
    window.location = "/";
  }

  return (
    // Render the login page layout
    <MainBody>
      <Header />
      <Main>
        <MyAlgoWallet />
      </Main>
    </MainBody>
  );
}

export default Login;
