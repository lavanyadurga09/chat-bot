from flask import Flask
#create a flask web application
app=Flask(__name__)
#define the route for the home page
@app.route('/')
def hello_world():
   return "hello world!"
#run the application
if __name__=='__main__':
   app.run()