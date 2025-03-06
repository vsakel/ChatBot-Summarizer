import { Link } from 'react-router-dom';
import './HomePage.css';

function HomePage() {
    return (
    <div className='homepage'>
        <h1>Welcome to Tax Documents Summarizer Application</h1>
        <p>
            This is an AI-powered Application, where you can upload a file and the system generates a summary.<br/>
            You can easy upload your file from Upload section in Navigation Bar.
        </p>
        <Link to="/upload"><button>Start</button></Link>
    </div>
    );
}

export default HomePage;
