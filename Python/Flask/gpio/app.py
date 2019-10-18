from flask import Flask, render_template, request
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
#greenstate = 0

app = Flask(__name__)
print("starting")
@app.route("/", methods=["GET","POST"])
def index():
	greenstate = "off"
	bluestate = "off"
	print("index called")
	if request.method == 'POST':
		#GPIO.output(17,GPIO.HIGH)
		#GPIO.output(27,GPIO.HIGH)
		mylist = request.form.to_dict()
		try:
			var = mylist["submit1.x"]
			print(GPIO.input(17))
			if GPIO.input(17)  == 1:
				GPIO.output(17, GPIO.LOW)
				greenstate = "off"
				
			else:
				GPIO.output(17, GPIO.HIGH)
				greenstate = "on"
		except:
			print(GPIO.input(27))
			if GPIO.input(27) == 1:
				GPIO.output(27, GPIO.LOW)
				bluestate = "off"
			else:
				GPIO.output(27, GPIO.HIGH)
				bluestate = "on"
		msg = "working?"
	else:
		GPIO.output(17,GPIO.LOW)
		GPIO.output(27,GPIO.LOW)
		msg = "no click yet"
		greenstate = "off"
		bluestate = "off"
	return render_template("index.html", msg=msg, green=greenstate, blue=bluestate)

if __name__ == "__main__":
	print("app called")
	app.run(host="0.0.0.0",port=80)
