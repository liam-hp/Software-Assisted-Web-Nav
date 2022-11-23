from flask import Flask, render_template, request, jsonify
import webscraper
import NeuralNet

app = Flask(__name__)

@app.route('/connect', methods=['GET','POST'])
def connect():
    if request.method == "POST": # for GET you use request.args.get()
        url=request.form.get('url')
        html=request.form.get('html')
    
    print("data recieved")
    print("url: " + url)
    print("html: " + html)
    button_paths = webscraper.main(html)
    buttons = list("")
    for b in button_paths:
        buttons.append(webscraper.extract_FFL(b))
    print(buttons)

    # identified returns in alphabetical order
    i = len(button_paths[0])-1
    folder = ""
    times = 0
    while(i>0):
        if(button_paths[0][i] == '/'):
            folder = button_paths[0][:i]
            times += 1
            if(times == 2):
                break;
        i-=1
    print(folder)
    identified = NeuralNet.main(folder)

    final_return = list("")
    pos = 0
    while(pos < len(buttons)):
        
        if(buttons[pos] == identified[pos*2]):
            final_return.append(buttons[pos])
        else:
            if(identified[pos*2+1] < .8):
                final_return.append(buttons[pos])
            else:
                print("Unsure of function... conflicting results: "+str(buttons[pos])+", "+str(identified[pos*2])+"("+str(identified[pos*2+1])+"%)")
        pos=pos+1

    return_str = ""
    for f in final_return:
        return_str += f
        return_str += ", "
    return_str = return_str[:len(return_str)-2]
    return return_str

@app.route('/index.html')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='localhost', debug=False, threaded=True, port=8080)
    
