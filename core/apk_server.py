from flask import Flask, send_file  

app = Flask(__name__)  

@app.route('/update.apk')  
def serve_apk():  
    return send_file("web/update.apk")  

if __name__ == "__main__":  
    app.run(port=8081)  
