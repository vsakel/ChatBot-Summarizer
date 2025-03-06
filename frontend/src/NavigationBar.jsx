import { Link } from 'react-router-dom'; 
import './NavigationBar.css';

function NavigationBar(){
    return (
        <ul className="navbar">
            <li><Link to="/">Home</Link></li>
            <li><Link to="/upload">Upload</Link></li>
        </ul>  
    )
};

export default NavigationBar;