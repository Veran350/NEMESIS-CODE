from flask import Flask, jsonify  
import subprocess  

app = Flask(__name__)  

@app.route('/cmd/<ip>/<command>')  
def execute(ip, command):  
    try:  
        output = subprocess.check_output(f"adb -s {ip} shell {command}", shell=True)  
        return jsonify({"status": "success", "output": output.decode()})  
    except Exception as e:  
        return jsonify({"status": "error", "error": str(e)})  

if __name__ == "__main__":  
    app.run(host="0.0.0.0", port=5000)  
