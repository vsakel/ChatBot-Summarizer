import { Link } from 'react-router-dom'; 
import './NavigationBar.css';

// NavigationBar is a function component that act as a navigation bar for our frontend
function NavigationBar(){
    return (
        <ul className="navbar">
            <li><Link to="/">Home</Link></li>
            <li><Link to="/upload">Upload</Link></li>
        </ul>  
    )
};

export default NavigationBar;