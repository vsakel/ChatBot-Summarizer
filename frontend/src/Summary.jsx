import ReactMarkdown from 'react-markdown';
import './Summary.css';
// need to install react-markdown

function Summary(props) {

    // We store the summary in the state of the UploadPage component. 
    // Then pass it as a prop to the Summary component for display.
    // We also store isReady variable as state and pass it as prop to make the check
    
    if (props.isReady) {
        return (
            <div className='markdown-container'>
                <ReactMarkdown>{props.summary}</ReactMarkdown>
                {/* <p>{props.summary}</p> */}
            </div>
        );
    }


}

export default Summary;