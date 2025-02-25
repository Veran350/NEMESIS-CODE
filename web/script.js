async function loadDevices() {  
    const res = await fetch('/devices.json');  
    const devices = await res.json();  
    const container = document.getElementById('devices');  
    container.innerHTML = devices.map(device => `  
        <div class="device-card">  
            <h3>${device.vendor}</h3>  
            <p>IP: ${device.ip}</p>  
            <p>MAC: ${device.mac}</p>  
            <button onclick="runCmd('${device.ip}', 'ls /sdcard')">View Files</button>  
        </div>  
    `).join('');  
}  

async function runCmd(ip, cmd) {  
    const res = await fetch(`http://localhost:5000/cmd/${ip}/${cmd}`);  
    const data = await res.json();  
    alert(data.output || data.error);  
}  

setInterval(loadDevices, 3000);  
loadDevices();  
