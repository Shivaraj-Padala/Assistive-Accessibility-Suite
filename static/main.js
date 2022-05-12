let recognizer = new webkitSpeechRecognition() || new SpeechRecognition();
let listening = false, recognizedTxt = ''
const mic = document.getElementById('mic-btn'),
txtContainer = document.getElementById('text-container'),
micIcon = document.getElementById('mic-icon')

mic.addEventListener('click', ()=>{
    if(listening == false){
        listening = true
        recognizer.start();
        micIcon.classList.add('bx-flashing')
    } else {
        listening = false
        micIcon.classList.remove('bx-flashing')
    }
})

recognizer.addEventListener('result', (e)=>{
    recognizedTxt = e.results[0][0].transcript;
    txtContent = document.createElement('div')
    txtContent.className = 'txt-content'
    txtContainer.appendChild(txtContent)
    txtContent.innerText = recognizedTxt
    fetch(`http://localhost:5000/command?voiceCommand=${recognizedTxt}`).then(resp =>{
        return resp.json();
    }).then(finalresponse =>{
        txtContent = document.createElement('div')
        txtContent.className = 'txt-content'
        txtContainer.appendChild(txtContent)
        txtContent.innerText = finalresponse.commandResponse;
    })
})

recognizer.addEventListener('end', ()=>{
    if(listening==false){
        recognizer.abort();
    } else {
        setTimeout(()=>{
            recognizer.start();
        },50)
    }
})