import React, {  useRef } from 'react'
import { Link } from 'react-router-dom';
import '../assets/css/home.css'

    
const Login_button = (props) => {
    let to=props.to;
    let className = props.className;

    const account = useRef()
    const balance = useRef()


    const connectWallet = async (e) => {
        e.preventDefault()
        
        try {
            await getAccount()
            await getBalance()


        } catch (err) {
            console.log(err)
        }
    }

    const getAccount = async () => {
        try {
            account.current = await reach.getDefaultAccount()
            
            console.log(JSON.stringify(account))
            console.log("Account :" + account.current.networkAccount.addr)
            localStorage.setItem('token', account.current.networkAccount.addr);
            window.location = '/'+to
        } catch (err) {
            console.log(err)
        }
    }

    const getBalance = async () => {
        try {
            let rawBalance = await reach.balanceOf(account.current)
            balance.current = reach.formatCurrency(rawBalance, 4)
            // setAccountBal(balance.current)
            console.log("Balance :" + balance.current)
            localStorage.setItem('balance', balance.current);

        } catch (err) {
            console.log(err)
        }

    }

    return (
        <p>
            <Link onClick={connectWallet} className={className} >Log in</Link>

        </p>
    )
}

export default Login_button