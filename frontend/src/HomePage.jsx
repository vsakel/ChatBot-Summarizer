import { Link } from 'react-router-dom';
import './HomePage.css';

// HomePage is a function component that renders the Home page, the root page of our application
function HomePage() {
    return (
    <div className='homepage'>
        <h1>Welcome to the Tax Documents Summarizer</h1>
        <p>
            This is an AI-powered Application, that simplifies tax document processing. 
            Upload your files, and the system will generate clear, 
            concise summaries to help you better understand your documents.<br/>
            Let's get started by submit your file using Upload section.
        </p>
        <Link to="/upload"><button>Start</button></Link>
    </div>
    );
}

export default HomePage;
